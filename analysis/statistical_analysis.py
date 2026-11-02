"""
Northstar Manufacturing Ltd. - Advanced Statistical & Econometric Analysis
--------------------------------------------------------------------------
Applies statistical inference and econometric modeling to Procure-to-Pay data:
1. Computes 95% Wilson Score Confidence Intervals for invoice hold rates.
2. Estimates a Multivariate Logistic Regression model identifying key risk
   drivers of invoice holds (Transaction Amount, 3-Way Matching, Supplier Risk, Category).
3. Produces regression summary tables, odds ratios, and forest plot charts.

Outputs:
- analysis/outputs/statistical_confidence_intervals.csv
- analysis/outputs/hold_regression_model.csv
- analysis/outputs/chart_regression_odds_ratios.png
- assets/images/chart_regression_odds_ratios.png
"""

import os
import shutil
import math
import pandas as pd
import numpy as np
import statsmodels.api as sm

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

def wilson_score_interval(successes, total, confidence=0.95):
    """
    Computes Wilson score confidence interval for binomial proportions
    """
    if total == 0:
        return 0.0, 0.0
    z = 1.95996 # 95% confidence
    p_hat = successes / total
    denominator = 1 + z**2 / total
    centre_adjusted_probability = p_hat + z**2 / (2 * total)
    adjusted_standard_deviation = math.sqrt((p_hat * (1 - p_hat) + z**2 / (4 * total)) / total)
    
    lower_bound = (centre_adjusted_probability - z * adjusted_standard_deviation) / denominator
    upper_bound = (centre_adjusted_probability + z * adjusted_standard_deviation) / denominator
    
    return max(0.0, lower_bound), min(1.0, upper_bound)

def compute_group_confidence_intervals(df, group_col, target_col):
    rows = []
    groups = df[group_col].unique()
    for g in sorted(groups):
        sub = df[df[group_col] == g]
        total = len(sub)
        holds = sub[target_col].sum()
        rate = (holds / total) * 100 if total > 0 else 0.0
        ci_low, ci_high = wilson_score_interval(holds, total)
        rows.append({
            "Grouping Dimension": group_col,
            "Cohort": g,
            "Total Invoices": total,
            "Hold Count": holds,
            "Hold Rate (%)": round(rate, 2),
            "95% CI Lower (%)": round(ci_low * 100, 2),
            "95% CI Upper (%)": round(ci_high * 100, 2)
        })
    return rows

def main():
    print("=" * 70)
    print("Northstar Manufacturing Ltd. - Econometric Hold Regression Engine")
    print("=" * 70)
    
    df_inv = pd.read_csv(os.path.join(DATA_DIR, 'invoices.csv'))
    df_sup = pd.read_csv(os.path.join(DATA_DIR, 'suppliers.csv'))
    df_po = pd.read_csv(os.path.join(DATA_DIR, 'purchase_orders.csv'))
    
    # Merge datasets to create econometric regression matrix
    df_merged = df_inv.merge(df_sup[['supplier_id', 'risk_rating', 'payment_terms']], on='supplier_id', how='left')
    df_merged = df_merged.merge(df_po[['po_id', 'category', 'line_count']], on='po_id', how='left')
    
    # Define binary dependent variable: Has_Hold = 1 if match_status starts with 'Hold'
    df_merged['has_hold'] = df_merged['match_status'].str.startswith('Hold').astype(int)
    
    # 1. COMPUTE 95% WILSON CONFIDENCE INTERVALS
    ci_records = []
    
    # Overall
    total_all = len(df_merged)
    holds_all = df_merged['has_hold'].sum()
    low_all, high_all = wilson_score_interval(holds_all, total_all)
    ci_records.append({
        "Grouping Dimension": "Overall Population",
        "Cohort": "All Invoices",
        "Total Invoices": total_all,
        "Hold Count": holds_all,
        "Hold Rate (%)": round((holds_all / total_all) * 100, 2),
        "95% CI Lower (%)": round(low_all * 100, 2),
        "95% CI Upper (%)": round(high_all * 100, 2)
    })
    
    # By Category
    ci_records.extend(compute_group_confidence_intervals(df_merged, 'category', 'has_hold'))
    # By Matching Type
    ci_records.extend(compute_group_confidence_intervals(df_merged, 'matching_type', 'has_hold'))
    # By Supplier Risk Rating
    ci_records.extend(compute_group_confidence_intervals(df_merged, 'risk_rating', 'has_hold'))
    
    df_ci = pd.DataFrame(ci_records)
    ci_path = os.path.join(OUTPUT_DIR, 'statistical_confidence_intervals.csv')
    df_ci.to_csv(ci_path, index=False)
    print(f"[OK] 95% Confidence Intervals exported to {ci_path}")
    
    # 2. MULTIVARIATE LOGISTIC REGRESSION MODEL
    # y = has_hold
    # X = log(invoice_amount) + is_3way_match + supplier_risk_score + is_raw_materials + is_mro_tooling
    
    reg_df = pd.DataFrame()
    reg_df['has_hold'] = df_merged['has_hold']
    reg_df['log_invoice_amount'] = np.log(df_merged['invoice_amount'])
    reg_df['is_3way_match'] = (df_merged['matching_type'] == '3-Way Match').astype(int)
    
    risk_map = {'Low': 1, 'Medium': 2, 'High': 3}
    reg_df['supplier_risk_score'] = df_merged['risk_rating'].map(risk_map).fillna(1)
    
    reg_df['is_raw_materials'] = (df_merged['category'] == 'Raw Materials').astype(int)
    reg_df['is_mro_tooling'] = (df_merged['category'] == 'MRO & Tooling').astype(int)
    
    # Add constant
    X = reg_df[['log_invoice_amount', 'is_3way_match', 'supplier_risk_score', 'is_raw_materials', 'is_mro_tooling']]
    X = sm.add_constant(X)
    y = reg_df['has_hold']
    
    logit_model = sm.Logit(y, X).fit(disp=False)
    
    # Extract results
    params = logit_model.params
    conf = logit_model.conf_int()
    conf['Odds Ratio'] = np.exp(params)
    conf['OR 95% CI Lower'] = np.exp(conf[0])
    conf['OR 95% CI Upper'] = np.exp(conf[1])
    conf['Coeff'] = params
    conf['Std Err'] = logit_model.bse
    conf['z-value'] = logit_model.tvalues
    conf['p-value'] = logit_model.pvalues
    
    var_labels = {
        'const': 'Intercept',
        'log_invoice_amount': 'Log(Invoice Amount)',
        'is_3way_match': '3-Way Match Required (Physical Dock)',
        'supplier_risk_score': 'Supplier Risk Score (1-3)',
        'is_raw_materials': 'Category: Raw Materials',
        'is_mro_tooling': 'Category: MRO & Tooling'
    }
    
    output_rows = []
    for var, row in conf.iterrows():
        output_rows.append({
            "Variable": var_labels.get(var, var),
            "Coefficient": round(row['Coeff'], 4),
            "Std Error": round(row['Std Err'], 4),
            "z-statistic": round(row['z-value'], 3),
            "p-value": round(row['p-value'], 4),
            "Odds Ratio": round(row['Odds Ratio'], 3),
            "95% CI Lower": round(row['OR 95% CI Lower'], 3),
            "95% CI Upper": round(row['OR 95% CI Upper'], 3),
            "Significance": "***" if row['p-value'] < 0.01 else ("**" if row['p-value'] < 0.05 else ("*" if row['p-value'] < 0.1 else "ns"))
        })
        
    res_df = pd.DataFrame(output_rows)
    reg_path = os.path.join(OUTPUT_DIR, 'hold_regression_model.csv')
    res_df.to_csv(reg_path, index=False)
    print(f"[OK] Econometric Logistic Regression exported to {reg_path}")
    print(f"Pseudo R-Squared: {logit_model.prsquared:.4f} | Log-Likelihood: {logit_model.llf:.2f}")
    print("\n" + res_df.to_string(index=False))
    
    # 3. GENERATE FOREST PLOT / ODDS RATIO CHART
    plot_df = res_df[res_df['Variable'] != 'Intercept'].copy()
    plot_df.sort_values(by='Odds Ratio', ascending=True, inplace=True)
    
    fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
    y_pos = np.arange(len(plot_df))
    
    # Plot reference line at OR = 1.0 (no effect)
    ax.axvline(x=1.0, color='#94a3b8', linestyle='--', linewidth=1.5, alpha=0.8)
    
    # Error bars
    xerr_lower = plot_df['Odds Ratio'] - plot_df['95% CI Lower']
    xerr_upper = plot_df['95% CI Upper'] - plot_df['Odds Ratio']
    
    ax.errorbar(
        plot_df['Odds Ratio'], y_pos,
        xerr=[xerr_lower, xerr_upper],
        fmt='o', color='#1e3a8a', ecolor='#3b82f6',
        elinewidth=2, capsize=5, capthick=1.5, markersize=8
    )
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(plot_df['Variable'], fontsize=9.5, fontweight='bold', color='#1e293b')
    ax.set_xlabel('Odds Ratio (with 95% Confidence Interval, Log Scale)', fontsize=10, labelpad=10, color='#334155')
    ax.set_xscale('log')
    ax.set_title('Multivariate Drivers of Invoice Holds (Logistic Regression)', fontsize=12, fontweight='bold', pad=15, color='#0f172a')
    ax.grid(axis='x', linestyle=':', alpha=0.5, color='#cbd5e1')
    
    # Annotate odds ratios
    for idx, (_, row) in enumerate(plot_df.iterrows()):
        ax.annotate(f"OR={row['Odds Ratio']:.2f} ({row['Significance']})",
                    xy=(row['Odds Ratio'], idx),
                    xytext=(15, 0), textcoords="offset points",
                    va='center', fontsize=8.5, fontweight='bold', color='#0f172a')
        
    plt.tight_layout()
    chart_path = os.path.join(OUTPUT_DIR, 'chart_regression_odds_ratios.png')
    plt.savefig(chart_path)
    plt.close()
    
    shutil.copy(chart_path, os.path.join(IMAGES_DIR, 'chart_regression_odds_ratios.png'))
    print(f"\n[OK] Regression Odds Ratio chart generated: {chart_path}")
    print("=" * 70)

if __name__ == "__main__":
    main()
