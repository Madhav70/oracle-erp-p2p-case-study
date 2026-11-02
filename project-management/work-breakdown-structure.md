# Work Breakdown Structure (WBS)

**Project**: Procure-to-Pay (P2P) Implementation Simulation  
**Organization**: Northstar Manufacturing Ltd. (Fictional Enterprise)  
**Standard**: PMBOK 5-Level Work Breakdown Structure  
**Document Reference**: PMO-WBS-001

> **Simulated Project Disclaimer**:  
> This WBS is an academic and portfolio artifact. It models a standard enterprise ERP implementation schedule across a 14-week execution lifecycle.

---

## 1. WBS Level 1 & Level 2 Hierarchy Overview

```
1.0 Oracle ERP Procure-to-Pay (P2P) Implementation
  ├── 1.1 Project Management & Governance
  ├── 1.2 Business Discovery & Requirements
  ├── 1.3 Solution Architecture & Functional Design
  ├── 1.4 Configuration & Prototype Walkthroughs
  ├── 1.5 Master Data Cleansing & Migration
  ├── 1.6 Quality Assurance & Testing
  ├── 1.7 Organizational Change Management & Training
  └── 1.8 Cutover, Go-Live & Hypercare Support
```

---

## 2. Detailed Work Breakdown Structure (Levels 3, 4, and 5)

| WBS Code | Workstream / Task Name | Predecessors | Estimated Duration | Responsible Owner | Primary Deliverable / Milestone |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | **Project Management & Governance** | | | | |
| 1.1.1 | Project Kick-off Meeting & Sponsor Mobilization | None | 3 Days | Project Manager | Project Kickoff Slide Deck & Attendance Log |
| 1.1.2 | Project Charter Authoring & Executive Sign-off | 1.1.1 | 5 Days | PM / Functional Lead | Approved & Signed Project Charter |
| 1.1.3 | Risk Register & RACI Matrix Baseline | 1.1.2 | 4 Days | Project Manager | Baselined Risk Register & RACI Matrix |
| 1.1.4 | Bi-Weekly Steering Committee Reviews | Continuous | 14 Weeks | PM / Sponsor (CFO) | Bi-Weekly Executive Status Decks |
| 1.1.5 | PMO Change Control Board Administration | Continuous | 14 Weeks | Project Manager | Maintained Project Change Log |
| **1.2** | **Business Discovery & Requirements** | | | | |
| 1.2.1 | As-Is Procurement Process Discovery Workshops | 1.1.2 | 6 Days | Functional Consultant | Current State Process Maps (Mermaid) |
| 1.2.2 | As-Is Accounts Payable & Dock Intake Workshops | 1.2.1 | 5 Days | Functional Consultant | As-Is Exception & Bottleneck Analysis |
| 1.2.3 | Business Requirements Document (BRD) Drafting | 1.2.2 | 7 Days | Business Analyst / PM | BRD Matrix (18 Traceable Requirements) |
| 1.2.4 | Gap Analysis Matrix & Remediation Formulation | 1.2.3 | 4 Days | Functional Consultant | Finalized Gap Analysis Matrix |
| 1.2.5 | Delegation of Authority (DoA) Policy Sign-off | 1.2.3 | 4 Days | Finance Lead / Controller | Signed Delegation of Authority Matrix |
| **1.3** | **Solution Architecture & Functional Design** | | | | |
| 1.3.1 | To-Be 10-Step Procure-to-Pay Process Design | 1.2.3, 1.2.5 | 6 Days | Functional Consultant | To-Be Process Flowcharts (Mermaid) |
| 1.3.2 | Requisition & Catalog Configuration Specifications | 1.3.1 | 5 Days | Functional Consultant | Self-Service Procurement FDD Section |
| 1.3.3 | Approvals Management Engine (AME) Logic Design | 1.3.1 | 5 Days | Functional Consultant | Approval Hierarchy Technical Spec |
| 1.3.4 | 3-Way & 2-Way Invoice Matching & Tolerance Spec | 1.3.1 | 5 Days | Finance Systems Lead | Matching Rules & Tolerance Group FDD |
| 1.3.5 | Security Profiles & Segregation of Duties Matrix | 1.3.1 | 4 Days | IT Security Lead | Role-Based Access Control (RBAC) Spec |
| **1.4** | **Configuration & Prototype Preparation** | | | | |
| 1.4.1 | Staging Sandbox Environment Provisioning | 1.3.5 | 3 Days | Technical Lead | Configured Staging Tenant |
| 1.4.2 | Business Unit & Cost Center Account Structure Setup | 1.4.1 | 4 Days | Finance Lead | General Ledger Flexfield Setup |
| 1.4.3 | Requisition Catalog & Category Hierarchies Setup | 1.4.2 | 5 Days | Procurement Lead | Requisition Workbenches Active |
| 1.4.4 | Matching Tolerance Group & Hold Rules Configuration | 1.4.2 | 4 Days | Functional Consultant | Configured Tolerance Group (1.5% / $50) |
| 1.4.5 | Conference Room Pilot 1 (CRP-1) Execution | 1.4.3, 1.4.4 | 5 Days | Core Project Team | CRP-1 Walkthrough Sign-off Memo |
| **1.5** | **Master Data Cleansing & Migration** | | | | |
| 1.5.1 | Legacy Supplier Master Data Extract & Profiling | 1.2.3 | 5 Days | Master Data SME | Raw Supplier Extract & Profiling Report |
| 1.5.2 | Automated Cleansing Scripts & Field Standardization | 1.5.1 | 7 Days | Data Migration Lead | Cleansed Supplier Master (25 Vendors) |
| 1.5.3 | Open Purchase Order Balance Reconciliation Script | 1.5.2 | 5 Days | Data Migration Lead | Validated Open PO Balance Table |
| 1.5.4 | Mock Cutover 1 Data Migration Execution | 1.4.5, 1.5.2 | 3 Days | Data Migration Lead | Mock Cutover 1 Reconciliation Report |
| 1.5.5 | Mock Cutover 2 (Full Volume Dress Rehearsal) | 1.6.3, 1.5.4 | 3 Days | Technical Lead / PMO | Mock Cutover 2 Sign-off Certificate |
| **1.6** | **Quality Assurance & Testing** | | | | |
| 1.6.1 | Functional Test Case Authoring (FUT Catalogue) | 1.3.1 | 6 Days | QA Lead | Functional Test Matrix (22 Test Cases) |
| 1.6.2 | Functional Unit Testing (FUT) Execution | 1.4.5, 1.6.1 | 7 Days | Functional Team | FUT Execution Log |
| 1.6.3 | System Integration Testing (SIT) Across Workstreams | 1.6.2 | 8 Days | QA Team / Leads | End-to-End SIT Sign-off Memo |
| 1.6.4 | User Acceptance Testing (UAT) Scenario Authoring | 1.6.1 | 5 Days | Business Analyst | UAT Scenario Matrix (12 Scenarios) |
| 1.6.5 | User Acceptance Testing (UAT) Business Execution | 1.6.3, 1.6.4 | 10 Days | Business Process SMEs | Formal UAT Business Sign-off Protocol |
| 1.6.6 | Defect Triage & Remediation Sprints | Continuous | 3 Weeks | Dev / Functional Leads | Closed Defect Log (0 Open Sev 1/2) |
| **1.7** | **Organizational Change Management & Training** | | | | |
| 1.7.1 | Stakeholder Impact Analysis by Operational Role | 1.2.3 | 5 Days | Change Lead | Role Impact Assessment Matrix |
| 1.7.2 | Training Curriculum & Sandbox Scenario Development | 1.7.1, 1.4.5 | 8 Days | Training Lead | 5 Role-Tailored Course Modules |
| 1.7.3 | Laminated Dock Job Aids & Quick-Reference Guides | 1.7.2 | 4 Days | Change Lead | Published Visual Desk Job Aids |
| 1.7.4 | End-User Training Delivery (Requisitioner, Dock, AP)| 1.7.2, 1.6.5 | 8 Days | Training Lead / SMEs | Training Attendance & Pass Rosters (>=90%)|
| 1.7.5 | Supplier Enablement Notice Letters Dispatched | 1.7.1 | 3 Days | Procurement Lead | Transmitted Vendor Enablement Packs |
| **1.8** | **Cutover, Go-Live & Hypercare Support** | | | | |
| 1.8.1 | Cutover Runbook & Rollback Contingency Authoring | 1.5.5, 1.6.5 | 4 Days | Technical Lead / PMO | Detailed 48-Hour Weekend Runbook |
| 1.8.2 | Steering Committee Formal Go / No-Go Decision Gate | 1.8.1, 1.7.4 | 1 Day | Steering Committee | Signed Go/No-Go Decision Protocol |
| 1.8.3 | 48-Hour Weekend Cutover Execution & Blackout | 1.8.2 | 2 Days (Weekend) | Technical / PMO Leads | Production Verification & Smoke Test Pass |
| 1.8.4 | Day 1 Production Go-Live Command Center Launch | 1.8.3 | 1 Day | Full Project Team | Production System Live for All Users |
| 1.8.5 | 14-Day Hypercare On-Site Floor Support & Triage | 1.8.4 | 14 Days | Functional / Super-Users| Daily Hypercare Incident Dashboard |
| 1.8.6 | Transition to Steady-State P2P Governance Council | 1.8.5 | 3 Days | PMO / Governance Lead| Final Handover Protocol & Retrospective |
