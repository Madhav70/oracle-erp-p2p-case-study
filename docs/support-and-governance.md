# Post-Implementation Support Model & P2P Governance Framework

**Project**: Procure-to-Pay (P2P) Implementation Simulation  
**Organization**: Northstar Manufacturing Ltd. (Fictional Enterprise)  
**Governance Scope**: Steady-State Operations & Continuous Improvement  
**Document Reference**: GOV-P2P-001

> **Simulated Project Disclaimer**:  
> This support and governance document is an academic and portfolio artifact. It models industry-standard IT service management (ITIL-aligned) and corporate operational governance structures for enterprise business processes.

---

## 1. Post-Go-Live Support Tier Architecture (L1 / L2 / L3)

Following the conclusion of the 14-day hypercare period, technical and operational support transitions to a sustainable three-tiered support structure:

```
+---------------------------------------------------------------------------------------------------------+
|                                    STEADY-STATE SUPPORT TIER MODEL                                      |
+---------------------------------------------------------------------------------------------------------+
|  Tier Level   | Team Composition                    | Primary Responsibilities                          |
+---------------+-------------------------------------+---------------------------------------------------+
|  Tier 1 (L1)  | Super-Users & Department Champions  | User navigation, password resets, basic           |
|               | (Plant, Dock, AP Lead)              | requisition entry assistance, job aid coaching.   |
+---------------+-------------------------------------+---------------------------------------------------+
|  Tier 2 (L2)  | Internal IT Business Systems Team   | Approval rule adjustments, user role provisioning,|
|               | & Functional Lead                   | tolerance group tuning, data discrepancy checks.  |
+---------------+-------------------------------------+---------------------------------------------------+
|  Tier 3 (L3)  | ERP Cloud Vendor Support & Systems  | Cloud patch defects, underlying database issues,  |
|               | Integration Consulting Partner      | interface failures, critical architectural bugs.  |
+---------------------------------------------------------------------------------------------------------+
```

---

## 2. Service Level Agreements (SLAs) by Incident Priority

| Incident Priority | Example Operational Scenario | Initial Acknowledgment | Target Workaround SLA | Target Permanent Resolution |
| :--- | :--- | :--- | :--- | :--- |
| **P1 - Critical** | Automated matching engine down; warehouse unable to log any goods receipts; plant production at risk. | 15 Minutes | 2 Hours | 8 Hours |
| **P2 - High** | Requisition approval workflow stalled for an entire department; payment file export failing for weekly run. | 1 Hour | 6 Hours | 24 Hours |
| **P3 - Medium** | Specific vendor invoice failing tolerance check incorrectly; minor report formatting alignment error. | 4 Hours | 24 Hours | 72 Hours |
| **P4 - Low** | General user enhancement request; request for additional non-mandatory report filter. | 1 Business Day | Next Scheduled Release | Next Quarterly Maintenance Release |

---

## 3. P2P Governance Council Charter

To ensure that Procure-to-Pay processes remain standardized, compliant, and continuously optimized across Northstar Manufacturing Ltd., a permanent cross-functional **P2P Governance Council** is chartered.

### 3.1 Council Composition & Representation
- **Council Chair**: Finance Director / Corporate Controller
- **Co-Chair**: Head of Strategic Procurement & Supply Chain
- **Core Members**:
  - Accounts Payable Lead
  - Purchasing Lead
  - Warehouse Receiving Lead
  - IT Business Systems Lead
  - Internal Audit / SOX Compliance Representative

### 3.2 Mandate & Authority
1. **Delegation of Authority (DoA) Custody**: Review and formally authorize any proposed alterations to monetary approval thresholds.
2. **Tolerance Policy Governance**: Annually review and adjust matching tolerance limits ($1.5\% / \$50$) based on historical invoice audit statistics.
3. **Master Data Integrity**: Review quarterly vendor deduplication reports, inactive vendor retirements, and spend categorization accuracy.
4. **Policy Enforcement**: Monitor maverick buying rates and address persistent organizational non-compliance directly with operating department heads.

---

## 4. Continuous Improvement & Operational KPI Review Cadence

The P2P Governance Council convenes on a recurring monthly schedule to evaluate operational performance against target SLAs:

```
+---------------------------------------------------------------------------------------------------------+
|                                    MONTHLY GOVERNANCE KPI SCORECARD                                     |
+---------------------------------------------------------------------------------------------------------+
| Metric Focus Area          | Primary Measure                    | Operating Target  | Escalation Trigger|
+----------------------------+------------------------------------+-------------------+-------------------+
| Requisition Turnaround     | Requisition submission to approval | <= 1.0 Day        | > 2.0 Days        |
| PO Issuance Latency        | PR approval to PO dispatch         | <= 1.0 Day        | > 2.0 Days        |
| Dock Receipt Compliance    | Receipts logged on delivery date   | >= 95.0%          | < 90.0%           |
| Invoice Auto-Match Rate    | Invoices matching without hold     | >= 75.0%          | < 65.0%           |
| Invoice Hold Resolution    | Days to clear price/dock holds     | <= 3.0 Days       | > 5.0 Days        |
| Supplier PO Compliance     | Supplier invoices quoting valid PO | >= 98.0%          | < 95.0%           |
| Payment Discount Capture   | Available early discounts secured  | >= 90.0%          | < 80.0%           |
+---------------------------------------------------------------------------------------------------------+
```

### Review Rhythm:
- **Monthly Cadence (1st Tuesday)**: Review the KPI Scorecard, assess supplier exception trends, and review open Sev 3 defects.
- **Quarterly Strategic Review**: Evaluate supplier performance scorecards, review catalog coverage, and prioritize process automation backlog items.
