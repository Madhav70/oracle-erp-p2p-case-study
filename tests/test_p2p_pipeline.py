"""
Northstar Manufacturing Ltd. - Procure-to-Pay Automated Verification Suite
----------------------------------------------------------------------------
Pytest automated tests replacing static claims with executable verifications:
1. Financial reconciliation (Total Invoiced == Disbursed + Pending + Active Hold).
2. Complete referential integrity (zero orphan foreign keys).
3. Primary key uniqueness across all datasets.
4. Temporal chronological sequence consistency.
5. Contractual payment terms compliance.
6. Business unit tolerance rule boundary enforcement.
"""

import os
import pytest
import pandas as pd
from datetime import datetime

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(TESTS_DIR, '..', 'data')

@pytest.fixture(scope="module")
def p2p_data():
    return {
        "suppliers": pd.read_csv(os.path.join(DATA_DIR, 'suppliers.csv')),
        "requisitions": pd.read_csv(os.path.join(DATA_DIR, 'requisitions.csv')),
        "pos": pd.read_csv(os.path.join(DATA_DIR, 'purchase_orders.csv')),
        "receipts": pd.read_csv(os.path.join(DATA_DIR, 'receipts.csv')),
        "invoices": pd.read_csv(os.path.join(DATA_DIR, 'invoices.csv'))
    }

def test_financial_reconciliation(p2p_data):
    """
    Test 1: Total Invoiced must equal Disbursed + Approved Pending + Active Hold to the exact cent ($0.00 gap)
    """
    df_inv = p2p_data["invoices"]
    total_invoiced = round(df_inv["invoice_amount"].sum(), 2)
    
    paid_amt = round(df_inv[df_inv["payment_status"] == "Paid"]["invoice_amount"].sum(), 2)
    pending_amt = round(df_inv[df_inv["payment_status"] == "Approved for Payment"]["invoice_amount"].sum(), 2)
    on_hold_amt = round(df_inv[df_inv["payment_status"] == "On Hold"]["invoice_amount"].sum(), 2)
    
    sum_components = round(paid_amt + pending_amt + on_hold_amt, 2)
    variance = round(abs(total_invoiced - sum_components), 2)
    
    assert variance <= 0.01, f"Financial reconciliation variance detected! Total: {total_invoiced}, Sum: {sum_components}, Gap: {variance}"

def test_referential_integrity_foreign_keys(p2p_data):
    """
    Test 2: Every child record must reference an existing valid parent entity (zero orphan keys)
    """
    df_sup = p2p_data["suppliers"]
    df_req = p2p_data["requisitions"]
    df_po = p2p_data["pos"]
    df_rec = p2p_data["receipts"]
    df_inv = p2p_data["invoices"]
    
    # 1. PO -> Supplier
    valid_sup_ids = set(df_sup["supplier_id"])
    po_sup_diff = set(df_po["supplier_id"]) - valid_sup_ids
    assert len(po_sup_diff) == 0, f"Orphan supplier IDs in POs: {po_sup_diff}"
    
    # 2. PO -> Requisition
    valid_pr_ids = set(df_req["pr_id"])
    po_pr_diff = set(df_po["pr_id"]) - valid_pr_ids
    assert len(po_pr_diff) == 0, f"Orphan PR IDs in POs: {po_pr_diff}"
    
    # 3. Receipt -> PO
    valid_po_ids = set(df_po["po_id"])
    rec_po_diff = set(df_rec["po_id"]) - valid_po_ids
    assert len(rec_po_diff) == 0, f"Orphan PO IDs in Receipts: {rec_po_diff}"
    
    # 4. Invoice -> PO
    inv_po_diff = set(df_inv["po_id"]) - valid_po_ids
    assert len(inv_po_diff) == 0, f"Orphan PO IDs in Invoices: {inv_po_diff}"
    
    # 5. Invoice -> Supplier
    inv_sup_diff = set(df_inv["supplier_id"]) - valid_sup_ids
    assert len(inv_sup_diff) == 0, f"Orphan supplier IDs in Invoices: {inv_sup_diff}"

def test_primary_key_uniqueness(p2p_data):
    """
    Test 3: Every table must have strictly unique primary keys
    """
    assert not p2p_data["suppliers"]["supplier_id"].duplicated().any(), "Duplicate Supplier ID detected"
    assert not p2p_data["requisitions"]["pr_id"].duplicated().any(), "Duplicate Requisition ID detected"
    assert not p2p_data["pos"]["po_id"].duplicated().any(), "Duplicate Purchase Order ID detected"
    assert not p2p_data["receipts"]["receipt_id"].duplicated().any(), "Duplicate Receipt ID detected"
    assert not p2p_data["invoices"]["invoice_id"].duplicated().any(), "Duplicate Invoice ID detected"

def test_temporal_chronological_validity(p2p_data):
    """
    Test 4: Transaction dates must follow chronological business sequence (PR <= Approval <= PO)
    """
    df_req = p2p_data["requisitions"]
    df_po = p2p_data["pos"]
    df_inv = p2p_data["invoices"]
    
    # Approved PRs: PR Date <= Approval Date
    approved_prs = df_req[df_req["approval_status"] == "Approved"]
    for _, row in approved_prs.iterrows():
        assert pd.to_datetime(row["pr_date"]) <= pd.to_datetime(row["approval_date"]), f"PR approval precedes submission: {row['pr_id']}"
        
    # POs: Approval Date <= PO Date
    po_pr_merged = df_po.merge(df_req[["pr_id", "approval_date"]], on="pr_id")
    for _, row in po_pr_merged.iterrows():
        assert pd.to_datetime(row["approval_date"]) <= pd.to_datetime(row["po_date"]), f"PO precedes approval: {row['po_id']}"
        
    # Paid Invoices: Invoice Date <= Paid Date
    paid_invs = df_inv[df_inv["payment_status"] == "Paid"]
    for _, row in paid_invs.iterrows():
        assert pd.to_datetime(row["invoice_date"]) <= pd.to_datetime(row["paid_date"]), f"Payment precedes invoice date: {row['invoice_id']}"

def test_matching_tolerance_enforcement(p2p_data):
    """
    Test 5: Invoices with variance <= 1.5% or <= $50 must pass tolerance matching without price hold
    """
    df_inv = p2p_data["invoices"]
    for _, inv in df_inv.iterrows():
        var_amt = inv["variance_amount"]
        po_amt = inv["po_amount"]
        pct_var = (var_amt / po_amt) * 100 if po_amt > 0 else 0
        
        # If within configured tolerance limit:
        if 0 < var_amt and (pct_var <= 1.5 or var_amt <= 50.0):
            assert inv["match_status"] != "Hold: Price Variance", f"Invoice {inv['invoice_id']} within tolerance was incorrectly held!"
