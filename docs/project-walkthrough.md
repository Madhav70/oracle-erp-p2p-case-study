# Project Walkthrough — Oracle ERP P2P Case Study

**Northstar Manufacturing Ltd. | Fictional Portfolio Case Study**

---

## Slide 1 — The Problem

### Northstar Manufacturing Ltd. had a broken procurement process

A fictional mid-sized manufacturer with **\$2.67M in annual invoiced spend** across 25 suppliers suffered from:

| Pain Point | Measured Symptom |
| :--- | :--- |
| No standardised requisition channel | 2.5-day average approval delay (target: ≤ 2.0 days) |
| No automated approval routing | Unauthorised commitments, unclear accountability |
| Paper-based dock receiving | 18 invoices held for "Missing Goods Receipt" |
| Manual invoice matching | **20.8% invoice exception rate** (43 of 207 invoices held) |
| Zero real-time visibility | Monthly spreadsheet-only reporting |

**Financial consequence**: \$299,208 (11.2% of total invoiced value) locked in active holds at any point in time — delaying supplier payments and risking early-payment discount forfeiture.

---

## Slide 2 — Real-World Benchmarking (BPI 2019)

### Is 20.8% hold rate a problem, or normal?

The **BPI Challenge 2019** dataset provides empirical ground truth from a real enterprise (AkzoNobel, 251,734 purchase-order event log cases, CC BY 4.0).

```
                              Real Enterprise    Northstar     Oracle Cloud
                               (BPI 2019)        Baseline       Target SLA
                              ─────────────    ──────────     ──────────────
Invoice Hold / Exception Rate    28.2%          20.8%          ≤ 8.0%
Straight-Through Processing      54.6%          79.2%          ≥ 85.0%
Early Invoice Rate               19.4%           8.7%          ≤ 3.0%
Avg Invoice Clearance Cycle      38.4 days      33.7 days      Terms (30–45d)
```

**Key insight**: Northstar's 20.8% hold rate is **below** a real enterprise's 28.2%, confirming the simulation is conservative. Both are far above the 8% Oracle Cloud target — confirming the implementation has a real problem to solve.

The improvement pathway from 20.8% → ≤ 8% requires:
1. Automated 3-way matching with configured tolerance rules
2. Structured dock-receipt logging (eliminating "Missing GR" holds)
3. Supplier on-boarding with price-catalogue anchoring

---

## Slide 3 — Tolerance Trade-off Analysis

### The real consulting decision: how tight should the tolerance rule be?

Every Oracle Payables implementation requires configuring a **matching tolerance group** — the percentage/dollar threshold below which an invoice variance is automatically accepted.

This project modelled seven policies across the 207-invoice dataset:

| Policy | Price Holds | Auto-Clear Rate | Overpayment Exposure | Clerical Cost | Total Cost |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Zero Tolerance (0% / \$0) | 23 | 88.9% | \$0 | \$604 | \$604 |
| Strict (0.5% / \$25) | 13 | 93.7% | \$227 | \$341 | **\$568** |
| **Current Design (1.5% / \$50)** | **12** | **94.2%** | **\$257** | **\$315** | **\$572** |
| Moderate (2.0% / \$75) | 11 | 94.7% | \$312 | \$289 | \$601 |
| Permissive (3.0% / \$100) | 10 | 95.2% | \$407 | \$263 | \$669 |
| High Tolerance (5.0% / \$250) | 8 | 96.1% | \$775 | \$210 | \$985 |

> **Clerical cost assumption**: \$35/hour × 0.75 hours per hold investigation.  
> **Overpayment exposure**: Cumulative invoice variance on auto-cleared invoices.

**Recommendation to the Controller**: The 1.5% / \$50 rule is defensible — it sits at the economic minimum. Moving to 0.5% / \$25 saves \$4 but doubles the number of price holds from 12 to 13. Moving to 3.0% / \$100 increases total economic cost by \$97 while passing \$150 of additional overpayment risk. **The current design is near-optimal.**

This analysis replaces a static policy recommendation with a **quantified trade-off** — the type of analysis a P2P consultant presents to a Controller during solution design.

---

## Slide 4 — Oracle Fusion Cloud Design

### Moving from concept to Oracle objects

| Design Artefact | File | Purpose |
| :--- | :--- | :--- |
| Database Schema | `oracle/p2p_tables_ddl.sql` | Six tables (`XXNS_` prefix) for Oracle Autonomous DB |
| Matching Engine | `oracle/oracle_fusion_matching_engine.sql` | PL/SQL `SP_EXECUTE_3WAY_MATCH` stored procedure |
| APEX Hold Worklist | `oracle/apex_hold_worklist_spec.md` | Page 100 interactive-grid spec, RBAC auth, hold-release logic |
| Object Mapping | `oracle/oracle_fusion_mapping_dictionary.md` | CSV columns → Oracle Fusion tables and REST API paths |

### CSV → Oracle Fusion Object Mapping

| Dataset | Oracle Fusion Table | Oracle REST Path |
| :--- | :--- | :--- |
| `suppliers.csv` | `POZ_SUPPLIERS` / `HZ_PARTIES` | `/fscmRestApi/resources/11.13.18.05/suppliers` |
| `purchase_orders.csv` | `PO_HEADERS_ALL` / `PO_LINES_ALL` | `/fscmRestApi/resources/11.13.18.05/purchaseOrders` |
| `receipts.csv` | `RCV_SHIPMENT_HEADERS` | `/fscmRestApi/resources/11.13.18.05/receivingReceiptRequests` |
| `invoices.csv` | `AP_INVOICES_ALL` | `/fscmRestApi/resources/11.13.18.05/invoices` |
| hold status | `AP_HOLDS_ALL` | (Payables subledger — no public REST; managed via `SP_EXECUTE_3WAY_MATCH`) |

**Terminology note**: This project uses exclusively **Oracle Fusion Cloud 24D/25A** terminology. Approval workflows reference **Oracle BPM Worklist (Human Workflow / AMX)** — not the legacy E-Business Suite AME engine. No EBS-specific terms are used.

### Automated Invoice Matching Flow (SQL logic)

```sql
-- SP_EXECUTE_3WAY_MATCH (excerpt)
-- Checks: PO price ± tolerance, quantity received vs. invoiced
-- Inserts into XXNS_INVOICE_HOLDS for any failing invoice
-- Updates XXNS_INVOICES.match_status to MATCHED / PRICE_HOLD / QTY_HOLD / MISSING_GR_HOLD
```

---

## Slide 5 — Results & To-Be Targets

### What the implementation is designed to achieve

**Illustrative targets** — labelled as planning assumptions, not achieved results.

```
                          AS-IS Baseline    TO-BE Target     Confidence
                          (Simulated)       (Assumption)
                          ─────────────    ─────────────     ──────────
Invoice exception rate       20.8%           ≤ 8.0%          BPI 2019 benchmarks
Straight-through rate        79.2%           ≥ 85.0%         support feasibility
PR approval turnaround       2.5 days        ≤ 2.0 days
PR → PO cycle time           4.0 days        ≤ 3.0 days
Early invoice rate            8.7%           ≤ 3.0%
Active holds value         \$299,208         ≤ \$80,000 est.
Financial reconciliation     \$0 gap         \$0 gap          Already verified ✓
```

**What was built to verify the design:**

- ✅ 5 automated pytest assertions — financial reconciliation to the cent, referential integrity, primary-key uniqueness, chronological validity, tolerance enforcement — run on every push via GitHub Actions CI
- ✅ Tolerance optimisation model — 7-policy trade-off table with economic cost quantification
- ✅ BPI 2019 real-enterprise benchmark — external validation for hold-rate baseline
- ✅ Statistical regression — directional odds ratios showing 3-way match and supplier risk as primary hold drivers
- ✅ Oracle DDL + PL/SQL + APEX specification — design artefacts mapped to Fusion Cloud objects

**Artefact map:**

```
Problem definition  →  docs/project-charter.md, docs/as-is-to-be-process.md
Solution design     →  docs/functional-design.md, oracle/
Gap analysis        →  docs/gap-analysis.md
Data evidence       →  analysis/*.py, analysis/outputs/
Testing evidence    →  tests/test_p2p_pipeline.py, testing/
Live demo           →  https://madhav70.github.io/oracle-erp-p2p-case-study/
```

---

*All figures labelled "Simulated" derive from deterministic Python code (seed = 42) and represent hypothetical scenarios, not actual business outcomes.*  
*BPI 2019 figures: Mannhardt, F. (2019). BPI Challenge 2019. 4TU.ResearchData. DOI: `10.4121/uuid:d06aff4b-79f0-45e6-8ec8-e19730c248f1`. CC BY 4.0.*
