# Testing Strategy & User Acceptance Testing (UAT) Plan

**Project**: Procure-to-Pay (P2P) Implementation Simulation  
**Organization**: Northstar Manufacturing Ltd. (Fictional Enterprise)  
**Author**: QA & Test Management Lead  
**Document Reference**: QA-P2P-TEST-001

> **Simulated Project Disclaimer**:  
> This testing governance document is an academic and portfolio deliverable demonstrating enterprise QA methodologies for ERP programs. Because this is an independent case study without an active Oracle Cloud tenant, test cases in the test catalogue are maintained with truthful execution statuses ("Simulated - Not Executed in Live Cloud Tenant" or "Verified in Synthetic Engine"). No claim of live production Oracle execution is made.

---

## 1. Quality Assurance Strategy & Test Levels

The testing framework organizes verification across four distinct, sequential stages:

```
+---------------------------------------------------------------------------------------------------------+
|                                        ENTERPRISE TESTING PYRAMID                                       |
+---------------------------------------------------------------------------------------------------------+
|  Test Level                | Scope & Responsibility                     | Primary Focus                 |
+----------------------------+--------------------------------------------+-------------------------------+
|  1. Functional Unit (FUT)  | Functional Consultants & Developers        | Discrete field validation,    |
|                            |                                            | form behavior, simple rules   |
+----------------------------+--------------------------------------------+-------------------------------+
|  2. System Integration     | QA Team & Integration Leads                | End-to-end data flows across  |
|     (SIT)                  |                                            | modules & synthetic bank files|
+----------------------------+--------------------------------------------+-------------------------------+
|  3. Regression Testing     | QA Automation & Test Leads                 | Re-verifying previously passed|
|                            |                                            | flows after configuration fix |
+----------------------------+--------------------------------------------+-------------------------------+
|  4. User Acceptance (UAT)  | Business SMEs (Requisitioners, Buyers,     | Real-world operational        |
|                            | Dock Clerks, AP Specialists, Controllers)  | scenarios & business sign-off |
+---------------------------------------------------------------------------------------------------------+
```

### Definitions:
- **Functional Unit Testing (FUT)**: Verifies that individual system components (e.g. mandatory field validation, approval thresholds) function according to the Functional Design Document.
- **System Integration Testing (SIT)**: Verifies end-to-end transactions passing across module boundaries (e.g. from a Requisition in Self-Service Procurement to a PO in Purchasing, through Dock Receiving, automated Payables matching, and payment batch generation).
- **Regression Testing**: Ensures that bug fixes or configuration changes do not inadvertently degrade previously validated functionality.
- **User Acceptance Testing (UAT)**: Business-driven validation where operational process owners verify that the solution supports daily business operations in realistic business scenarios.

---

## 2. Test Phase Entry and Exit Criteria

```
+---------------------------------------------------------------------------------------------------------+
| Phase        | Entry Criteria                                    | Exit Criteria (Gate Requirement)     |
+--------------+---------------------------------------------------+--------------------------------------+
| FUT          | - Baseline FDD signed off                         | - 100% test cases attempted          |
|              | - Staging sandbox provisioned & seeded            | - Zero open Sev 1 defects            |
+--------------+---------------------------------------------------+--------------------------------------+
| SIT          | - Successful completion of FUT                    | - 100% end-to-end scenarios passed   |
|              | - Cross-module test scripts baselined             | - Zero open Sev 1 or Sev 2 defects   |
+--------------+---------------------------------------------------+--------------------------------------+
| UAT          | - SIT exit criteria achieved                      | - 100% business UAT scenarios run    |
|              | - Business SMEs trained in TRN-101 to TRN-501     | - 0 Sev 1, 0 Sev 2, <= 2 Sev 3 bugs  |
|              | - Cleansed migration mock data loaded             | - Formal written business sign-off   |
+---------------------------------------------------------------------------------------------------------+
```

---

## 3. Defect Classification & Severity Scale

Defects identified during testing are logged, tracked, and prioritized using a four-tier severity classification:

| Severity Level | Name | Definition & Operational Impact | SLA for Initial Response | Target Resolution Window | Release Blocking? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Sev 1** | **Critical / Blocker** | System crash, data corruption, total transaction blockage with no workaround (e.g. PR approval completely fails to route; matching engine crashes on receipt). | Within 1 Hour | $\le 8$ Hours | **Yes** (Halts Testing Gate) |
| **Sev 2** | **Major** | Severe impairment of a core business process without an acceptable operational workaround (e.g. price tolerance holds not releasing after manual supervisor override). | Within 4 Hours | $\le 24$ Hours | **Yes** (Blocks UAT Exit) |
| **Sev 3** | **Moderate** | Functional defect that affects non-critical features or has an acceptable manual workaround (e.g. notification email formatting error; dock receipt search slow). | Within 8 Hours | $\le 72$ Hours | **No** (Conditional upon PMO approval) |
| **Sev 4** | **Minor / Cosmetic** | Aesthetic flaws, minor typos, UI alignment issues that do not impact processing integrity (e.g. column header misspelling on executive report). | Within 24 Hours | Scheduled for Post-Launch Sprint | **No** |

---

## 4. Test Data Strategy

Testing requires authentic, internally consistent test data that mirrors production manufacturing volumes without exposing confidential personal information:
1. **Master Data Seeding**: Pre-load 25 synthetic suppliers with validated payment terms, tax identifiers, and commodity classifications.
2. **Transactional Scenarios**: Seed realistic transactions across all 6 spend categories, including edge cases:
   - Partial delivery receipts (e.g., 80% delivered, 20% backordered).
   - Price discrepancies ($+8\%$ overage triggering tolerance hold).
   - Missing dock receipts (invoices arriving ahead of physical goods).
   - Inactive vendor rejection.
3. **Reproducibility**: All synthetic data sets generated via deterministic Python scripts with fixed seed (`random.seed(42)`).

---

## 5. Requirements Traceability Matrix (RTM) Summary

The RTM ensures that every business requirement specified in the BRD is validated by at least one dedicated test case:

| Requirement ID | Requirement Scope | Priority | Assigned Test Case IDs | Test Type |
| :--- | :--- | :--- | :--- | :--- |
| `BR-01` | Supplier Master Validation | Must Have | `TC-FUNC-01` | Functional / Data |
| `BR-02` | Self-Service Requisition Entry | Must Have | `TC-FUNC-02` | Functional / UI |
| `BR-03` | Multi-Tier Approval Routing ($<\$5\text{k}, \$5\text{k}-\$25\text{k}, >\$25\text{k}$) | Must Have | `TC-FUNC-03`, `TC-FUNC-04` | Workflow / Integration |
| `BR-04` | Requisition Rejection & Justification | Should Have | `TC-FUNC-05` | Workflow / Negative |
| `BR-05` | Automated Purchase Order Creation | Must Have | `TC-FUNC-06` | Integration / Document Gen |
| `BR-06` | Dock Goods Receipt Intake | Must Have | `TC-FUNC-07` | Functional / Inventory |
| `BR-07` | Inspection & Partial Delivery Logging | Should Have | `TC-FUNC-08` | Functional / Negative |
| `BR-08` | Invoice Capture & Duplicate Validation | Must Have | `TC-FUNC-09` | Functional / Negative |
| `BR-09` | Automated 3-Way Matching Engine | Must Have | `TC-FUNC-10` | Core Engine / SIT |
| `BR-10` | 2-Way Service Matching Protocol | Must Have | `TC-FUNC-11` | Core Engine / SIT |
| `BR-11` | Invoice Matching Tolerance ($1.5\% / \$50$) | Should Have | `TC-FUNC-12` | Engine / Boundary |
| `BR-12` | Hold Management & Exception Routing | Must Have | `TC-FUNC-13`, `TC-FUNC-14` | Workflow / Exceptions |
| `BR-13` | Payment Batch Generation & Approval | Must Have | `TC-FUNC-15` | Financial / Treasury |
| `BR-14` | Executive Analytics Dashboard | Should Have | `TC-FUNC-16` | Reporting / Analytics |
| `BR-15` | Segregation of Duties (SoD) & RBAC | Must Have | `TC-FUNC-17` | Security / Access |
| `BR-16` | Immutable Audit Logging | Must Have | `TC-FUNC-18` | Compliance / Audit |
| `BR-17` | Hold Escalation Timers (7-Day SLA) | Could Have | `TC-FUNC-19` | Workflow / Timing |
| `BR-18` | End-User Training Certification | Should Have | `TC-FUNC-20` | Enablement / Change |
