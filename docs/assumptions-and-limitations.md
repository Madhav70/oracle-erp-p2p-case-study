# Assumptions, Technical Boundaries & Project Limitations

**Project**: Oracle ERP Procure-to-Pay Implementation Case Study  
**Entity**: Northstar Manufacturing Ltd. (Fictional Organization)  
**Author**: Lead Systems Architect & Functional Consultant

---

## 1. Academic & Independent Portfolio Disclosure

> **IMPORTANT NOTICE**:  
> This project is an independent simulated case study developed strictly for academic, educational, and professional portfolio demonstration.
> - **Fictional Enterprise**: "Northstar Manufacturing Ltd." is a fictional company. All employees, vendors, transactional volumes, purchase orders, receipts, and invoices are synthetic artifacts generated through deterministic computer code.
> - **No Actual Oracle Deployment**: This project does not claim that an actual Oracle ERP implementation took place, that a real enterprise deployed the software, or that official Oracle certification was obtained.
> - **Demonstrated Competencies**: The portfolio demonstrates mastery of enterprise business analysis, process re-engineering (As-Is to To-Be), functional requirements documentation, PMBOK project-management governance, quality assurance frameworks, and data analytics.

---

## 2. Distinction: Simulated Design vs. Live Oracle Cloud Capabilities

To preserve strict truthfulness and integrity, the following matrix distinguishes simulated design artifacts from capabilities that require licensed, live Oracle Cloud ERP instances:

| Functional Capability | Portfolio Simulated Deliverable | Requirement for Live Oracle Cloud ERP Deployment |
| :--- | :--- | :--- |
| **Self-Service Requisitioning** | Requirements matrix, functional design, simulated data, UI workflow representation. | Active subscription to Oracle Fusion Cloud Procurement (Self-Service Requisitioning module); configured functional setup manager (FSM) business unit profiles. |
| **Approval Hierarchy (DoA)** | Logic rules, supervisory tiers ($<\$5\text{k}, \$5\text{k}-\$25\text{k}, >\$25\text{k}$), negative test scenarios. | Oracle BPM Worklist / Approvals Management Engine (AME); live integration with corporate Active Directory / HR hierarchy. |
| **Automated 3-Way Matching** | Python validation engine, tolerance rules ($1.5\% / \$50$), synthetic invoice data. | Oracle Fusion Cloud Payables (AP) matching engine; configured invoice tolerance groups and line-level distribution rules. |
| **Supplier Portal & Ingestion** | Vendor master data dictionary, standardized CSV datasets, supplier communication plan. | Oracle Supplier Portal Cloud; secure external reverse-proxy or Single Sign-On (SSO) gateway. |
| **Electronic Payments** | Synthetic payment file reference generation (EFT/ACH), remittance advice layouts. | Oracle Payments engine; secure host-to-host SFTP / AS2 connectivity with commercial banking partner; ISO 20022 payment templates. |
| **Operational Reporting** | Python pandas analytics suite, executive JSON metrics, responsive interactive HTML dashboard. | Oracle Transactional Business Intelligence (OTBI), Oracle BI Publisher, or Oracle Fusion Data Intelligence (FDI). |
| **Audit Trails & Security** | RBAC matrix, SoD role definitions, immutable timestamp log design. | Oracle Cloud Infrastructure (OCI) audit service; Oracle Identity & Access Management (IAM) role definitions. |

---

## 3. Data Assumptions & Mathematical Definitions

All analytical figures displayed in this project are derived deterministically from the sample datasets generated via `analysis/generate_sample_data.py` (fixed random seed = 42).

### Metric Formulas:

1. **Invoice Discrepancy Rate (Transaction Count)**:
   $$\text{Discrepancy Rate}_{\text{count}} = \left( \frac{\text{Total Invoices with Exception Holds}}{\text{Total Invoices Processed}} \right) \times 100$$
   *Current Value*: $51 / 208 = 24.52\%$

2. **Value-Weighted Invoice Discrepancy Rate**:
   $$\text{Discrepancy Rate}_{\text{value}} = \left( \frac{\sum \text{Invoice Amount of Invoices on Hold}}{\sum \text{Total Invoiced Amount}} \right) \times 100$$
   *Current Value*: $\$752,382.90 / \$2,810,206.58 = 26.77\%$

3. **Requisition Approval Turnaround Time**:
   $$\text{Approval Turnaround} = \frac{1}{N} \sum_{i=1}^N \left( \text{Approval Date}_i - \text{Requisition Date}_i \right)$$
   *Current Value*: $2.48 \text{ days (Mean)}, 2.00 \text{ days (Median)}$

4. **Total Procurement Cycle Time (PR to PO)**:
   $$\text{Procurement Cycle} = \frac{1}{M} \sum_{j=1}^M \left( \text{PO Issuance Date}_j - \text{Requisition Date}_j \right)$$
   *Current Value*: $3.88 \text{ days (Mean)}, 4.00 \text{ days (Median)}$

5. **Invoice-to-Payment Turnaround**:
   $$\text{Payment Turnaround} = \frac{1}{K} \sum_{k=1}^K \left( \text{Disbursement Date}_k - \text{Invoice Date}_k \right)$$
   *Current Value*: $30.82 \text{ days (Mean)}, 30.00 \text{ days (Median)}$

---

## 4. Technical Environment Boundaries

1. **Local File System Execution**: The analysis scripts and interactive website operate locally using vanilla HTML5, CSS3, JavaScript (ES6), Python 3, pandas, and matplotlib. No external cloud database or proprietary software is required to run the demonstrator.
2. **Deterministic Reproducibility**: Re-running `python analysis/generate_sample_data.py` followed by `python analysis/p2p_analysis.py` will regenerate identical datasets, JSON metrics, and visualization charts.
3. **No Live Bank Clearing**: Financial payment records simulate Automated Clearing House (ACH) and Electronic Funds Transfer (EFT) trace numbers without interacting with live banking networks.
