# Project Implementation Plan & Master Schedule

**Project**: Procure-to-Pay (P2P) Modernization  
**Organization**: Northstar Manufacturing Ltd. (Fictional Enterprise)  
**Methodology**: Hybrid Agile-Waterfall ERP Implementation  
**Total Duration**: 14 Weeks + Hypercare Support (Illustrative Planning Horizon)

> **Simulated Project Disclaimer**:  
> This project plan represents an illustrative planning model developed for an independent academic and portfolio case study. Durations, workstream allocations, and phase exit criteria illustrate typical mid-market enterprise ERP deployments and do not represent an official Oracle Corporation project schedule.

---

## 1. Project Phase Breakdown & Roadmap

```
+-----------------------------------------------------------------------------------------------------------------------+
| Week:  01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | +Hypercare (Weeks 15-16)             |
+-----------------------------------------------------------------------------------------------------------------------+
| [Phase 1: Discovery & Requirements]                                                                                   |
|        Weeks 1 - 3                                                                                                    |
|                     [Phase 2: Solution Design & Prototype Prep]                                                       |
|                                Weeks 4 - 7                                                                            |
|                                             [Phase 3: Testing & Quality Assurance]                                    |
|                                                        Weeks 8 - 11                                                   |
|                                                                     [Phase 4: Training & Cutover]                     |
|                                                                                Weeks 12 - 13                          |
|                                                                                              [Phase 5: Go-Live & Ops] |
|                                                                                                        Week 14 + HC   |
+-----------------------------------------------------------------------------------------------------------------------+
```

---

## 2. Phase-by-Phase Workstream Breakdown

### Phase 1: Project Initiation, Discovery & Requirements (Weeks 1–3)
- **Objectives**: Mobilize project team, align executive sponsorship, document current As-Is pain points, and baseline traceable business requirements.
- **Key Tasks**:
  - `TSK-1.1`: Formal Project Kick-off and Charter Sign-off.
  - `TSK-1.2`: As-Is Process Discovery Workshops with Procurement, Warehouse, and AP teams.
  - `TSK-1.3`: Draft and baseline Business Requirements Document (BRD) with 18 traceable entries.
  - `TSK-1.4`: Conduct Gap Analysis Matrix across process, data, and controls.
  - `TSK-1.5`: Finalize Delegation of Authority (DoA) Matrix with Finance and Operations.
- **Phase Exit Gate (Milestone 1 - Week 3)**: Unanimous Steering Committee sign-off on Project Charter, BRD, and Scope Baseline.

### Phase 2: Solution Design & Prototype Preparation (Weeks 4–7)
- **Objectives**: Translate requirements into functional design specifications, configure prototype workflows in staging environment, and establish master data standards.
- **Key Tasks**:
  - `TSK-2.1`: Author Functional Design Document (FDD) covering 10-step To-Be lifecycle.
  - `TSK-2.2`: Configure Self-Service Requisition item templates and accounting flexfields.
  - `TSK-2.3`: Configure Approvals Management Engine (AME) routing rules ($<\$5\text{k}, \$5\text{k}-\$25\text{k}, >\$25\text{k}$).
  - `TSK-2.4`: Configure 3-Way and 2-Way Invoice Matching rules with $1.5\% / \$50$ tolerance group.
  - `TSK-2.5`: Establish Supplier Master Data cleansing rules and mock extract scripts.
  - `TSK-2.6`: Conduct Conference Room Pilot 1 (CRP-1) prototype walkthrough with business leads.
- **Phase Exit Gate (Milestone 2 - Week 7)**: Successful execution of CRP-1 and sign-off on Functional Design Documents.

### Phase 3: Testing & Quality Assurance (Weeks 8–11)
- **Objectives**: Validate system functionality against requirements, conduct end-to-end integration tests, execute mock data loads, and complete business UAT.
- **Key Tasks**:
  - `TSK-3.1`: Author Functional Test Cases (20 test cases) covering positive and negative paths.
  - `TSK-3.2`: Execute Functional Unit Testing (FUT) in test sandbox.
  - `TSK-3.3`: Conduct System Integration Testing (SIT) spanning PR $\rightarrow$ PO $\rightarrow$ Dock Receipt $\rightarrow$ Matching $\rightarrow$ Payment File.
  - `TSK-3.4`: Execute Mock Cutover Data Migration 1 (Cleansed Supplier Master & Open PO balances).
  - `TSK-3.5`: Facilitate User Acceptance Testing (UAT) with business SMEs across 12 end-to-end business scenarios.
  - `TSK-3.6`: Defect triage, remediation, and re-testing.
- **Phase Exit Gate (Milestone 3 - Week 11)**: Formal UAT business sign-off with 0 open Severity 1/2 defects and $100\%$ requirement traceability.

### Phase 4: End-User Enablement & Cutover Readiness (Weeks 12–13)
- **Objectives**: Deliver role-based training, conduct Mock Cutover 2, execute cutover checklist during plant blackout, and obtain formal Go-Live authorization.
- **Key Tasks**:
  - `TSK-4.1`: Publish role-tailored training modules, job aids, and dock receiving laminated guides.
  - `TSK-4.2`: Conduct end-user training labs for Plant Requisitioners, Dock Clerks, and AP Specialists.
  - `TSK-4.3`: Execute Mock Cutover Data Migration 2 with final reconciliation audits.
  - `TSK-4.4`: Transmit formal vendor enablement letters to all 25 active suppliers.
  - `TSK-4.5`: Convene Steering Committee Go / No-Go Decision Gate.
  - `TSK-4.6`: Execute 48-Hour Weekend Production Cutover Runbook (Legacy PO freeze, final delta load, production configuration verification).
- **Phase Exit Gate (Milestone 4 - End of Week 13)**: Unanimous Go-Live authorization; successful production data migration sign-off.

### Phase 5: Production Go-Live & Hypercare Support (Week 14 + Weeks 15–16)
- **Objectives**: Launch system into active plant operations, support operational users, monitor matching hold rates, and transition to ongoing governance.
- **Key Tasks**:
  - `TSK-5.1`: Day 1 Go-Live Command Center mobilization (on-site floor support at warehouse docks and purchasing offices).
  - `TSK-5.2`: Daily hypercare standups and rapid-response defect triage.
  - `TSK-5.3`: Monitor Week 1 transaction processing, PO issuance cycle times, and invoice hold rates.
  - `TSK-5.4`: Finalize Project Retrospective, Lessons Learned documentation, and transition to P2P Governance Council.
- **Phase Exit Gate (Milestone 5 - End of Week 16)**: Formal project closure and transition to steady-state operational support.

---

## 3. Implementation Schedule Summary Table

| Milestone Ref | Milestone Description | Planned Target Date | Workstream Owner | Prerequisite Dependencies | Verification Gate Deliverable |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M1** | Project Charter & Requirements Baseline | End of Week 3 | PMO / Steering Comm | Kickoff complete, Discovery held | Approved Charter & Signed BRD Matrix |
| **M2** | Functional Design & CRP-1 Walkthrough | End of Week 7 | Functional Consultant | Requirements sign-off | Signed FDD & CRP-1 Exit Memo |
| **M3** | User Acceptance Testing (UAT) Sign-off | End of Week 11 | QA Lead / AP & Buyer Leads | SIT complete, Test cases written | UAT Sign-off Protocol (0 Sev 1/2 defects) |
| **M4** | Training Complete & Go/No-Go Approval | End of Week 13 | Change Lead / Sponsor (CFO) | Mock Cutover 2, User Training $\ge 90\%$ | Signed Go/No-Go Governance Protocol |
| **M5** | Cutover Complete & Production Go-Live | Start of Week 14 | Technical Lead / PMO | 48-hr weekend blackout runbook | Production Validation & Smoke Test Sign-off |
| **M6** | Hypercare Exit & Operational Handover | End of Week 16 | PMO / Operations Leads | 2 weeks stable production operations | Final Project Retrospective & Handover Memo |
