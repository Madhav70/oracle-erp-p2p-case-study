"""
Northstar Manufacturing Ltd. - Procure-to-Pay (P2P) Sample Data Generator
--------------------------------------------------------------------------
Generates realistic, fully fictional datasets for an Oracle ERP P2P Case Study.
All entities, transactions, and metrics are synthetic and designed for academic
and professional portfolio demonstration.

Output datasets generated in ../data/:
- suppliers.csv
- requisitions.csv
- purchase_orders.csv
- receipts.csv
- invoices.csv
"""

import os
import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# Ensure fixed seed for complete reproducibility
RANDOM_SEED = 42
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. GENERATE SUPPLIERS (25 realistic fictional vendors)
# -------------------------------------------------------------
def generate_suppliers():
    suppliers_data = [
        ("SUP-001", "Apex Industrial Fasteners", "Raw Materials", "Net 30", "Low", 7),
        ("SUP-002", "Vulcan Steelworks Corp", "Raw Materials", "Net 45", "Medium", 14),
        ("SUP-003", "Precision Hydraulics Ltd", "MRO & Tooling", "Net 30", "Low", 10),
        ("SUP-004", "Orion Logistics & Freight", "Logistics", "Net 30", "Low", 5),
        ("SUP-005", "Solenoid Systems Corp", "Raw Materials", "Net 45", "Medium", 12),
        ("SUP-006", "Global Packaging Solutions", "Packaging", "Net 30", "Low", 8),
        ("SUP-007", "Titan Bearings & Drives", "MRO & Tooling", "Net 45", "Low", 10),
        ("SUP-008", "Kinetics Lubricants Inc", "MRO & Tooling", "2/10 Net 30", "Low", 6),
        ("SUP-009", "Benchmark Electricals Ltd", "MRO & Tooling", "Net 30", "Medium", 9),
        ("SUP-010", "AccuPlast Molding Corp", "Raw Materials", "Net 60", "High", 21),
        ("SUP-011", "Nordic Chemical Reagents", "Raw Materials", "Net 45", "Medium", 15),
        ("SUP-012", "Crestview Facilities Management", "Facilities & Services", "Net 30", "Low", 7),
        ("SUP-013", "Ironclad Safety Gear Co", "MRO & Tooling", "Net 30", "Low", 5),
        ("SUP-014", "Matrix Information Technologies", "IT & Telecommunications", "Net 30", "Low", 10),
        ("SUP-015", "Pinnacle Corrugated Boxes", "Packaging", "Net 45", "Low", 8),
        ("SUP-016", "Summit CNC Tooling GmbH", "MRO & Tooling", "Net 60", "Medium", 18),
        ("SUP-017", "AeroMetals Alloy Supply", "Raw Materials", "Net 45", "Medium", 16),
        ("SUP-018", "Fleetlink Transport Services", "Logistics", "Net 30", "Low", 5),
        ("SUP-019", "Quantum Sensor Tech", "Raw Materials", "Net 30", "High", 20),
        ("SUP-020", "CleanRoom Janitorial Supplies", "Facilities & Services", "Net 30", "Low", 5),
        ("SUP-021", "Dynamic Pneumatics Ltd", "MRO & Tooling", "Net 30", "Low", 8),
        ("SUP-022", "Polymer Extrusions Inc", "Raw Materials", "Net 45", "Medium", 14),
        ("SUP-023", "ByteCloud Software Solutions", "IT & Telecommunications", "Net 30", "Low", 3),
        ("SUP-024", "Starlight Industrial Gas", "Raw Materials", "Net 30", "Low", 6),
        ("SUP-025", "Vanguard Security Services", "Facilities & Services", "Net 30", "Low", 7),
    ]
    
    df_suppliers = pd.DataFrame(suppliers_data, columns=[
        "supplier_id", "supplier_name", "category", "payment_terms", "risk_rating", "lead_time_days"
    ])
    df_suppliers["is_active"] = True
    df_suppliers["created_date"] = "2025-11-15"
    return df_suppliers

# -------------------------------------------------------------
# 2. GENERATE PURCHASE REQUISITIONS (250 Records)
# -------------------------------------------------------------
def generate_requisitions(df_suppliers):
    departments = [
        "Manufacturing Operations", "Maintenance & Engineering", "Supply Chain & Logistics",
        "Quality Assurance", "Plant Facilities", "Information Technology", "Health & Safety"
    ]
    
    requesters = {
        "Manufacturing Operations": ["Liam Henderson", "Zoe Patterson", "David Kowalski", "Chloe Martin"],
        "Maintenance & Engineering": ["Arthur Pendelton", "Marcus Brody", "Igor Belov"],
        "Supply Chain & Logistics": ["Sophia Chen", "Trevor Higgins", "Rachel Moore"],
        "Quality Assurance": ["Evelyn Wright", "Brian O'Connor"],
        "Plant Facilities": ["Gary Simmons", "Fiona Gallagher"],
        "Information Technology": ["Alex Rivera", "Derek Vance"],
        "Health & Safety": ["Monique Laurent", "Jason Miller"]
    }
    
    start_date = datetime(2026, 1, 5)
    records = []
    
    for i in range(1, 251):
        pr_id = f"PR-{10000 + i}"
        dept = random.choice(departments)
        requester = random.choice(requesters[dept])
        
        # Date distribution across Jan 2026 to Jun 2026
        days_offset = int(np.random.beta(2, 2) * 175)
        pr_date = start_date + timedelta(days=days_offset)
        
        # Category based on department
        if dept in ["Manufacturing Operations"]:
            cat = random.choices(["Raw Materials", "Packaging"], weights=[0.75, 0.25])[0]
            amount = round(random.uniform(5000, 65000), 2)
        elif dept in ["Maintenance & Engineering"]:
            cat = "MRO & Tooling"
            amount = round(random.uniform(800, 28000), 2)
        elif dept in ["Supply Chain & Logistics"]:
            cat = random.choices(["Packaging", "Logistics"], weights=[0.4, 0.6])[0]
            amount = round(random.uniform(1500, 22000), 2)
        elif dept in ["Information Technology"]:
            cat = "IT & Telecommunications"
            amount = round(random.uniform(1200, 35000), 2)
        elif dept in ["Plant Facilities"]:
            cat = "Facilities & Services"
            amount = round(random.uniform(600, 15000), 2)
        else:
            cat = random.choice(["MRO & Tooling", "Facilities & Services", "Raw Materials"])
            amount = round(random.uniform(400, 12000), 2)
            
        # Approval logic and approval authority tiers
        approval_rand = random.random()
        if approval_rand < 0.88:
            status = "Approved"
            approval_turnaround = random.randint(1, 4)
            approval_date = (pr_date + timedelta(days=approval_turnaround)).strftime('%Y-%m-%d')
            if amount < 5000:
                approver = "Dept Manager - Line Approval"
            elif amount < 25000:
                approver = "Director of Operations"
            else:
                approver = "VP Finance & Operations"
        elif approval_rand < 0.95:
            status = "Rejected"
            approval_turnaround = random.randint(1, 3)
            approval_date = (pr_date + timedelta(days=approval_turnaround)).strftime('%Y-%m-%d')
            approver = "Dept Manager - Budget Exceeded"
        else:
            status = "Pending Approval"
            approval_date = None
            approver = "Pending Routing"
            
        records.append({
            "pr_id": pr_id,
            "pr_date": pr_date.strftime('%Y-%m-%d'),
            "department": dept,
            "requester_name": requester,
            "category": cat,
            "estimated_amount": amount,
            "approval_status": status,
            "approver": approver,
            "approval_date": approval_date,
            "justification": f"Replenishment & operational requirements for {cat} under {dept} budget"
        })
        
    return pd.DataFrame(records)

# -------------------------------------------------------------
# 3. GENERATE PURCHASE ORDERS (from Approved Requisitions)
# -------------------------------------------------------------
def generate_purchase_orders(df_requisitions, df_suppliers):
    approved_prs = df_requisitions[df_requisitions["approval_status"] == "Approved"].copy()
    buyers = ["Rachel Adams (Senior Buyer)", "Marcus Vance (Procurement Specialist)", "Elena Rostova (Lead Buyer)", "David Kim (Purchasing Analyst)"]
    
    po_records = []
    po_counter = 1
    
    for _, pr in approved_prs.iterrows():
        po_id = f"PO-{20000 + po_counter}"
        po_counter += 1
        
        # Pick appropriate supplier matching category
        cat_suppliers = df_suppliers[df_suppliers["category"] == pr["category"]]
        if cat_suppliers.empty:
            cat_suppliers = df_suppliers
        chosen_sup = cat_suppliers.sample(1, random_state=po_counter).iloc[0]
        
        pr_app_dt = datetime.strptime(pr["approval_date"], '%Y-%m-%d')
        # Buyer creates PO 0-3 days after PR approval
        po_date = pr_app_dt + timedelta(days=random.choice([0, 1, 1, 2, 3]))
        
        # Matching Type: Physical categories get 3-way matching; Services get 2-way
        if pr["category"] in ["Raw Materials", "MRO & Tooling", "Packaging"]:
            matching_type = "3-Way Match"
        else:
            matching_type = "2-Way Match"
            
        buyer = random.choice(buyers)
        
        # Slight quote adjustment from estimate (-2% to +3%)
        variance_factor = random.uniform(0.98, 1.03)
        po_amount = round(pr["estimated_amount"] * variance_factor, 2)
        
        # Line count based on spend
        if po_amount < 3000:
            lines = 1
        elif po_amount < 15000:
            lines = random.choice([1, 2, 3])
        else:
            lines = random.choice([2, 3, 5, 8])
            
        po_records.append({
            "po_id": po_id,
            "pr_id": pr["pr_id"],
            "supplier_id": chosen_sup["supplier_id"],
            "supplier_name": chosen_sup["supplier_name"],
            "category": pr["category"],
            "buyer_name": buyer,
            "po_date": po_date.strftime('%Y-%m-%d'),
            "po_amount": po_amount,
            "line_count": lines,
            "payment_terms": chosen_sup["payment_terms"],
            "matching_type": matching_type,
            "lead_time_days": chosen_sup["lead_time_days"],
            "po_status": "Issued" # will be updated once receipts and invoices are generated
        })
        
    return pd.DataFrame(po_records)

# -------------------------------------------------------------
# 4. GENERATE GOODS RECEIPTS (for physical goods POs)
# -------------------------------------------------------------
def generate_receipts(df_pos):
    clerks = ["Tom Bradley (Receiving Lead)", "Sarah Jenkins (Dock Specialist)", "Carlos Mendez (Warehouse Clerk)"]
    receipt_records = []
    rec_counter = 1
    
    # Receipts are generated for 3-Way Match orders primarily
    # Also allow 92% of 3-Way orders to have receipts; some remain unreceived (in transit/open)
    for _, po in df_pos.iterrows():
        if po["matching_type"] == "3-Way Match":
            po_date = datetime.strptime(po["po_date"], '%Y-%m-%d')
            # 8% of POs are recently placed or delayed and not received yet
            if random.random() < 0.08:
                continue
                
            lead_time = po["lead_time_days"]
            # Realistic transit variance: lead_time +/- 3 days
            transit_days = max(2, lead_time + random.randint(-3, 5))
            receipt_date = po_date + timedelta(days=transit_days)
            
            # Don't receipt beyond simulated current date (2026-07-05)
            if receipt_date > datetime(2026, 7, 5):
                continue
                
            receipt_id = f"REC-{30000 + rec_counter}"
            rec_counter += 1
            clerk = random.choice(clerks)
            
            # Receipt condition / inspection
            rec_quality = random.random()
            if rec_quality < 0.94:
                inspection = "Accepted Full"
                received_qty_pct = 100.0
            elif rec_quality < 0.97:
                inspection = "Partial Delivery Received"
                received_qty_pct = 80.0
            else:
                inspection = "Damaged in Transit / Return Recorded"
                received_qty_pct = 90.0
                
            receipt_records.append({
                "receipt_id": receipt_id,
                "po_id": po["po_id"],
                "supplier_id": po["supplier_id"],
                "receipt_date": receipt_date.strftime('%Y-%m-%d'),
                "receiving_clerk": clerk,
                "received_qty_pct": received_qty_pct,
                "inspection_status": inspection,
                "dock_location": random.choice(["Dock A - Raw Intake", "Dock B - Central Bay", "Dock C - Pallet Staging"])
            })
            
    return pd.DataFrame(receipt_records)

# -------------------------------------------------------------
# 5. GENERATE SUPPLIER INVOICES & MATCHING LOGIC
# -------------------------------------------------------------
def generate_invoices(df_pos, df_receipts, df_suppliers):
    invoice_records = []
    inv_counter = 1
    
    receipts_by_po = {r["po_id"]: r for _, r in df_receipts.iterrows()}
    suppliers_dict = {s["supplier_id"]: s for _, s in df_suppliers.iterrows()}
    
    for _, po in df_pos.iterrows():
        po_id = po["po_id"]
        po_date = datetime.strptime(po["po_date"], '%Y-%m-%d')
        has_receipt = po_id in receipts_by_po
        receipt = receipts_by_po.get(po_id)
        
        # Not every PO is invoiced yet (e.g. 90% invoiced)
        if random.random() < 0.08:
            continue
            
        invoice_id = f"INV-{40000 + inv_counter}"
        supplier_inv_ref = f"{po['supplier_id'][:3]}-{random.randint(100000, 999999)}"
        inv_counter += 1
        
        # When does invoice arrive?
        if has_receipt:
            rec_date = datetime.strptime(receipt["receipt_date"], '%Y-%m-%d')
            # 85% arrive after receipt; 15% arrive before receipt (simulating early invoice / missing receipt hold!)
            if random.random() < 0.88:
                invoice_date = rec_date + timedelta(days=random.randint(1, 10))
                arrived_before_receipt = False
            else:
                invoice_date = rec_date - timedelta(days=random.randint(2, 6))
                arrived_before_receipt = True
        else:
            # 2-Way match or PO without receipt
            invoice_date = po_date + timedelta(days=random.randint(4, 18))
            arrived_before_receipt = False
            
        if invoice_date > datetime(2026, 7, 5):
            continue
            
        # Pricing and Exceptions Simulation
        base_amount = po["po_amount"]
        rand_scenario = random.random()
        
        # Scenarios:
        # 1. Clean Match (78%)
        # 2. Minor Variance within tolerance <= 1.5% (6%)
        # 3. Price Discrepancy beyond tolerance > 2.0% (8%)
        # 4. Missing Goods Receipt Hold (5%)
        # 5. Quantity Variance Hold (3%)
        
        if po["matching_type"] == "3-Way Match" and not has_receipt:
            # Arrived with no receipt logged
            inv_amount = base_amount
            match_status = "Hold: Missing Goods Receipt"
            hold_reason = "Goods receipt record not found in system at time of invoice validation"
            hold_resolution = "Awaiting Warehouse Receiving Confirmation"
            payment_status = "On Hold"
            paid_date = None
            pay_ref = None
        elif po["matching_type"] == "3-Way Match" and arrived_before_receipt:
            inv_amount = base_amount
            match_status = "Hold: Missing Goods Receipt"
            hold_reason = "Invoice arrived prior to dock receipt processing"
            hold_resolution = "Hold Released After Dock Receipt Verified"
            payment_status = "Approved for Payment"
            paid_date = (datetime.strptime(receipt["receipt_date"], '%Y-%m-%d') + timedelta(days=25)).strftime('%Y-%m-%d')
            pay_ref = f"EFT-{random.randint(500000, 999999)}"
        elif rand_scenario < 0.78:
            # Perfect Match
            inv_amount = base_amount
            match_status = "Matched"
            hold_reason = "None - Passed Automated Tolerance Check"
            hold_resolution = "Standard Auto-Approval"
            payment_status = "Paid"
            paid_date = (invoice_date + timedelta(days=30)).strftime('%Y-%m-%d')
            pay_ref = f"ACH-{random.randint(500000, 999999)}"
        elif rand_scenario < 0.84:
            # Minor variance within tolerance limit (<= 1.5% or <= $50)
            variance = round(random.uniform(5.0, min(50.0, base_amount * 0.015)), 2)
            inv_amount = round(base_amount + variance, 2)
            match_status = "Matched (Within Tolerance)"
            hold_reason = f"Minor freight/fuel line adjustment (+${variance}) within configured tolerance threshold"
            hold_resolution = "Auto-approved within standard tolerance"
            payment_status = "Paid"
            paid_date = (invoice_date + timedelta(days=30)).strftime('%Y-%m-%d')
            pay_ref = f"ACH-{random.randint(500000, 999999)}"
        elif rand_scenario < 0.93:
            # Price Variance exceeding tolerance (> 2%)
            variance_pct = random.uniform(0.04, 0.12)
            variance_amt = round(base_amount * variance_pct, 2)
            inv_amount = round(base_amount + variance_amt, 2)
            match_status = "Hold: Price Variance"
            hold_reason = f"Invoice line price exceeds PO price by {round(variance_pct*100, 1)}% (+${variance_amt})"
            if random.random() < 0.55:
                hold_resolution = "AP Supervisor Reviewed & Approved Price Amendment"
                payment_status = "Paid"
                paid_date = (invoice_date + timedelta(days=45)).strftime('%Y-%m-%d')
                pay_ref = f"EFT-{random.randint(500000, 999999)}"
            else:
                hold_resolution = "Pending Credit Memo from Supplier"
                payment_status = "On Hold"
                paid_date = None
                pay_ref = None
        else:
            # Quantity variance or partial receipt mismatch
            inv_amount = base_amount
            match_status = "Hold: Quantity Variance"
            hold_reason = "Invoiced quantity exceeds dock received quantity (100% billed vs 80% received)"
            hold_resolution = "Shortage Claim Filed with Supplier / Under Review"
            payment_status = "On Hold"
            paid_date = None
            pay_ref = None
            
        # Due Date based on payment terms
        terms = po["payment_terms"]
        term_days = 30
        if "45" in terms:
            term_days = 45
        elif "60" in terms:
            term_days = 60
        due_date = (invoice_date + timedelta(days=term_days)).strftime('%Y-%m-%d')
        
        invoice_records.append({
            "invoice_id": invoice_id,
            "po_id": po_id,
            "supplier_id": po["supplier_id"],
            "supplier_name": po["supplier_name"],
            "supplier_invoice_ref": supplier_inv_ref,
            "invoice_date": invoice_date.strftime('%Y-%m-%d'),
            "due_date": due_date,
            "invoice_amount": inv_amount,
            "po_amount": base_amount,
            "variance_amount": round(inv_amount - base_amount, 2),
            "matching_type": po["matching_type"],
            "match_status": match_status,
            "hold_reason": hold_reason,
            "hold_resolution": hold_resolution,
            "payment_status": payment_status,
            "paid_date": paid_date,
            "payment_reference": pay_ref
        })
        
    df_inv = pd.DataFrame(invoice_records)
    
    # Update PO statuses based on invoices & receipts
    invoiced_pos = set(df_inv["po_id"])
    receipt_pos = set(df_receipts["po_id"])
    
    po_status_list = []
    for _, po in df_pos.iterrows():
        p_id = po["po_id"]
        if p_id in invoiced_pos:
            inv_match = df_inv[df_inv["po_id"] == p_id].iloc[0]
            if inv_match["payment_status"] == "Paid":
                po_status_list.append("Closed")
            else:
                po_status_list.append("Invoiced - Pending Payment")
        elif p_id in receipt_pos:
            po_status_list.append("Received - Pending Invoice")
        else:
            po_status_list.append("Open - Awaiting Delivery")
            
    df_pos["po_status"] = po_status_list
    return df_inv, df_pos

# -------------------------------------------------------------
# MAIN GENERATION ROUTINE
# -------------------------------------------------------------
def main():
    print("=" * 70)
    print("Northstar Manufacturing Ltd. - P2P Sample Data Generation")
    print("=" * 70)
    
    print("1. Generating Suppliers (25 active vendors)...")
    df_suppliers = generate_suppliers()
    
    print("2. Generating Requisitions (250 procurement requests)...")
    df_requisitions = generate_requisitions(df_suppliers)
    
    print("3. Generating Purchase Orders (from approved requisitions)...")
    df_pos = generate_purchase_orders(df_requisitions, df_suppliers)
    
    print("4. Generating Goods Receipts (for 3-Way matching inventory)...")
    df_receipts = generate_receipts(df_pos)
    
    print("5. Generating Supplier Invoices & Simulating Matching Logic...")
    df_invoices, df_pos = generate_invoices(df_pos, df_receipts, df_suppliers)
    
    # Save CSV files
    suppliers_path = os.path.join(DATA_DIR, "suppliers.csv")
    requisitions_path = os.path.join(DATA_DIR, "requisitions.csv")
    pos_path = os.path.join(DATA_DIR, "purchase_orders.csv")
    receipts_path = os.path.join(DATA_DIR, "receipts.csv")
    invoices_path = os.path.join(DATA_DIR, "invoices.csv")
    
    df_suppliers.to_csv(suppliers_path, index=False)
    df_requisitions.to_csv(requisitions_path, index=False)
    df_pos.to_csv(pos_path, index=False)
    df_receipts.to_csv(receipts_path, index=False)
    df_invoices.to_csv(invoices_path, index=False)
    
    print(f"\nSuccessfully generated and saved datasets to '{DATA_DIR}':")
    print(f" - Suppliers:       {len(df_suppliers):4d} records -> {suppliers_path}")
    print(f" - Requisitions:    {len(df_requisitions):4d} records -> {requisitions_path}")
    print(f" - Purchase Orders: {len(df_pos):4d} records -> {pos_path}")
    print(f" - Goods Receipts:  {len(df_receipts):4d} records -> {receipts_path}")
    print(f" - Invoices:        {len(df_invoices):4d} records -> {invoices_path}")
    print("=" * 70)

if __name__ == "__main__":
    main()
