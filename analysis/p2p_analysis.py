"""
Northstar Manufacturing Ltd. - Procure-to-Pay (P2P) Comprehensive Analysis
--------------------------------------------------------------------------
Conducts data quality audits, calculates key operational & financial metrics,
computes cycle times, analyzes invoice discrepancies, and outputs summaries
and professional visualization charts.

Outputs generated in ../analysis/outputs/ and ../assets/images/:
- p2p_summary_metrics.json
- spend_by_supplier.csv
- spend_by_category.csv
- exception_analysis.csv
- cycle_times.csv
- chart_spend_by_category.png
- chart_monthly_spend.png
- chart_exception_breakdown.png
- chart_cycle_times.png
"""

import os
import json
import shutil
from datetime import datetime
import pandas as pd
import numpy as np

# Set matplotlib backend and config to avoid GUI errors and permission warnings
os.environ['MPLCONFIGDIR'] = os.path.join(os.path.dirname(__file__), '.mpl_cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, '..', 'data')
OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'outputs')
IMAGES_DIR = os.path.join(SCRIPT_DIR, '..', 'assets', 'images')

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(os.environ['MPLCONFIGDIR'], exist_ok=True)

def run_data_quality_checks(df_sup, df_req, df_po, df_rec, df_inv):
    """
    Automated Data Quality & Referential Integrity Verifications
    """
    print("\n--- RUNNING AUTOMATED DATA QUALITY AUDIT ---")
    issues = []
    
    # 1. Primary Key Uniqueness
    if df_sup['supplier_id'].duplicated().any():
        issues.append("Duplicate supplier IDs detected")
    if df_req['pr_id'].duplicated().any():
        issues.append("Duplicate PR IDs detected")
    if df_po['po_id'].duplicated().any():
        issues.append("Duplicate PO IDs detected")
    if df_rec['receipt_id'].duplicated().any():
        issues.append("Duplicate Receipt IDs detected")
    if df_inv['invoice_id'].duplicated().any():
        issues.append("Duplicate Invoice IDs detected")
        
    # 2. Foreign Key Referential Integrity
    sup_ids = set(df_sup['supplier_id'])
    po_sup_diff = set(df_po['supplier_id']) - sup_ids
    if po_sup_diff:
        issues.append(f"Orphan supplier IDs in POs: {po_sup_diff}")
        
    pr_ids = set(df_req['pr_id'])
    po_pr_diff = set(df_po['pr_id']) - pr_ids
    if po_pr_diff:
        issues.append(f"Orphan PR IDs in POs: {po_pr_diff}")
        
    po_ids = set(df_po['po_id'])
    rec_po_diff = set(df_rec['po_id']) - po_ids
    if rec_po_diff:
        issues.append(f"Orphan PO IDs in Receipts: {rec_po_diff}")
        
    inv_po_diff = set(df_inv['po_id']) - po_ids
    if inv_po_diff:
        issues.append(f"Orphan PO IDs in Invoices: {inv_po_diff}")
        
    # 3. Numeric Integrity
    if (df_po['po_amount'] <= 0).any():
        issues.append("Non-positive PO amounts detected")
    if (df_inv['invoice_amount'] <= 0).any():
        issues.append("Non-positive Invoice amounts detected")
        
    if not issues:
        print("[PASS] Referential integrity verified: All Foreign Keys map accurately.")
        print("[PASS] Uniqueness check passed: No duplicate primary keys found.")
        print("[PASS] Numeric check passed: All transaction amounts are strictly positive.")
    else:
        for iss in issues:
            print(f"[FAIL] {iss}")
            
    return len(issues) == 0

def analyze_p2p_metrics(df_sup, df_req, df_po, df_rec, df_inv):
    """
    Computes mathematically rigorous P2P performance metrics
    """
    print("\n--- COMPUTING PROCUREMENT & FINANCIAL METRICS ---")
    
    # Financial Totals
    total_po_value = float(df_po['po_amount'].sum())
    total_invoiced_value = float(df_inv['invoice_amount'].sum())
    paid_invoices = df_inv[df_inv['payment_status'] == 'Paid']
    total_paid_value = float(paid_invoices['invoice_amount'].sum())
    
    # Counts
    total_prs = len(df_req)
    approved_prs = len(df_req[df_req['approval_status'] == 'Approved'])
    rejected_prs = len(df_req[df_req['approval_status'] == 'Rejected'])
    pending_prs = len(df_req[df_req['approval_status'] == 'Pending Approval'])
    
    total_pos = len(df_po)
    total_receipts = len(df_rec)
    total_invoices = len(df_inv)
    
    # Discrepancy & Exception Analysis
    # Definition: Exceptions include any hold (Price variance, Missing receipt, Quantity variance)
    exception_invoices = df_inv[df_inv['match_status'].str.startswith('Hold')]
    exception_count = len(exception_invoices)
    clean_matched_count = len(df_inv[df_inv['match_status'].str.startswith('Matched')])
    
    # Metrics definitions:
    # 1. Transaction Discrepancy Rate (Count) = Total Invoices with Exception Holds / Total Invoices Processed
    exception_rate_count = round((exception_count / total_invoices) * 100, 2) if total_invoices > 0 else 0.0
    
    # 2. Value-Weighted Discrepancy Rate = Total Amount of Invoices on Hold / Total Invoiced Amount
    exception_value = float(exception_invoices['invoice_amount'].sum())
    exception_rate_value = round((exception_value / total_invoiced_value) * 100, 2) if total_invoiced_value > 0 else 0.0
    
    # Price Variance Breakdown
    price_var_invs = df_inv[df_inv['match_status'] == 'Hold: Price Variance']
    price_var_count = len(price_var_invs)
    price_var_amt = float(price_var_invs['invoice_amount'].sum())
    total_price_delta = float(df_inv['variance_amount'].sum())
    
    missing_receipt_invs = df_inv[df_inv['match_status'] == 'Hold: Missing Goods Receipt']
    missing_rec_count = len(missing_receipt_invs)
    missing_rec_amt = float(missing_receipt_invs['invoice_amount'].sum())
    
    qty_var_invs = df_inv[df_inv['match_status'] == 'Hold: Quantity Variance']
    qty_var_count = len(qty_var_invs)
    qty_var_amt = float(qty_var_invs['invoice_amount'].sum())
    
    # Cycle Time Computations
    # 1. Requisition Approval Cycle Time: PR Date -> PR Approval Date
    pr_merged = df_req[df_req['approval_date'].notna()].copy()
    pr_merged['approval_days'] = (
        pd.to_datetime(pr_merged['approval_date']) - pd.to_datetime(pr_merged['pr_date'])
    ).dt.days
    avg_pr_approval_days = round(float(pr_merged['approval_days'].mean()), 2)
    median_pr_approval_days = round(float(pr_merged['approval_days'].median()), 2)
    
    # 2. PO Issuance Turnaround: PR Approval Date -> PO Date
    po_pr_merged = df_po.merge(df_req[['pr_id', 'approval_date']], on='pr_id')
    po_pr_merged['po_creation_days'] = (
        pd.to_datetime(po_pr_merged['po_date']) - pd.to_datetime(po_pr_merged['approval_date'])
    ).dt.days
    avg_po_creation_days = round(float(po_pr_merged['po_creation_days'].mean()), 2)
    median_po_creation_days = round(float(po_pr_merged['po_creation_days'].median()), 2)
    
    # 3. Overall Procurement Cycle Time (PR Creation -> PO Issuance)
    po_pr_full = df_po.merge(df_req[['pr_id', 'pr_date']], on='pr_id')
    po_pr_full['full_po_cycle_days'] = (
        pd.to_datetime(po_pr_full['po_date']) - pd.to_datetime(po_pr_full['pr_date'])
    ).dt.days
    avg_po_cycle_days = round(float(po_pr_full['full_po_cycle_days'].mean()), 2)
    median_po_cycle_days = round(float(po_pr_full['full_po_cycle_days'].median()), 2)
    
    # 4. Receipt to Invoice Days (for matched items with receipts)
    inv_rec = df_inv.merge(df_rec[['po_id', 'receipt_date']], on='po_id', how='inner')
    inv_rec['rec_to_inv_days'] = (
        pd.to_datetime(inv_rec['invoice_date']) - pd.to_datetime(inv_rec['receipt_date'])
    ).dt.days
    avg_rec_to_inv_days = round(float(inv_rec['rec_to_inv_days'].mean()), 2)
    
    # 5. Invoice to Payment Days (for paid items)
    paid_invs = df_inv[df_inv['paid_date'].notna()].copy()
    paid_invs['inv_to_pay_days'] = (
        pd.to_datetime(paid_invs['paid_date']) - pd.to_datetime(paid_invs['invoice_date'])
    ).dt.days
    avg_inv_to_pay_days = round(float(paid_invs['inv_to_pay_days'].mean()), 2)
    median_inv_to_pay_days = round(float(paid_invs['inv_to_pay_days'].median()), 2)
    
    # Compile Summary Dictionary
    summary = {
        "metadata": {
            "organization": "Northstar Manufacturing Ltd.",
            "project_name": "Oracle ERP Procure-to-Pay Implementation Simulation",
            "analysis_timestamp": datetime.now().isoformat(),
            "status": "Simulated Analytics - Synthetic Baseline",
            "seed": 42
        },
        "financial_overview": {
            "total_po_value": round(total_po_value, 2),
            "total_invoiced_value": round(total_invoiced_value, 2),
            "total_paid_value": round(total_paid_value, 2),
            "total_price_variance_delta": round(total_price_delta, 2)
        },
        "transaction_counts": {
            "total_suppliers": len(df_sup),
            "total_requisitions": total_prs,
            "approved_requisitions": approved_prs,
            "rejected_requisitions": rejected_prs,
            "pending_requisitions": pending_prs,
            "total_purchase_orders": total_pos,
            "total_goods_receipts": total_receipts,
            "total_invoices": total_invoices,
            "paid_invoices": len(paid_invoices),
            "invoices_on_hold": len(df_inv[df_inv['payment_status'] == 'On Hold']),
            "approved_pending_payment": len(df_inv[df_inv['payment_status'] == 'Approved for Payment'])
        },
        "discrepancy_and_exception_metrics": {
            "clean_matched_count": clean_matched_count,
            "total_exception_count": exception_count,
            "exception_rate_count_pct": exception_rate_count,
            "exception_value": round(exception_value, 2),
            "exception_rate_value_pct": exception_rate_value,
            "price_variance_count": price_var_count,
            "price_variance_value": round(price_var_amt, 2),
            "missing_receipt_count": missing_rec_count,
            "missing_receipt_value": round(missing_rec_amt, 2),
            "quantity_variance_count": qty_var_count,
            "quantity_variance_value": round(qty_var_amt, 2)
        },
        "cycle_time_metrics_days": {
            "pr_approval_time": {
                "mean": avg_pr_approval_days,
                "median": median_pr_approval_days,
                "description": "Days between Requisition submission and Managerial approval"
            },
            "po_creation_turnaround": {
                "mean": avg_po_creation_days,
                "median": median_po_creation_days,
                "description": "Days between PR approval and PO issuance by Buyer"
            },
            "procurement_cycle_time": {
                "mean": avg_po_cycle_days,
                "median": median_po_cycle_days,
                "description": "Total elapsed days from initial Requisition creation to PO issuance"
            },
            "receipt_to_invoice_turnaround": {
                "mean": avg_rec_to_inv_days,
                "description": "Days between physical dock receipt and invoice recording"
            },
            "invoice_to_payment_cycle_time": {
                "mean": avg_inv_to_pay_days,
                "median": median_inv_to_pay_days,
                "description": "Days between invoice recording and final payment disbursement"
            }
        }
    }
    
    # Save JSON summary
    json_path = os.path.join(OUTPUT_DIR, 'p2p_summary_metrics.json')
    with open(json_path, 'w') as f:
        json.dump(summary, f, indent=4)
    print(f"[OK] Summary metrics JSON saved to {json_path}")
    
    # Groupings & Export Tables
    # 1. Spend by Category
    cat_spend = df_po.groupby('category').agg(
        po_count=('po_id', 'count'),
        total_spend=('po_amount', 'sum'),
        avg_po_size=('po_amount', 'mean')
    ).reset_index()
    cat_spend['spend_share_pct'] = round((cat_spend['total_spend'] / total_po_value) * 100, 2)
    cat_spend['total_spend'] = cat_spend['total_spend'].round(2)
    cat_spend['avg_po_size'] = cat_spend['avg_po_size'].round(2)
    cat_spend.sort_values(by='total_spend', ascending=False, inplace=True)
    cat_spend.to_csv(os.path.join(OUTPUT_DIR, 'spend_by_category.csv'), index=False)
    
    # 2. Spend by Supplier with Exception Rate
    sup_pos = df_po.groupby(['supplier_id', 'supplier_name', 'category']).agg(
        po_count=('po_id', 'count'),
        total_committed_spend=('po_amount', 'sum')
    ).reset_index()
    
    sup_invs = df_inv.groupby('supplier_id').agg(
        invoice_count=('invoice_id', 'count'),
        invoiced_amount=('invoice_amount', 'sum'),
        exception_count=('match_status', lambda s: s.str.startswith('Hold').sum()),
        paid_amount=('invoice_amount', lambda s: s[df_inv.loc[s.index, 'payment_status'] == 'Paid'].sum())
    ).reset_index()
    
    sup_analysis = sup_pos.merge(sup_invs, on='supplier_id', how='left').fillna(0)
    sup_analysis['exception_rate_pct'] = np.where(
        sup_analysis['invoice_count'] > 0,
        (sup_analysis['exception_count'] / sup_analysis['invoice_count']) * 100,
        0.0
    ).round(2)
    sup_analysis['total_committed_spend'] = sup_analysis['total_committed_spend'].round(2)
    sup_analysis['invoiced_amount'] = sup_analysis['invoiced_amount'].round(2)
    sup_analysis['paid_amount'] = sup_analysis['paid_amount'].round(2)
    sup_analysis.sort_values(by='total_committed_spend', ascending=False, inplace=True)
    sup_analysis.to_csv(os.path.join(OUTPUT_DIR, 'spend_by_supplier.csv'), index=False)
    
    # 3. Exception Breakdown
    exc_breakdown = df_inv.groupby(['match_status', 'hold_resolution']).agg(
        incident_count=('invoice_id', 'count'),
        total_amount=('invoice_amount', 'sum'),
        total_variance=('variance_amount', 'sum')
    ).reset_index()
    exc_breakdown['total_amount'] = exc_breakdown['total_amount'].round(2)
    exc_breakdown['total_variance'] = exc_breakdown['total_variance'].round(2)
    exc_breakdown.to_csv(os.path.join(OUTPUT_DIR, 'exception_analysis.csv'), index=False)
    
    # 4. Cycle Times Summary Table
    cycle_df = pd.DataFrame([
        {"Stage": "Requisition to Manager Approval", "Average (Days)": avg_pr_approval_days, "Median (Days)": median_pr_approval_days, "Target (Days)": 2.0},
        {"Stage": "Approval to PO Issuance (Buyer Turnaround)", "Average (Days)": avg_po_creation_days, "Median (Days)": median_po_creation_days, "Target (Days)": 1.0},
        {"Stage": "Total Procurement Cycle (PR to PO)", "Average (Days)": avg_po_cycle_days, "Median (Days)": median_po_cycle_days, "Target (Days)": 3.0},
        {"Stage": "Receipt to Invoice Capture", "Average (Days)": avg_rec_to_inv_days, "Median (Days)": "N/A", "Target (Days)": 3.0},
        {"Stage": "Invoice Capture to Payment Disbursement", "Average (Days)": avg_inv_to_pay_days, "Median (Days)": median_inv_to_pay_days, "Target (Days)": 30.0}
    ])
    cycle_df.to_csv(os.path.join(OUTPUT_DIR, 'cycle_times.csv'), index=False)
    
    return summary, cat_spend, sup_analysis, df_inv, df_po

def generate_visualizations(cat_spend, df_inv, df_po, summary):
    """
    Generates 4 high-quality charts matching the executive dashboard
    """
    print("\n--- GENERATING VISUALIZATION CHARTS ---")
    
    # Styling settings
    plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
    plt.rcParams['axes.edgecolor'] = '#cbd5e1'
    plt.rcParams['axes.linewidth'] = 0.8
    
    # 1. Spend by Category Bar Chart
    fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
    colors = ['#1e3a8a', '#2563eb', '#0284c7', '#0d9488', '#10b981', '#64748b']
    bars = ax.barh(cat_spend['category'], cat_spend['total_spend'] / 1e3, color=colors[:len(cat_spend)], edgecolor='none', height=0.6)
    ax.invert_yaxis()
    ax.set_title('Procurement Spend by Category (in $ Thousands)', fontsize=13, fontweight='bold', pad=15, color='#0f172a')
    ax.set_xlabel('Committed PO Spend ($k USD)', fontsize=10, labelpad=10, color='#334155')
    ax.grid(axis='x', linestyle='--', alpha=0.5, color='#94a3b8')
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 15, bar.get_y() + bar.get_height()/2, f"${width:,.1f}k",
                va='center', ha='left', fontsize=9, fontweight='bold', color='#1e293b')
    ax.set_xlim(0, max(cat_spend['total_spend'] / 1e3) * 1.18)
    plt.tight_layout()
    chart1_path = os.path.join(OUTPUT_DIR, 'chart_spend_by_category.png')
    plt.savefig(chart1_path)
    plt.close()
    
    # 2. Monthly Spend Trend
    df_po_copy = df_po.copy()
    df_po_copy['month'] = pd.to_datetime(df_po_copy['po_date']).dt.to_period('M')
    monthly_trend = df_po_copy.groupby('month')['po_amount'].sum().reset_index()
    monthly_trend['month_str'] = monthly_trend['month'].astype(str)
    
    fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
    ax.plot(monthly_trend['month_str'], monthly_trend['po_amount'] / 1e3, marker='o', linewidth=2.5, markersize=8, color='#0284c7')
    ax.fill_between(monthly_trend['month_str'], monthly_trend['po_amount'] / 1e3, alpha=0.15, color='#38bdf8')
    ax.set_title('Monthly Committed Purchase Order Volume (Jan - Jun 2026)', fontsize=13, fontweight='bold', pad=15, color='#0f172a')
    ax.set_ylabel('Committed Spend ($k USD)', fontsize=10, labelpad=10, color='#334155')
    ax.set_xlabel('PO Issuance Month', fontsize=10, labelpad=10, color='#334155')
    ax.grid(True, linestyle='--', alpha=0.5, color='#94a3b8')
    for x, y in zip(monthly_trend['month_str'], monthly_trend['po_amount'] / 1e3):
        ax.annotate(f"${y:,.1f}k", (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, fontweight='bold', color='#0369a1')
    ax.set_ylim(0, max(monthly_trend['po_amount'] / 1e3) * 1.25)
    plt.tight_layout()
    chart2_path = os.path.join(OUTPUT_DIR, 'chart_monthly_spend.png')
    plt.savefig(chart2_path)
    plt.close()
    
    # 3. Invoice Exception Distribution (Donut Chart)
    exc_metrics = summary['discrepancy_and_exception_metrics']
    labels = ['Clean 3-Way/2-Way Match', 'Price Variance Hold', 'Missing Receipt Hold', 'Quantity Variance Hold']
    counts = [
        exc_metrics['clean_matched_count'],
        exc_metrics['price_variance_count'],
        exc_metrics['missing_receipt_count'],
        exc_metrics['quantity_variance_count']
    ]
    colors_donut = ['#10b981', '#f59e0b', '#ef4444', '#8b5cf6']
    
    fig, ax = plt.subplots(figsize=(8, 5.2), dpi=150)
    wedges, texts, autotexts = ax.pie(
        counts, 
        labels=None, 
        autopct='%1.1f%%', 
        pctdistance=0.75,
        startangle=140, 
        colors=colors_donut,
        wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2)
    )
    for at in autotexts:
        at.set_color('white')
        at.set_weight('bold')
        at.set_fontsize(10)
    ax.legend(wedges, [f"{l} ({c})" for l, c in zip(labels, counts)], title="Invoice Status Breakdown", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)
    ax.set_title(f"Supplier Invoice Matching & Hold Distribution\n(Total Invoices = {summary['transaction_counts']['total_invoices']})", fontsize=12, fontweight='bold', pad=15, color='#0f172a')
    plt.tight_layout()
    chart3_path = os.path.join(OUTPUT_DIR, 'chart_exception_breakdown.png')
    plt.savefig(chart3_path)
    plt.close()
    
    # 4. Cycle Times Comparison (Actual Simulated vs Target Assumption)
    stages = [
        'PR Manager\nApproval',
        'Buyer PO\nTurnaround',
        'Full Procurement\nCycle (PR-PO)',
        'Dock Receipt\nto Invoice'
    ]
    simulated_vals = [
        summary['cycle_time_metrics_days']['pr_approval_time']['mean'],
        summary['cycle_time_metrics_days']['po_creation_turnaround']['mean'],
        summary['cycle_time_metrics_days']['procurement_cycle_time']['mean'],
        summary['cycle_time_metrics_days']['receipt_to_invoice_turnaround']['mean']
    ]
    target_vals = [2.0, 1.0, 3.0, 3.0]
    
    x = np.arange(len(stages))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
    rects1 = ax.bar(x - width/2, simulated_vals, width, label='Current Simulated (Mean Days)', color='#3b82f6')
    rects2 = ax.bar(x + width/2, target_vals, width, label='To-Be ERP SLA Target', color='#10b981')
    
    ax.set_title('P2P Cycle Times: Simulated Current Performance vs Target ERP SLA', fontsize=12, fontweight='bold', pad=15, color='#0f172a')
    ax.set_ylabel('Duration (Elapsed Days)', fontsize=10, labelpad=10, color='#334155')
    ax.set_xticks(x)
    ax.set_xticklabels(stages, fontsize=9)
    ax.legend(fontsize=9)
    ax.grid(axis='y', linestyle='--', alpha=0.5, color='#94a3b8')
    
    for r in rects1:
        h = r.get_height()
        ax.annotate(f"{h:.1f}d", xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 4), textcoords="offset points", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#1d4ed8')
    for r in rects2:
        h = r.get_height()
        ax.annotate(f"{h:.1f}d", xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 4), textcoords="offset points", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#047857')
        
    ax.set_ylim(0, max(simulated_vals) * 1.3)
    plt.tight_layout()
    chart4_path = os.path.join(OUTPUT_DIR, 'chart_cycle_times.png')
    plt.savefig(chart4_path)
    plt.close()
    
    # Copy charts to assets/images for website consumption
    for c_path in [chart1_path, chart2_path, chart3_path, chart4_path]:
        shutil.copy(c_path, IMAGES_DIR)
        
    print(f"[OK] 4 High-Resolution Charts created in '{OUTPUT_DIR}' and synced to '{IMAGES_DIR}'.")

def main():
    print("=" * 70)
    print("Northstar Manufacturing Ltd. - P2P Analytics & Integrity Engine")
    print("=" * 70)
    
    # Load raw datasets
    df_sup = pd.read_csv(os.path.join(DATA_DIR, 'suppliers.csv'))
    df_req = pd.read_csv(os.path.join(DATA_DIR, 'requisitions.csv'))
    df_po = pd.read_csv(os.path.join(DATA_DIR, 'purchase_orders.csv'))
    df_rec = pd.read_csv(os.path.join(DATA_DIR, 'receipts.csv'))
    df_inv = pd.read_csv(os.path.join(DATA_DIR, 'invoices.csv'))
    
    # Run QA checks
    is_valid = run_data_quality_checks(df_sup, df_req, df_po, df_rec, df_inv)
    if not is_valid:
        print("[WARNING] Data quality issues encountered! Halting.")
        return
        
    # Analyze metrics
    summary, cat_spend, sup_analysis, df_inv, df_po = analyze_p2p_metrics(df_sup, df_req, df_po, df_rec, df_inv)
    
    # Generate Visualizations
    generate_visualizations(cat_spend, df_inv, df_po, summary)
    
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE - EXECUTIVE SUMMARY METRICS:")
    print(f"Total Committed PO Spend:      ${summary['financial_overview']['total_po_value']:,.2f}")
    print(f"Total Invoiced Amount:         ${summary['financial_overview']['total_invoiced_value']:,.2f}")
    print(f"Total Paid Invoices Value:     ${summary['financial_overview']['total_paid_value']:,.2f}")
    print(f"Total Invoices Processed:      {summary['transaction_counts']['total_invoices']}")
    print(f"Invoice Exception Holds:       {summary['discrepancy_and_exception_metrics']['total_exception_count']} ({summary['discrepancy_and_exception_metrics']['exception_rate_count_pct']}%)")
    print(f"Average PR Approval Turnaround:{summary['cycle_time_metrics_days']['pr_approval_time']['mean']} days")
    print(f"Average PR-to-PO Cycle Time:   {summary['cycle_time_metrics_days']['procurement_cycle_time']['mean']} days")
    print("=" * 70)

if __name__ == "__main__":
    main()
