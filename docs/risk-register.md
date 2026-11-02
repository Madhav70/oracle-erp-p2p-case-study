# Project Risk Register & Mitigation Strategy

**Project**: Procure-to-Pay (P2P) Implementation Simulation  
**Organization**: Northstar Manufacturing Ltd. (Fictional Enterprise)  
**Methodology**: PMBOK Risk Management Framework  
**Risk Scoring Formula**: $\text{Risk Score} = \text{Likelihood (1–5)} \times \text{Impact (1–5)}$ (Scale: 1 to 25)

> **Simulated Project Disclaimer**:  
> This risk register is formulated for an academic, project-management, and business-analysis portfolio demonstration. It models real-world enterprise risks encountered during cloud ERP procure-to-pay transformations.

---

## 1. Risk Evaluation Criteria & Severity Tiers

- **Low Risk (Score 1–6)**: Managed through standard operational cadence and routine monitoring.
- **Medium Risk (Score 8–12)**: Proactive mitigation plan required; reviewed bi-weekly in PMO standups.
- **High / Critical Risk (Score 15–25)**: Executive intervention required; reported weekly to Steering Committee.

```
+-------------------------------------------------------------------------------------------------+
|                                     RISK HEATMAP DISTRIBUTION                                   |
+-------------------------------------------------------------------------------------------------+
| Likelihood \ Impact  | 1 (Negligible) | 2 (Minor) | 3 (Moderate) | 4 (Major)     | 5 (Critical) |
+----------------------+----------------+-----------+--------------+---------------+--------------+
| 5 (Almost Certain)   | 5              | 10        | 15           | 20 [RSK-01]   | 25           |
| 4 (Likely)           | 4              | 8         | 12 [RSK-07]  | 16 [RSK-03,08]| 20 [RSK-09]  |
| 3 (Possible)         | 3              | 6         | 9  [RSK-04]  | 12 [RSK-02,05]| 15 [RSK-11]  |
| 2 (Unlikely)         | 2              | 4         | 6  [RSK-06]  | 8  [RSK-10]   | 10 [RSK-12]  |
| 1 (Rare)             | 1              | 2         | 3            | 4             | 5            |
+-------------------------------------------------------------------------------------------------+
```

---

## 2. Comprehensive Risk Register (13 Entries)

| Risk ID | Category | Risk Description | Likelihood (1–5) | Impact (1–5) | Score (1–25) | Severity Tier | Preventative Mitigation Strategy | Contingency Plan | Risk Owner | Current Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **RSK-01** | **Data Quality** | Legacy vendor records contain duplicate entries, incomplete tax IDs, and outdated payment terms, corrupting the new vendor master. | 5 | 4 | **20** | **Critical** | Implement pre-migration automated data cleansing scripts; enforce mandatory tax/banking validation gates. | Fallback to manual verification sprint for top 80% spend suppliers; quarantine incomplete vendors. | Master Data SME / AP Lead | Active / In Progress |
| **RSK-02** | **Scope Creep** | Business stakeholders request advanced sourcing RFx and contract lifecycle authoring modules during Phase 1 design. | 3 | 4 | **12** | **Medium** | Enforce strict Project Charter scope boundary; establish formal PMO Change Control Board (CCB) process. | Defer all advanced sourcing requests to Phase 2 roadmap with formal steering committee memo. | Project Manager | Mitigated |
| **RSK-03** | **Stakeholder Availability** | Operational SMEs from AP and Purchasing are overburdened with daily plant operations, missing design and UAT sessions. | 4 | 4 | **16** | **High** | Secure executive sponsor mandate allocating 30% dedicated SME project time; fund temporary AP backfill contractor. | Reschedule critical UAT workshops to half-day focused morning blocks; escalate persistent absenteeism to CFO. | Executive Sponsor (CFO) | Active / Managed |
| **RSK-04** | **Approval Latency** | Department managers fail to act on electronic requisition approvals within 48 hours, causing procurement bottlenecks. | 3 | 3 | **9** | **Medium** | Configure automated 48-hour email reminders and 72-hour supervisory escalation rules in approval workflow. | Establish temporary peer-delegation rules during holiday and peak production periods. | Procurement Lead | Mitigated |
| **RSK-05** | **Testing Coverage** | UAT scenarios fail to test complex edge cases (e.g. partial receipts, damaged deliveries, credit memo cancellations), leading to post-launch defects. | 3 | 4 | **12** | **Medium** | Develop comprehensive 20-scenario functional catalogue and 12-scenario UAT matrix with negative testing paths. | Mandate 100% test execution pass rate on Severity 1 & 2 scenarios before cutover authorization. | QA Lead | Active / Managed |
| **RSK-06** | **Security & SoD** | Overly permissive user roles allow requisitioners to approve their own orders or AP staff to edit vendor banking details. | 2 | 3 | **6** | **Low** | Design rigorous Role-Based Access Control (RBAC) security matrix enforcing strict Segregation of Duties (SoD). | Conduct pre-cutover access control audit and obtain formal sign-off from Internal Audit / Compliance. | IT Security Lead | Mitigated |
| **RSK-07** | **Integration / Formats** | Electronic payment batch files generated by Payables fail validation during commercial bank ingestion due to character encoding mismatches. | 4 | 3 | **12** | **Medium** | Conduct early end-to-end payment file mock tests with commercial bank using synthetic test data in Week 9. | Maintain dual-processing capability (manual bank portal upload) for Week 1 go-live as temporary fallback. | Treasury / Finance Lead | Active / Managed |
| **RSK-08** | **User Adoption** | Warehouse dock clerks resist digital receiving workbench, continuing to rely on paper slips and causing missing receipt holds. | 4 | 4 | **16** | **High** | Conduct hands-on floor training labs at warehouse docks; install dedicated ruggedized touchscreens; deploy visual 1-page guides. | Station dedicated hypercare floor support specialist on receiving dock during first two weeks of go-live. | Change Management Lead | Active / In Progress |
| **RSK-09** | **Cutover Downtime** | Legacy PO data extraction and open balance cutover exceed 48-hour weekend blackout window, threatening Monday plant production. | 4 | 5 | **20** | **Critical** | Execute two full mock cutover dry runs in Weeks 10 and 12; optimize SQL migration scripts; baseline execution timestamps. | Trigger cutover rollback protocol if critical migration milestone is delayed beyond Sunday 18:00 cutoff. | Technical Lead / PMO | Active / High Priority |
| **RSK-10** | **Reporting Inaccuracy** | Discrepancies between executive OTBI spend dashboards and general ledger subledger balances undermine leadership confidence. | 2 | 4 | **8** | **Medium** | Establish automated reconciliation scripts cross-referencing subledger accounting entries against reporting tables. | Perform formal weekly financial reconciliation between AP trial balance and executive dashboard metrics. | BI / Reporting Analyst | Active / Managed |
| **RSK-11** | **Supplier Resistance** | Strategic vendors fail to quote PO numbers on invoices or reject electronic submission guidelines, stalling automated matching. | 3 | 5 | **15** | **High** | Transmit formal supplier enablement packets at T-4 and T-1 weeks; mandate PO quotation on all supplier billing documents. | Establish temporary AP exception triage desk to contact non-compliant suppliers during initial 30 days. | Procurement Lead | Active / High Priority |
| **RSK-12** | **Regulatory Compliance** | Failure to retain complete immutable audit logs of invoice tolerance overrides violates internal SOX-equivalent financial controls. | 2 | 5 | **10** | **Medium** | Enable database-level transaction logging; implement automated weekly change audit reports for internal review. | Configure secondary managerial approval workflow for any manual price tolerance overrides $> \$250$. | Internal Audit / Compliance | Mitigated |
| **RSK-13** | **Hardware / Dock Network** | Wi-Fi dead zones on Warehouse Dock C prevent receiving clerks from accessing cloud receiving workbench during deliveries. | 3 | 3 | **9** | **Medium** | Conduct wireless site survey across all receiving bays; install industrial ruggedized access points prior to testing. | Deploy hardwired Ethernet terminals as primary backup workstations at each dock desk. | Facilities / IT Infrastructure | Mitigated |
