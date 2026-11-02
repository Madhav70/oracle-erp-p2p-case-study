# Oracle APEX Implementation Specification: Accounts Payable Hold Worklist

**Target Platform**: Oracle APEX (Application Express) 23.x / 24.x on Oracle Autonomous Database (Free Tier)  
**Application Name**: Northstar Procure-to-Pay Command Center  
**Page ID / Alias**: Page 100 (`AP_HOLD_WORKLIST`)  
**Purpose**: Interactive operational screen enabling Accounts Payable specialists and supervisors to review, triage, and release automated matching holds.

---

## 1. Page Component Architecture

```
+----------------------------------------------------------------------------------------------------+
| Page 100: Accounts Payable Matching Hold Worklist                                                 |
+----------------------------------------------------------------------------------------------------+
| [Search Vouchers...]  [Filter by Hold Reason v]  [Filter by Supplier v]  [Export to CSV / Excel]   |
+----------------------------------------------------------------------------------------------------+
| Invoice ID | PO Number | Supplier Name | Billed ($) | PO ($) | Var ($) | Hold Code | Actions       |
+------------+-----------+---------------+------------+--------+---------+-----------+---------------+
| INV-40009  | PO-20010  | Crestview Fac | $11,225.64 | $10.7k | +$458   | PRICE_VAR | [Review/Rel]  |
| INV-40015  | PO-20016  | Ironclad Gear | $10,185.73 | $10.1k | $0.00   | NO_REC    | [Check Dock]  |
| INV-40035  | PO-20038  | Vulcan Steel  | $28,450.00 | $26.1k | +$2.3k  | PRICE_VAR | [Req Credit]  |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Interactive Grid SQL Source Query

```sql
SELECT 
    i.INVOICE_ID,
    i.PO_ID,
    i.SUPPLIER_NAME,
    i.INVOICE_DATE,
    i.DUE_DATE,
    i.INVOICE_AMOUNT,
    i.PO_AMOUNT,
    i.VARIANCE_AMOUNT,
    ROUND((i.VARIANCE_AMOUNT / NULLIF(i.PO_AMOUNT, 0)) * 100, 2) AS VARIANCE_PCT,
    i.MATCH_STATUS,
    i.HOLD_REASON,
    h.HOLD_ID,
    h.HOLD_LOOKUP_CODE,
    ROUND(SYSDATE - i.INVOICE_DATE, 1) AS HOLD_AGING_DAYS,
    CASE 
        WHEN SYSDATE - i.INVOICE_DATE > 7 THEN 'CRITICAL_SLA_BREACH'
        WHEN SYSDATE - i.INVOICE_DATE > 4 THEN 'WARNING_AGING'
        ELSE 'NORMAL'
    END AS SLA_BADGE_CLASS
FROM XXNS_INVOICES i
LEFT JOIN XXNS_AP_HOLDS h ON i.INVOICE_ID = h.INVOICE_ID AND h.STATUS = 'ACTIVE'
WHERE i.PAYMENT_STATUS = 'On Hold'
ORDER BY i.INVOICE_DATE ASC;
```

---

## 3. Interactive Workflow Actions & PL/SQL Dynamic Actions

### Action 1: "Approve Tolerance Override" (AP Supervisor Role)
When a supervisor verifies a legitimate freight surcharge:
```sql
BEGIN
    -- Release hold in audit table
    UPDATE XXNS_AP_HOLDS
       SET STATUS = 'RELEASED',
           RELEASE_LOOKUP_CODE = 'MGR_OVERRIDE',
           RELEASE_REASON = :P100_RELEASE_REASON,
           RELEASE_DATE = SYSTIMESTAMP,
           RELEASED_BY = :APP_USER
     WHERE INVOICE_ID = :P100_SELECTED_INVOICE_ID
       AND STATUS = 'ACTIVE';

    -- Update invoice to approved
    UPDATE XXNS_INVOICES
       SET MATCH_STATUS = 'Matched (Supervisor Override)',
           HOLD_RESOLUTION = :P100_RELEASE_REASON,
           PAYMENT_STATUS = 'Approved for Payment'
     WHERE INVOICE_ID = :P100_SELECTED_INVOICE_ID;

    COMMIT;
END;
```

### Action 2: "Verify Dock Receipt" (Warehouse Dock Link)
Directly queries `XXNS_RECEIPTS` for the PO number and displays dock receiving timestamp and clerk signature to confirm delivery intake.

### Action 3: "Request Supplier Credit Memo"
Generates an automated email notification to the vendor purchasing contact quoting the PO Number, Invoice Reference, and required credit amount (`VARIANCE_AMOUNT`).

---

## 4. APEX Role Authorization Schemes

- **`AP_CLERK_AUTH`**: Can query hold details, attach supplier emails, and request dock verifications. Cannot release price holds exceeding $50.00.
- **`AP_SUPERVISOR_AUTH`**: Full authority to execute price variance overrides and release payment holds.
- **`AUDIT_READONLY`**: View-only access to historical hold releases and audit timestamps.
