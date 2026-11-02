# Project Charter: Procure-to-Pay (P2P) Transformation Simulation

> **Academic & Portfolio Disclosure**:  
> This project charter represents an independent, simulated implementation case study for a fictional enterprise, **Northstar Manufacturing Ltd.**. It has been developed strictly for academic, portfolio, and professional demonstration purposes in technology consulting, business analysis, and IT project management. No actual Oracle ERP implementation took place, no real corporate data was utilized, and this document does not represent an endorsement, official recommendation, or certified deployment by Oracle Corporation.

---

## 1. Executive Summary

Northstar Manufacturing Ltd., a mid-sized discrete manufacturing company specializing in precision industrial components, seeks to modernize its fragmented procurement and accounts payable operations. The organization currently relies on disconnected legacy spreadsheets, paper purchase orders, decentralized email approvals, and manual invoice verification. These fragmented practices result in high invoice discrepancy rates (~24.5%), prolonged procurement cycle times (~3.9 days from requisition to PO issuance), lack of spend visibility, and late-payment friction with key strategic suppliers.

This project outlines an illustrative, 14-week simulated implementation plan to transition Northstar Manufacturing Ltd. to a standardized Procure-to-Pay (P2P) process conceptually aligned with Oracle Fusion Cloud Procurement and Financials (Payables). By instituting automated Delegation of Authority (DoA) approval hierarchies, automated 2-Way and 3-Way invoice matching with configured tolerance thresholds, and centralized reporting dashboards, the proposed future-state design targets operational excellence, tight financial controls, and scalable supplier relationships.

---

## 2. Business Problem Statement

Operational audits and simulated baseline data at Northstar Manufacturing Ltd. have exposed systemic vulnerabilities across the procurement lifecycle:
- **Inconsistent Requisition Channels**: Requisitions are submitted via paper forms, informal emails, or unrecorded verbal commitments, creating rampant "maverick spend" and unbudgeted obligations.
- **Unclear & Decentralized Approvals**: Absence of automated Delegation of Authority rules leads to managerial bottlenecks, orphaned approval requests, and occasional unauthorized commitments exceeding sign-off thresholds.
- **Tracking & Receiving Deficiencies**: Physical goods receipts recorded in dock paper logs are frequently mislaid or entered after vendor invoices arrive, generating artificial "Missing Goods Receipt" holds.
- **Invoice Discrepancies & Stalled Cash Flow**: Over 24% of received invoices encounter matching exceptions—primarily due to uncoordinated pricing amendments or dock shortages—requiring labor-intensive manual investigations by Accounts Payable clerks.
- **Deficient Reporting & Spend Analytics**: Executive management lacks consolidated visibility into supplier performance, category spend concentrations, pending commitments, and cash-outflow liabilities.

---

## 3. Project Objectives (Simulated Targets)

The project establishes the following illustrative, measurable targets for the future-state operating model:

| Objective ID | Strategic Objective | Baseline Metric (Simulated) | Target State (Illustrative Assumption) | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **OBJ-01** | Standardize Requisition & Approval Routing | 2.5 days avg approval; ad-hoc emails | $\le 1.0$ business day via automated DoA workflows | Workflow audit logs in ERP |
| **OBJ-02** | Compress Total Procurement Cycle Time | 3.88 days from PR creation to PO dispatch | $\le 2.0$ business days for standard catalogue items | Purchase Order timestamp metrics |
| **OBJ-03** | Automate Invoice Matching & Reduce Exception Rate | 24.52% invoice exception holds | $\le 8.0\%$ exceptions through tolerance rules & 3-Way match | Accounts Payable hold report |
| **OBJ-04** | Eliminate Maverick & Unmatched Invoices | Frequent unreferenced invoices | $100\%$ invoices matched to approved PO or contract | AP subledger reconciliation |
| **OBJ-05** | Real-Time Spend Visibility & Analytics | Monthly manual Excel consolidations | Real-time interactive OTBI / Executive dashboard | Dashboard operational sign-off |
| **OBJ-06** | Change Readiness & Role Adoption | Minimal structured training | $\ge 90\%$ verified end-user competency score | LMS completion & UAT sign-off |

---

## 4. Project Scope

### In-Scope Functional Processes
1. **Supplier Master Management**: Standardization of supplier profiles, payment terms (`Net 30`, `Net 45`, `Net 60`, `2/10 Net 30`), and commodity classifications.
2. **Purchase Requisitions**: Implementation of Self-Service Requisitions with catalog and non-catalog item templates and mandatory accounting distribution.
3. **Approval Workflows**: Multi-tier approval routing rules based on department and spend thresholds ($<\$5\text{k}$, $\$5\text{k}$–$\$25\text{k}$, $>\$25\text{k}$).
4. **Purchase Order Execution**: Automatic conversion of approved PRs into POs, electronic PO dispatch, and master agreement tracking.
5. **Receiving & Dock Intake**: Standardized dock receipt logging, inspection status capture, and partial shipment handling.
6. **Accounts Payable & Matching**: Configuration of 2-Way (services) and 3-Way (goods) matching rules, with a 1.5% / $50 price variance tolerance threshold.
7. **Hold Resolution & Exception Management**: Workflow notifications for price variance, missing goods receipts, and quantity discrepancies.
8. **Disbursements & Cash Management**: Automated payment schedule generation and electronic remittance batch processing.
9. **Reporting & Dashboards**: Pre-packaged operational reporting for buyer performance, supplier discrepancy rates, and AP aging.

### Out-of-Scope Functional Processes
1. Complex multi-stage strategic sourcing events and supplier bidding auctions (RFx module).
2. Advanced supplier qualification lifecycle management (SQM portal).
3. Contract authoring with clause library and automated digital signature integrations.
4. Global intercompany transfer pricing across multiple multinational tax jurisdictions.
5. Automated optical character recognition (OCR) scanning hardware deployment (conceptual intake assumed).
6. Live direct host-to-host bank connectivity (mock EDI/ACH payment output simulated).

---

## 5. Implementation Methodology & Timeline Assumptions

The project adopts a structured 14-week hybrid agile-waterfall methodology organized across five foundational stages:

```
[Discovery & Architecture] -> [Design & Config Prep] -> [Testing & Validation] -> [Training & Cutover] -> [Hypercare & Transition]
      Weeks 1 - 3                 Weeks 4 - 7                 Weeks 8 - 11               Weeks 12 - 13              Week 14+
```

- **Phase 1: Project Initiation & Discovery (Weeks 1–3)**: Finalize Charter, validate As-Is pain points, document Business Requirements, and conduct Gap Analysis.
- **Phase 2: Solution Design & Prototype Preparation (Weeks 4–7)**: Author Functional Design Documents (FDD), define matching tolerances, configure prototype workflows, and draft conversion specifications.
- **Phase 3: Testing & Quality Assurance (Weeks 8–11)**: Execute Functional Unit Testing (FUT), System Integration Testing (SIT), and User Acceptance Testing (UAT).
- **Phase 4: End-User Enablement & Cutover (Weeks 12–13)**: Conduct role-based training, execute data migration runbooks, and perform production cutover during scheduled blackout.
- **Phase 5: Go-Live & Hypercare Support (Weeks 14+)**: Operational command center, SLA monitoring, defect triage, and transition to ongoing P2P governance.

---

## 6. Project Stakeholders & Governance Structure

```
                      +---------------------------------------+
                      |       Project Steering Committee       |
                      |   CFO (Executive Sponsor), COO, CIO   |
                      +---------------------------------------+
                                          |
                      +---------------------------------------+
                      |         PMO & Project Manager         |
                      |  Senior PM / P2P Functional Lead      |
                      +---------------------------------------+
                                          |
         +--------------------------------+--------------------------------+
         |                                |                                |
+------------------+             +------------------+             +------------------+
| Procurement Lead |             |   Finance Lead   |             | Technical & QA   |
| Purchasing Team  |             |  AP Specialists  |             | IT & Data Leads  |
+------------------+             +------------------+             +------------------+
```

- **Executive Sponsor (CFO)**: Ultimate financial accountability, governance escalation, and scope approval.
- **Project Manager / PMO Lead**: Day-to-day workstream coordination, risk tracking, milestone schedule management, and steering committee reporting.
- **P2P Functional Consultant**: Lead business process design, workflow definition, tolerance rule design, and configuration specifications.
- **Procurement Workstream Lead**: Procurement operational policies, catalogue hierarchies, and buyer workflow adoption.
- **Finance & AP Workstream Lead**: Matching validation rules, chart of accounts integration, and payment authorization sign-offs.
- **Change Management & QA Lead**: Test execution oversight, defect governance, end-user curriculum design, and adoption measurement.

---

## 7. Illustrative Budget Assumptions (Planning Estimate)

> *Note: Figures below are illustrative scenario planning models and do not represent actual vendor quotations or contractual commitments.*

| Cost Category | Scope Description | Illustrative Allocation ($ USD) |
| :--- | :--- | :--- |
| **External Advisory & Consulting** | Lead Functional Consultant, Solution Architect, PMO Support (14 wks) | $165,000 |
| **Internal Resource Backfill** | Temporary operational backfill for AP & Purchasing SME leads | $45,000 |
| **Training & Change Materials** | Interactive training modules, job aids, and simulation sandbox environments | $22,000 |
| **Data Migration & Cleansing** | Script development, supplier data enrichment, and legacy PO reconciliations | $18,000 |
| **Contingency Reserve (15%)** | Buffer for scope variations and hypercare stabilization extensions | $37,500 |
| **Total Estimated Investment** | **Illustrative Project Envelope** | **$287,500** |

---

## 8. Assumptions, Constraints & Dependencies

### Key Assumptions
1. Northstar business leadership will make subject matter experts (SMEs) available for at least 30% of their operational time during testing and design phases.
2. Legacy supplier and open purchase order data will be cleansed and standardized prior to Week 10 migration mock runs.
3. Matching tolerance policies approved by the Steering Committee will remain fixed throughout testing.

### Key Constraints
1. The project must complete cutover within a strict 48-hour weekend window to avoid disrupting physical plant operations.
2. No live interfaces to external customs or tax portals will be built in Phase 1.

### Key Dependencies
1. Timely steering committee sign-off on the Delegation of Authority matrix by end of Week 3.
2. Access to staging/test environments provisioned and available by Week 4.

---

## 9. Acceptance Criteria & Definition of Done

The simulated implementation shall be considered ready for operational go-live upon meeting the following gates:
1. **100% Traceability**: All in-scope business requirements mapped to approved functional designs and validated test cases.
2. **UAT Sign-off**: Completion of all business-critical UAT test cases with zero Sev-1 or Sev-2 defects open.
3. **Data Verification**: Successful execution of Mock Cutover 2 with 100% supplier master and open PO balance reconciliation.
4. **User Readiness**: $\ge 90\%$ of designated requisitioners, buyers, dock clerks, and AP personnel completing mandatory training.
5. **Governance Sign-off**: Formal unanimous approval from the Executive Steering Committee.
