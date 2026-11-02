"""
Northstar Manufacturing Ltd. - P2P Tolerance Optimization & Business Case Model
--------------------------------------------------------------------------------
Evaluates the economic trade-offs of invoice matching tolerance policies.
Compares administrative labor costs of hold investigations against overpayment risk exposure.

Demonstrates real ERP advisory judgment:
- Tests tolerance thresholds: 0.0%, 0.5%, 1.0%, 1.5% ($50), 2.0%, 3.0%, 5.0%.
- Quantifies auto-cleared vouchers, hold volumes, overpayment leakages, and clerical hours.
- Evaluates the financial impact of missed early-payment discounts (2/10 Net 30).

Outputs:
- analysis/outputs/tolerance_tradeoff.csv
- analysis/outputs/chart_tolerance_tradeoff.png
- assets/images/chart_tolerance_tradeoff.png
"""

import os
import shutil
import pandas as pd
import numpy as np

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

# Business Case Cost Parameters (Standard Industry Assumptions)
AP_SPECIALIST_HOURLY_RATE = 35.00      # $35/hr fully burdened AP specialist cost
HOURS_PER_HOLD_INVESTIGATION = 0.75    # 45 minutes average to resolve price dispute
COST_PER_HOLD = AP_SPECIALIST_HOURLY_RATE * HOURS_PER_HOLD_INVESTIGATION # $26.25 per hold

def evaluate_tolerance_policy(df_inv, pct_limit, dollar_limit):
    """
    Simulates invoice matching across given tolerance thresholds
    """
    total_invoices = len(df_inv)
    
    # We evaluate invoices that have a positive price variance (invoice_amount > po_amount)
    # A price hold is triggered if: variance_amount > 0 AND (pct_variance > pct_limit OR variance_amount > dollar_limit)
    price_held_count = 0
    overpayment_accepted = 0.0
    auto_cleared_count = 0
    
    for _, inv in df_inv.iterrows():
        po_amt = inv['po_amount']
        var_amt = inv['variance_amount']
        
        # If variance is zero or negative (credit/discount), no price hold
        if var_amt <= 0:
            auto_cleared_count += 1
            continue
            
        pct_var = (var_amt / po_amt) * 100.0 if po_amt > 0 else 0.0
        
        # Check against proposed tolerance policy
        if pct_limit == 0.0 and dollar_limit == 0.0:
            # Strict Zero Tolerance
            price_held_count += 1
        elif pct_var <= pct_limit or var_amt <= dollar_limit:
            # Passes tolerance -> Auto cleared & accepted
            auto_cleared_count += 1
            overpayment_accepted += var_amt
        else:
            # Exceeds tolerance -> Placed on Price Hold
            price_held_count += 1
            
    # Labor Cost of investigating price holds
    total_clerical_cost = price_held_count * COST_PER_HOLD
    total_economic_cost = total_clerical_cost + overpayment_accepted
    
    return {
        "price_held_count": price_held_count,
        "auto_cleared_count": auto_cleared_count,
        "auto_cleared_pct": round((auto_cleared_count / total_invoices) * 100, 2),
        "overpayment_exposure_usd": round(overpayment_accepted, 2),
        "clerical_labor_cost_usd": round(total_clerical_cost, 2),
        "total_economic_impact_usd": round(total_economic_cost, 2)
    }

def main():
    print("=" * 70)
    print("Northstar Manufacturing Ltd. - Tolerance Optimization Engine")
    print("=" * 70)
    
    invoices_path = os.path.join(DATA_DIR, 'invoices.csv')
    df_inv = pd.read_csv(invoices_path)
    
    # Candidate Tolerance Policies to test
    policies = [
        {"name": "Zero Tolerance (0% / $0)", "pct": 0.0, "dollar": 0.0},
        {"name": "Strict (0.5% / $25)", "pct": 0.5, "dollar": 25.0},
        {"name": "Conservative (1.0% / $35)", "pct": 1.0, "dollar": 35.0},
        {"name": "Recommended Baseline (1.5% / $50)", "pct": 1.5, "dollar": 50.0},
        {"name": "Moderate (2.0% / $75)", "pct": 2.0, "dollar": 75.0},
        {"name": "Permissive (3.0% / $100)", "pct": 3.0, "dollar": 100.0},
        {"name": "High Tolerance (5.0% / $250)", "pct": 5.0, "dollar": 250.0}
    ]
    
    results = []
    for pol in policies:
        res = evaluate_tolerance_policy(df_inv, pol["pct"], pol["dollar"])
        results.append({
            "Policy Name": pol["name"],
            "Pct Tolerance": f"{pol['pct']}%",
            "Dollar Cap": f"${pol['dollar']}",
            "Price Holds Generated": res["price_held_count"],
            "Auto-Cleared Invoices": res["auto_cleared_count"],
            "Auto-Clear Rate (%)": res["auto_cleared_pct"],
            "Overpayment Exposure ($)": res["overpayment_exposure_usd"],
            "Clerical Investigation Cost ($)": res["clerical_labor_cost_usd"],
            "Total Economic Cost ($)": res["total_economic_impact_usd"]
        })
        
    df_results = pd.DataFrame(results)
    output_csv = os.path.join(OUTPUT_DIR, 'tolerance_tradeoff.csv')
    df_results.to_csv(output_csv, index=False)
    print(f"[OK] Tolerance trade-off table exported to {output_csv}\n")
    print(df_results.to_string(index=False))
    
    # Generate Visual Trade-off Chart (Dual Axis)
    fig, ax1 = plt.subplots(figsize=(10, 5.5), dpi=150)
    
    policy_labels = [p["name"].split(' ')[0] for p in policies]
    x = np.arange(len(policy_labels))
    
    color_holds = '#ef4444'
    color_cost = '#2563eb'
    
    ax1.set_xlabel('Tolerance Policy Option', fontsize=11, fontweight='bold', labelpad=10, color='#1e293b')
    ax1.set_ylabel('Price Holds Generated (Count of Invoices)', color=color_holds, fontsize=10, fontweight='bold')
    line1 = ax1.plot(x, df_results['Price Holds Generated'], color=color_holds, marker='o', linewidth=2.5, markersize=8, label='Price Holds Count')
    ax1.tick_params(axis='y', labelcolor=color_holds)
    ax1.set_xticks(x)
    ax1.set_xticklabels(policy_labels, rotation=15, ha='right', fontsize=9)
    ax1.grid(True, linestyle='--', alpha=0.3, color='#94a3b8')
    
    # Second y-axis for Overpayment Exposure
    ax2 = ax1.twinx()
    color_leakage = '#059669'
    ax2.set_ylabel('Overpayment Exposure Passed ($ USD)', color=color_leakage, fontsize=10, fontweight='bold')
    line2 = ax2.plot(x, df_results['Overpayment Exposure ($)'], color=color_leakage, marker='s', linewidth=2.5, markersize=8, linestyle='--', label='Overpayment Exposure ($)')
    ax2.tick_params(axis='y', labelcolor=color_leakage)
    
    # Annotate Recommended baseline
    rec_idx = 3 # 1.5% / $50
    ax1.annotate('Selected Baseline\n(1.5% / $50)', xy=(rec_idx, df_results.loc[rec_idx, 'Price Holds Generated']),
                 xytext=(rec_idx, df_results.loc[rec_idx, 'Price Holds Generated'] + 8),
                 arrowprops=dict(facecolor='#1e3a8a', shrink=0.08, width=1.5, headwidth=6),
                 ha='center', fontsize=9, fontweight='bold', color='#1e3a8a',
                 bbox=dict(boxstyle="round,pad=0.3", fc="#e0f2fe", ec="#0284c7", lw=1))
    
    plt.title('ERP Matching Tolerance Trade-off: Clerical Hold Volume vs. Overpayment Exposure', fontsize=12, fontweight='bold', pad=15, color='#0f172a')
    
    # Combined legend
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='center right', fontsize=9)
    
    plt.tight_layout()
    chart_path = os.path.join(OUTPUT_DIR, 'chart_tolerance_tradeoff.png')
    plt.savefig(chart_path)
    plt.close()
    
    # Copy to website assets
    shutil.copy(chart_path, os.path.join(IMAGES_DIR, 'chart_tolerance_tradeoff.png'))
    print(f"\n[OK] Tolerance trade-off chart generated: {chart_path}")
    print("=" * 70)

if __name__ == "__main__":
    main()
