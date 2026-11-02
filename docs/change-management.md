# Change Management & User Enablement Strategy

**Project**: Procure-to-Pay (P2P) Implementation Simulation  
**Organization**: Northstar Manufacturing Ltd. (Fictional Enterprise)  
**Framework**: Prosci ADKAR Model for Organizational Change  
**Author**: Change Management & Training Lead

> **Simulated Project Disclaimer**:  
> This change management strategy is an academic and portfolio artifact detailing modern organizational change management (OCM), training design, and user adoption measurement for enterprise ERP transitions.

---

## 1. Change Management Methodology (Prosci ADKAR Framework)

To transition Northstar Manufacturing Ltd. from informal paper/email purchasing to a disciplined digital ERP environment, the change strategy aligns with the five phases of the **ADKAR** model:

```
[Awareness]      -> [Desire]         -> [Knowledge]      -> [Ability]        -> [Reinforcement]
"Why change?"       "What's in it for  "How to operate in  "Hands-on practice   "Sustained habit &
                     me & company?"     the new system?"    in sandbox & labs"   continuous adoption"
Weeks 1 - 4         Weeks 4 - 8         Weeks 9 - 12        Weeks 12 - 13        Weeks 14 - 16+
```

1. **Awareness (Weeks 1–4)**: Transparent communication regarding current operational pain points (24.5% invoice holds, supplier payment delays, maverick spend) and the strategic necessity of standardizing procurement.
2. **Desire (Weeks 4–8)**: Demonstrating personal benefits for each role—eliminating tedious paper chasing for buyers, removing payment friction for AP, and empowering requisitioners with real-time tracking.
3. **Knowledge (Weeks 9–12)**: Structured role-based training curriculums, interactive system walk-throughs, and laminated desk job aids.
4. **Ability (Weeks 12–13)**: Hands-on scenario simulations in the training sandbox, role proficiency assessments ($\ge 90\%$ pass requirement), and mock cutover drills.
5. **Reinforcement (Weeks 14–16+)**: On-site floor support champions, hypercare helpdesk, weekly adoption scorecards, and recognition of high-performing departments.

---

## 2. Role-Based Stakeholder Impact Assessment

| Operational Persona | Current Working Practice (As-Is) | Future Working Practice (To-Be) | Perceived Change Impact | Primary Change Challenges & Mitigations |
| :--- | :--- | :--- | :--- | :--- |
| **Plant Requisitioners** | Fill out paper forms, send emails to buyers, phone favored vendors directly. | Log into Self-Service portal, select catalog items, input cost center, track digital approval status. | **Medium** | *Challenge*: Resistance to standardized catalog rules.  <br>*Mitigation*: Simplified "shopping cart" UI, quick-order templates for frequent items. |
| **Department Managers** | Sign physical paperwork or reply "approved" to loose email threads. | Review automated approval notifications in system or via mobile; act within 48-hour SLA. | **Medium** | *Challenge*: Delays due to traveling or competing plant duties.  <br>*Mitigation*: In-app 1-click approvals, automated delegation during planned leave. |
| **Procurement Buyers** | Re-type requisition details into Excel, chase suppliers via email for quotes and delivery updates. | Automated conversion of approved PRs into POs; focus on strategic supplier agreements and price dispute reviews. | **High** | *Challenge*: Shift from clerical entry to strategic contract management.  <br>*Mitigation*: In-depth buyer workbench training; automated BPA dispatch. |
| **Receiving Dock Clerks** | Stamp paper delivery slips, store dockets in physical dock binders. | Digital PO lookup on dock terminals; record received count and condition; flag damaged goods. | **High** | *Challenge*: Reluctance to use computers on industrial dock floor.  <br>*Mitigation*: Ruggedized touchscreens, visual 1-page dock job aids, floor super-users. |
| **Accounts Payable Staff** | Manually cross-check paper invoices against spreadsheets and phone docks to locate lost slips. | Manage exceptions on automated hold worklists; review 3-Way match holds; execute automated payment runs. | **High** | *Challenge*: Apprehension regarding automated tolerance matching.  <br>*Mitigation*: Hands-on exception resolution labs, clear policy rules for variance overrides. |

---

## 3. Role-Tailored Training Curriculum

| Course Code | Target Audience | Course Title & Scope | Duration | Delivery Format | Mandatory Prerequisite | Competency Assessment Method |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TRN-101** | All Requisitioners | *Self-Service Requisitioning Fundamentals*: Catalog search, non-catalog requests, expense allocations. | 1.5 Hours | Interactive Virtual Lab / Recorded Module | None | Submit test requisition in sandbox without validation errors. |
| **TRN-201** | Dept Managers & Directors | *Delegation of Authority & Workflow Approvals*: Approving, reassigning, rejecting, and tracking department spend. | 1.0 Hour | Executive Briefing & Sandbox Walkthrough | TRN-101 | Successfully approve and reject sample PRs; set up vacation delegate. |
| **TRN-301** | Procurement Buyers | *Purchasing Workbench Mastery*: Blanket agreements, auto-creation rules, PO dispatch, supplier exception triage. | 4.0 Hours | Classroom Workshop & Hands-on Lab | TRN-101, 201 | End-to-end execution of complex multi-line PO and BPA setup. |
| **TRN-401** | Warehouse Receiving Staff | *Dock Receiving & Inspection Operations*: PO search, full receipt, partial delivery logging, RMA damage holds. | 2.5 Hours | On-Dock Floor Lab with Rugged Terminals | None | Physical simulation of receiving 3 sample shipments with inspection dispositions. |
| **TRN-501** | Accounts Payable Team | *Payables Automation & Hold Resolution*: 3-Way match review, tolerance overrides, hold releases, payment batch runs. | 6.0 Hours (2x 3hr) | Intensive Hands-on Workshop | None | Resolve 5 simulated invoice hold scenarios and generate sample payment batch. |

---

## 4. Communication Cascade Plan

```
[Month -2: T-8 Wks]  Executive Kickoff Town Hall: "Modernizing Northstar Procurement"
[Month -1: T-4 Wks]  Manager Roadshows: "DoA Policies, Roles & Training Schedules"
[T-2 Weeks]          Vendor Notice Sent: "Mandatory PO Quotation Guidelines for Invoices"
[T-1 Week]           "Go-Live Readiness Guide" & 1-Page Quick Reference Job Aids Distributed
[Go-Live Day]        Day 1 Welcome Bulletin & Command Center Contact Desk Published
[Post-Launch +2 Wks] "First 100 POs Celebrated" & User Feedback Pulse Survey Published
```

---

## 5. User Adoption Monitoring & Success Metrics

To ensure the new processes take root and deliver expected operational benefits, the PMO tracks five post-launch adoption indicators:

| Adoption Metric | Measurement Frequency | Baseline (Legacy) | Post-Go-Live Target | Remediation Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **Requisition First-Pass Accuracy** | Weekly | 55% (frequent errors) | $\ge 92\%$ approved without revision | $< 80\%$ triggers refresher coaching for department |
| **Requisition Approval SLA ($< 24\text{h}$)** | Weekly | 2.5 days | $\ge 90\%$ approved within 24 hours | Requisitions stagnant $> 48\text{h}$ auto-escalated |
| **Dock Receipts Logged on Day of Arrival** | Daily | 40% (delays/lost slips) | $\ge 95\%$ logged same day as delivery | Daily dock backlog review with Warehouse Manager |
| **Invoices Processed via Auto-Match** | Weekly | 0% (100% manual) | $\ge 75\%$ clean match without clerical hold | Drop below 65% triggers supplier pricing audit |
| **User Training Completion Rate** | Pre-Cutover Gate | 0% | $100\%$ certified prior to production access | Mandatory block on system login until course passed |
