-- =============================================================================
-- Northstar Manufacturing Ltd. - Oracle Cloud ERP 3-Way Matching Stored Procedure
-- Simulates the Oracle Payables Validation Engine & Business Unit Tolerance Logic
-- =============================================================================

CREATE OR REPLACE PROCEDURE SP_EXECUTE_3WAY_MATCH (
    p_invoice_id        IN  VARCHAR2,
    p_tolerance_pct     IN  NUMBER   DEFAULT 1.5,  -- 1.5% business unit tolerance
    p_tolerance_amt     IN  NUMBER   DEFAULT 50.00, -- $50.00 dollar cap
    p_out_status        OUT VARCHAR2,
    p_out_hold_reason   OUT VARCHAR2
)
IS
    v_po_id             VARCHAR2(30);
    v_matching_type     VARCHAR2(30);
    v_po_amount         NUMBER(12,2);
    v_inv_amount        NUMBER(12,2);
    v_variance_amt      NUMBER(12,2);
    v_variance_pct      NUMBER(6,2);
    v_receipt_count     NUMBER;
    v_latest_rec_date   DATE;
    v_invoice_date      DATE;
    v_hold_applied      BOOLEAN := FALSE;
    v_hold_code         VARCHAR2(50);
BEGIN
    -- 1. Retrieve Invoice and associated PO Header parameters
    SELECT i.PO_ID, i.INVOICE_AMOUNT, i.PO_AMOUNT, i.INVOICE_DATE, po.MATCHING_TYPE
      INTO v_po_id, v_inv_amount, v_po_amount, v_invoice_date, v_matching_type
      FROM XXNS_INVOICES i
      JOIN XXNS_PURCHASE_ORDERS po ON i.PO_ID = po.PO_ID
     WHERE i.INVOICE_ID = p_invoice_id;

    v_variance_amt := v_inv_amount - v_po_amount;
    IF v_po_amount > 0 THEN
        v_variance_pct := (v_variance_amt / v_po_amount) * 100.0;
    ELSE
        v_variance_pct := 0.0;
    END IF;

    -- 2. Evaluate 3-Way Match vs 2-Way Match Rules
    IF v_matching_type = '3-Way Match' THEN
        -- Query dock receiving records
        SELECT COUNT(*), MAX(RECEIPT_DATE)
          INTO v_receipt_count, v_latest_rec_date
          FROM XXNS_RECEIPTS
         WHERE PO_ID = v_po_id;

        -- Check Rule A: Missing Goods Receipt
        IF v_receipt_count = 0 THEN
            v_hold_applied := TRUE;
            v_hold_code := 'NO REC';
            p_out_status := 'Hold: Missing Goods Receipt';
            p_out_hold_reason := 'Goods receipt record not found in system at time of invoice validation';
        ELSIF v_invoice_date < v_latest_rec_date THEN
            -- Invoice arrived before dock intake
            v_hold_applied := TRUE;
            v_hold_code := 'INV BEFORE REC';
            p_out_status := 'Hold: Missing Goods Receipt';
            p_out_hold_reason := 'Invoice date precedes physical warehouse dock intake timestamp';
        END IF;
    END IF;

    -- Check Rule B: Price Variance Evaluation (if no receipt hold)
    IF NOT v_hold_applied AND v_variance_amt > 0 THEN
        -- Evaluate configured tolerance group thresholds
        IF (v_variance_pct > p_tolerance_pct) AND (v_variance_amt > p_tolerance_amt) THEN
            v_hold_applied := TRUE;
            v_hold_code := 'PRICE VARIANCE';
            p_out_status := 'Hold: Price Variance';
            p_out_hold_reason := 'Billed unit price exceeds PO commitment by ' || TO_CHAR(v_variance_pct, 'FM990.0') || '% (+$' || TO_CHAR(v_variance_amt, 'FM999,990.00') || '), exceeding tolerance threshold';
        ELSE
            -- Within tolerance
            p_out_status := 'Matched (Within Tolerance)';
            p_out_hold_reason := 'Minor price adjustment (+$' || TO_CHAR(v_variance_amt, 'FM990.00') || ') accepted within configured tolerance limit';
        END IF;
    ELSIF NOT v_hold_applied THEN
        p_out_status := 'Matched';
        p_out_hold_reason := 'Clean automated 3-Way match verification passed';
    END IF;

    -- 3. Update Invoice & Insert Hold Audit Record
    IF v_hold_applied THEN
        UPDATE XXNS_INVOICES
           SET MATCH_STATUS = p_out_status,
               HOLD_REASON = p_out_hold_reason,
               PAYMENT_STATUS = 'On Hold'
         WHERE INVOICE_ID = p_invoice_id;

        INSERT INTO XXNS_AP_HOLDS (INVOICE_ID, HOLD_LOOKUP_CODE, HOLD_REASON, STATUS)
        VALUES (p_invoice_id, v_hold_code, p_out_hold_reason, 'ACTIVE');
    ELSE
        UPDATE XXNS_INVOICES
           SET MATCH_STATUS = p_out_status,
               HOLD_REASON = p_out_hold_reason,
               PAYMENT_STATUS = 'Approved for Payment'
         WHERE INVOICE_ID = p_invoice_id;
    END IF;

    COMMIT;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        p_out_status := 'ERROR';
        p_out_hold_reason := 'Invoice ID ' || p_invoice_id || ' not found in Payables database';
    WHEN OTHERS THEN
        ROLLBACK;
        p_out_status := 'EXCEPTION';
        p_out_hold_reason := 'PL/SQL Match Engine Exception: ' || SQLERRM;
END SP_EXECUTE_3WAY_MATCH;
/
