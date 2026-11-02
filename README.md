# Oracle ERP Procure-to-Pay (P2P) Implementation Case Study

**Fictional Enterprise**: Northstar Manufacturing Ltd.  
**Role Demonstrated**: Senior Oracle ERP Functional Consultant, Business Analyst, QA/UAT Specialist, Technical Writer & Project Manager  
**Project Methodology**: Hybrid Agile-Waterfall ERP Implementation (14-Week Illustrative Horizon)  
**Target Architecture**: Conceptual Alignment with Oracle Fusion Cloud Procurement & Financials (Payables)

---

## Academic & Independent Portfolio Disclaimer

> **IMPORTANT NOTICE**:  
> This project is an independent simulated case study developed strictly for academic, educational, and professional portfolio demonstration.
> - **Simulated Enterprise**: "Northstar Manufacturing Ltd." is an entirely fictional mid-sized manufacturing organization. All employee names, commercial vendors, transaction volumes, purchase orders, dock receipts, and invoice records are synthetic artifacts generated through deterministic Python code.
> - **No Actual Oracle Deployment**: This case study does not claim that an actual Oracle ERP implementation took place, that a real enterprise deployed the software, or that official Oracle certification was obtained.
> - **Competency Focus**: This project demonstrates mastery of enterprise business analysis, requirements engineering (BRD), business process re-engineering (As-Is to To-Be), PMBOK project-management governance, quality assurance frameworks, and data analytics. It does not imply hands-on production administration of a live, licensed Oracle Cloud tenant.

---

## 1. Project Overview & Business Problem

Northstar Manufacturing Ltd., a discrete manufacturer of precision industrial components, suffered from systemic operational friction across its procurement and accounts payable functions:
- **Inconsistent Requisition Channels**: Plant workers submitted requests via paper forms, unrecorded emails, and verbal phone orders, creating rampant maverick spend.
- **Approval Bottlenecks**: Absence of automated Delegation of Authority (DoA) approval hierarchies resulted in an average managerial approval latency of **2.48 days** and unauthorized commitments.
- **Dock Receiving Deficits**: Physical delivery packing slips were filed on paper or lost during shift handovers, generating artificial "Missing Goods Receipt" holds when supplier invoices arrived.
- **High Invoice Discrepancy Rate**: Over **24.52%** of incoming supplier invoices encountered matching holds (Price variances, Missing receipts, Quantity mismatches), requiring tedious clerical investigations and causing delayed payments.
- **Lack of Spend Visibility**: Management relied on labor-intensive, month-end spreadsheet consolidations with zero real-time visibility into committed PO spend or supplier performance.

The proposed solution establishes a standardized, automated Procure-to-Pay process aligned conceptually with Oracle Fusion Cloud Procurement and Financials.

---

## 2. Business Objectives & Simulated Baseline Metrics

| Objective ID | Strategic Objective | Baseline (Simulated) | Target State (Assumption) | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **OBJ-01** | Standardize Requisition & Approval Routing | 2.48 days latency; loose emails | $\le 1.0$ business day via automated DoA | BPM approval workflow logs |
| **OBJ-02** | Compress Total Procurement Cycle Time | 3.88 days from initial PR to PO | $\le 2.0$ business days for catalog orders | Purchasing workbench timestamps |
| **OBJ-03** | Automate Invoice Matching & Reduce Holds | 24.52% invoice exception holds | $\le 8.0\%$ exception rate via 3-Way match | Accounts Payable hold report |
| **OBJ-04** | Eliminate Maverick & Unmatched Invoices | Frequent unreferenced invoices | $100\%$ invoices linked to approved PO | Payables subledger reconciliation |
| **OBJ-05** | Real-Time Spend Visibility & Analytics | Monthly manual Excel reports | Real-time interactive OTBI dashboard | Executive dashboard sign-off |
| **OBJ-06** | Change Readiness & Role Adoption | Minimal structured documentation | $\ge 90\%$ verified competency score | LMS completion & UAT sign-off |

---

## 3. Scope & Boundary Conditions

### In-Scope Functional Processes (Phase 1)
1. **Supplier Master Standardization**: Centralized capture of 25 active vendors, standardized payment terms (`Net 30`, `Net 45`, `Net 60`, `2/10 Net 30`), and commodity classifications.
2. **Self-Service Requisitioning**: Online catalog templates and non-catalog expense forms with mandatory cost-center validation.
3. **Automated Approval Workflows**: Three-tier Delegation of Authority routing ($<\$5\text{k}$ Dept Mgr, $\$5\text{k}-\$25\text{k}$ Director, $>\$25\text{k}$ VP/CFO).
4. **Purchase Order Execution**: Automated conversion of approved PRs into POs against Blanket Purchase Agreements (BPAs).
5. **Dock Receiving Intake**: Warehouse dock logging of full receipts, partial deliveries, and damaged shipment RMA returns.
6. **Automated Invoice Matching**: 3-Way matching (goods) and 2-Way matching (services) with a configured $1.5\% / \$50$ tolerance group.
7. **Exception Routing & Hold Escalation**: Structured hold worklists with automated 7-day managerial escalation.
8. **Disbursements & Cash Management**: Automated Payment Process Request (PPR) runs with dual authorization.

### Out-of-Scope Exclusions (Deferred to Phase 2 Roadmap)
- Multi-vendor competitive RFx bidding auctions (Sourcing Cloud).
- Contract lifecycle authoring with automated clause libraries.
- Physical optical character recognition (OCR) hardware scanning.
- Direct host-to-host banking socket integrations (mock ACH simulated).

---

## 4. Repository Structure

```
oracle-erp-p2p-case-study/
├── index.html                               # Interactive Executive Portfolio Website
├── README.md                                # Comprehensive Project Documentation & Guide
├── LICENSE                                  # MIT Open-Source License
├── .gitignore                               # Git Ignore Configuration
├── docs/                                    # 14 Comprehensive Markdown Deliverables
│   ├── project-charter.md                   # Charter, objectives, governance, budget
│   ├── business-requirements.md             # 18 traceable requirements with MoSCoW priorities
│   ├── as-is-to-be-process.md               # 10-step To-Be workflow & exception matrix
│   ├── functional-design.md                 # Future-state design, tolerances, security profiles
│   ├── gap-analysis.md                      # 12 detailed operational & technical gaps
│   ├── stakeholder-management.md            # Stakeholder matrix & communication plan
│   ├── project-plan.md                      # 14-week milestone schedule & workstream tasks
│   ├── risk-register.md                     # 13 assessed risks with 1-25 scoring model
│   ├── change-management.md                 # Prosci ADKAR change plan & 5-course curriculum
│   ├── testing-and-uat.md                   # Quality assurance strategy & RTM
│   ├── implementation-and-cutover.md        # 48-hour weekend runbook & rollback plan
│   ├── support-and-governance.md            # L1/L2/L3 support model & P2P Council charter
│   ├── assumptions-and-limitations.md       # Full disclosure of technical boundaries
│   └── project-retrospective.md             # Post-mortem, lessons learned, Phase 2 roadmap
├── data/                                    # Deterministic Synthetic Datasets
│   ├── suppliers.csv                        # 25 active commercial vendors
│   ├── requisitions.csv                     # 250 procurement requests
│   ├── purchase_orders.csv                  # 223 purchase orders issued
│   ├── receipts.csv                         # 105 dock receiving slips
│   ├── invoices.csv                         # 208 invoice vouchers with matching statuses
│   └── data_dictionary.md                   # Complete schema, datatypes, and referential rules
├── analysis/                                # Python Analytics & Visualization Suite
│   ├── generate_sample_data.py              # Synthetic data generator (seed = 42)
│   ├── p2p_analysis.py                      # Data audit, cycle times, and KPI calculator
│   ├── requirements.txt                     # pandas, numpy, matplotlib dependencies
│   └── outputs/                             # Analytical CSVs, JSON, and Chart Outputs
│       ├── README.md                        # Documentation of analytical outputs
│       ├── p2p_summary_metrics.json         # Executive KPI summary JSON
│       ├── spend_by_supplier.csv            # Vendor-level spend and hold rates
│       ├── spend_by_category.csv            # Commodity spend breakdown
│       ├── exception_analysis.csv           # Detailed invoice hold classification
│       ├── cycle_times.csv                  # Stage-by-stage cycle times vs SLAs
│       ├── chart_spend_by_category.png      # Bar chart: Spend by Category
│       ├── chart_monthly_spend.png          # Trend chart: Monthly PO Commitment Volume
│       ├── chart_exception_breakdown.png    # Donut chart: Invoice Match & Hold Distribution
│       └── chart_cycle_times.png            # Bar chart: Current Cycle Times vs ERP SLAs
├── testing/                                 # Quality Assurance & Testing Materials
│   ├── functional-test-cases.csv            # 22 detailed functional test cases
│   ├── uat-test-cases.csv                   # 12 business UAT scenarios
│   ├── defect-log.csv                       # 8 illustrative defects across severities
│   └── test-summary.md                      # QA sign-off memo & RTM verification
├── project-management/                      # PMO Deliverables
│   ├── work-breakdown-structure.md          # 5-level WBS across 8 workstreams
│   ├── milestone-plan.csv                   # 10 stage-gate milestones with exit criteria
│   ├── raci-matrix.csv                      # RACI matrix across 18 project activities
│   ├── communications-plan.md               # Multi-tier stakeholder communication cadence
│   └── change-log.csv                       # Scope & schedule change control log
├── diagrams/                                # Mermaid Process & Architecture Flowcharts
│   ├── as-is-process.mmd                    # Current fragmented procurement workflow
│   ├── to-be-process.mmd                    # Standardized 10-step ERP lifecycle
│   └── system-context.mmd                   # System context & module boundary diagram
└── assets/                                  # Website Presentation Layer
    ├── css/
    │   └── styles.css                       # Consulting-grade responsive styling
    ├── js/
    │   └── app.js                           # Interactive filtering, tabs & search engine
    └── images/                              # High-resolution visualization charts
```

---

## 5. Technology Stack

- **Documentation & Methodologies**: Markdown (GFM), Mermaid.js process diagrams, PMBOK project-management standards, Prosci ADKAR change framework.
- **Data Engineering & Analytics**: Python 3.14, pandas, numpy, matplotlib.
- **Frontend Presentation Layer**: HTML5 (semantic, accessible), CSS3 (custom consulting theme, zero heavyweight frameworks), vanilla JavaScript (ES6+ modular DOM engine).
- **Version Control & Hosting**: Git, GitHub, GitHub Pages compatibility.

---

## 6. Setup & Execution Instructions

### Prerequisites
- Python 3.8+ installed.
- Modern web browser (Chrome, Edge, Firefox, Safari).

### Step 1: Clone or Navigate to the Repository
```bash
git clone https://github.com/Madhav70/oracle-erp-p2p-case-study.git
cd oracle-erp-p2p-case-study
```

### Step 2: Install Python Analytics Dependencies
```bash
pip install -r analysis/requirements.txt
```

### Step 3: Regenerate Synthetic Datasets (Deterministic Seed = 42)
```bash
python analysis/generate_sample_data.py
```
*Output*: Generates clean, referentially sound CSV files in `data/`.

### Step 4: Run Data Audit & Analytics Engine
```bash
python analysis/p2p_analysis.py
```
*Output*:
- Validates 100% referential integrity and primary key uniqueness.
- Generates `analysis/outputs/p2p_summary_metrics.json`.
- Produces analytical CSV summaries in `analysis/outputs/`.
- Generates 4 high-resolution charts in `analysis/outputs/` and syncs them to `assets/images/`.

### Step 5: View the Interactive Website
Simply open `index.html` in your web browser:
- **Windows**: Double-click `index.html` or run `start index.html` in PowerShell.
- **macOS**: `open index.html`
- **Linux**: `xdg-open index.html`

No local web server, database, or API keys are required.

---

## 7. Key Analytical Metrics & Mathematical Formulations

All analytical figures displayed on the dashboard match `analysis/outputs/p2p_summary_metrics.json`:

1. **Total Committed Purchase Order Spend**: **\$2,964,919.38** across 223 issued POs.
2. **Total Invoiced Volume**: **\$2,810,206.58** across 208 vouchers (\$2,297,431.60 disbursed; \$720,146.31 on hold).
3. **Invoice Discrepancy Rate (Transaction Count)**:
   $$\text{Discrepancy Rate}_{\text{count}} = \frac{51 \text{ Invoices on Hold}}{208 \text{ Total Invoices}} \times 100 = \mathbf{24.52\%}$$
   - *Hold: Missing Goods Receipt*: 21 vouchers (\$285,947.33)
   - *Hold: Price Variance*: 19 vouchers (\$305,535.27)
   - *Hold: Quantity Variance*: 11 vouchers (\$128,663.71)
4. **Requisition Approval Turnaround**: **2.48 days** (Mean) / **3.00 days** (Median). Target SLA: $\le 2.0\text{d}$.
5. **Requisition-to-PO Procurement Cycle Time**: **3.88 days** (Mean) / **4.00 days** (Median). Target SLA: $\le 3.0\text{d}$.
6. **Invoice-to-Payment Cycle Time**: **30.89 days** (Mean) / **30.00 days** (Median).

---

## 8. Quality Assurance & Testing Governance

- **Functional Test Cases (`testing/functional-test-cases.csv`)**: 22 traceable test cases covering normal and negative paths (AME routing boundaries, tolerance group calculations, inactive vendor blocking, self-approval prevention).
- **User Acceptance Testing (`testing/uat-test-cases.csv`)**: 12 comprehensive business scenarios executed with operational personas (Plant Requisitioner, Maintenance Lead, Dock Clerk, Buyer, AP Specialist, Controller).
- **Defect Log (`testing/defect-log.csv`)**: 8 sample defects across severities (Sev 1 to Sev 4) with documented root causes and permanent remediations. 100% closed prior to UAT sign-off.
- **Traceability**: 100% of the 18 business requirements are mapped to verified test cases.

---

## 9. GitHub Pages Deployment Instructions

To view this portfolio project live via GitHub Pages:
1. Ensure this repository is pushed to your GitHub account (`main` branch).
2. On GitHub, navigate to **Settings** &rarr; **Pages** (under "Code and automation").
3. Under **Build and deployment** &rarr; **Source**, select **Deploy from a branch**.
4. Under **Branch**, select `main` and root `/(root)`, then click **Save**.
5. Within 1–2 minutes, GitHub Pages will deploy the project at:
   `https://<your-username>.github.io/oracle-erp-p2p-case-study/`

---

## 10. Candidate Skills Demonstrated

This case study is engineered to provide concrete evidence of competencies for entry-level and junior roles in:
- **ERP Functional Consulting & Technology Consulting**: Understanding of P2P modules, 3-Way matching logic, tolerance groups, chart of accounts flexfields, and subledger accounting entries.
- **Business Analysis & Requirements Engineering**: As-Is to To-Be process re-engineering, MoSCoW-prioritized BRD authoring, gap analysis, and requirements traceability matrices (RTM).
- **PMO & Project Management**: Work Breakdown Structure (WBS), stage-gate milestone planning, RACI matrix definition, quantitative risk register management, change control logs, and 48-hour cutover runbooks.
- **Organizational Change Management (OCM)**: Prosci ADKAR change plan, role impact assessment, multi-tier training curriculum design, and adoption measurement.
- **Data Analytics & Verification**: Python, pandas, deterministic dataset generation, automated referential integrity testing, and data visualization.

---

## License

This project is licensed under the [MIT License](LICENSE).
