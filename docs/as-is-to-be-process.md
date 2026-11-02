# As-Is vs. To-Be Process Mapping: Procure-to-Pay Lifecycle

**Client Organization**: Northstar Manufacturing Ltd. (Fictional Enterprise)  
**Process Area**: Procure-to-Pay (P2P)  
**Author**: P2P Functional Design Team

> **Simulated Project Disclaimer**:  
> This operational process documentation is formulated for an independent simulated implementation case study. It establishes conceptual operational models aligned with modern cloud ERP standards (such as Oracle Fusion Cloud) to demonstrate business analysis, process re-engineering, and internal controls design.

---

## 1. Executive Summary & Process Transformation Vision

Prior to the modernization initiative, Northstar Manufacturing Ltd. operated an informal, largely manual procurement process fraught with operational friction, disconnected spreadsheets, physical paper shuffling, and uncoordinated communication. The future-state architecture transitions Northstar into an integrated, auditable, and automated digital lifecycle spanning self-service requisitioning, automated Delegation of Authority (DoA) approvals, real-time receiving, automated multi-way matching, tolerance-driven exception management, and systematic cash management.

```
+----------------------------------------------------------------------------------------------------+
|                                    TRANSFORMATION AT A GLANCE                                      |
+----------------------------------------------------------------------------------------------------+
|  Process Domain        |  As-Is Current State (Fragmented)        |  To-Be Future State (Oracle ERP)       |
+------------------------+------------------------------------------+----------------------------------------+
|  Requisitions          |  Paper, email, verbal, maverick spend    |  Self-Service digital catalog & forms  |
|  Approvals             |  Manual chasing, unrecorded email chains |  Automated DoA rule routing by amount  |
|  Purchase Orders       |  Manual spreadsheets, delayed dispatch   |  Automated PO creation & EDI/Portal    |
|  Goods Receipt         |  Paper dock slips, lost documents        |  Real-time dock receiving against PO   |
|  Invoice Matching      |  Manual paper cross-referencing          |  Automated 2-Way & 3-Way tolerance match|
|  Hold Resolution       |  Chasing via phone/email, payment freeze |  Automated notification worklists      |
|  Disbursements         |  Manual check runs, late-fee exposure    |  Automated batch EFT/ACH runs          |
|  Operational Analytics |  Monthly manual spreadsheet reports      |  Real-time interactive BI dashboards   |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. As-Is Current State Analysis (Pain Points & Bottlenecks)

### Process Narrative
In the legacy operational model at Northstar, when an operational need arose on the plant floor or in maintenance:
1. **Unregulated Intake**: Requesters either filled out a paper requisition form, sent an informal email to a purchasing clerk, or phoned a favored vendor directly without notifying purchasing ("maverick buying").
2. **Approval Chasing**: Requisitions sat on managers' desks for physical signatures or languished in crowded email inboxes. If an approver was traveling or on leave, the procurement request stalled indefinitely, resulting in an average approval latency of 2.5 to 5+ business days.
3. **Manual PO Creation**: Purchasing clerks manually transcribed paper requisition details into disconnected spreadsheets to generate a purchase order number. Orders were often emailed or faxed to vendors days after the requisition was submitted, dragging the total procurement cycle out to ~3.9 days.
4. **Dock Receiving Gaps**: When shipments arrived at the plant docks (Docks A, B, or C), receiving staff stamped a paper delivery docket or packing slip. Dock slips were stored in paper binders. Frequently, delivery receipts were not logged into any central record or were mislaid during shift handovers.
5. **Invoice Inundation & Manual Matching**: Supplier invoices arrived in paper mail or Accounts Payable inboxes. AP clerks manually compared the invoice line items against the PO spreadsheet and phoned the warehouse dock to locate the stamped packing slip.
6. **Exception Traps & Payment Delays**: Over 24.5% of invoices encountered discrepancies:
   - *Missing Receipts*: Dock slips were lost or unrecorded, leading to frozen vouchers.
   - *Price Variances*: Minor freight adjustments or uncoordinated vendor price increases caused prolonged dispute emails between buyers and suppliers.
   - *Payment Delays*: Due to the manual matching backlog, invoices routinely passed their due dates, exposing Northstar to supplier credit holds and forfeited early-payment discounts.

---

## 3. To-Be Standardized Future-State Workflow (10-Step Lifecycle)

The To-Be process establishes an integrated, automated, 10-step lifecycle conceptually aligned with Oracle Fusion Cloud Procurement and Financials:

### Step 1: Requisition Creation via Self-Service Procurement
Operational employees submit purchase requests directly through an intuitive Self-Service Procurement workbench. Requesters select predefined catalog items (with negotiated contract pricing) or fill out guided non-catalog templates. Mandatory fields include cost center, project code, required delivery date, and commodity categorization.

### Step 2: Automated Multi-Tier Approval Routing
Upon submission, the automated approval workflow engine evaluates the requisition against Northstar's Delegation of Authority (DoA) policy:
- **Level 1 ($<\$5,000)**: Routes automatically to the Department Manager.
- **Level 2 ($\$5,000 - \$25,000)**: Routes to the Director of Operations.
- **Level 3 ($>\$25,000)**: Routes to the VP of Finance & Operations / CFO.
- *Rejection Handling*: If rejected, the approver must provide structured feedback in a mandatory justification field, instantly notifying the requester and terminating downstream processing.

### Step 3: Purchase Order Generation & Electronic Issuance
Once fully approved, the system automatically converts the requisition lines into an official Purchase Order (`PO-#####`). Standard catalog orders against active Blanket Purchase Agreements (BPAs) are dispatched electronically (via email/supplier portal) without manual buyer intervention. Complex or non-catalog orders route to the Purchasing Buyer Workbench for commercial terms review before dispatch.

### Step 4: Supplier Fulfillment & Advanced Shipping Notice (ASN)
The supplier fulfills the order according to contractual lead times and agreed packaging specifications. Electronic notifications or packing manifests accompany the shipment.

### Step 5: Real-Time Dock Goods Receiving
Upon shipment arrival at the warehouse dock, receiving clerks access the receiving workbench and query the purchase order number. The clerk records delivered quantities, packaging condition, and dock location.
- **Partial Shipments**: If a vendor delivers 80% of ordered units, the system records the partial quantity, leaves the remaining PO line balance open, and makes the delivered units available for matching.
- **Damaged Shipments**: Items failing inspection are quarantined with an automated Return Material Authorization (RMA) transaction.

### Step 6: Supplier Invoice Ingestion
Invoices are ingested electronically via supplier portal upload, XML data transmission, or automated AP invoice workbench entry. Mandatory validation rules enforce the presence of a valid PO number and supplier identifier. The system immediately checks for and blocks duplicate vendor invoice numbers.

### Step 7: Automated 2-Way and 3-Way Matching Engine
The automated matching engine processes invoice line items against system records:
- **3-Way Matching (Goods & Materials)**: The engine cross-references `PO Quantity & Price` $\leftrightarrow$ `Dock Receipt Quantity` $\leftrightarrow$ `Billed Invoice Quantity & Price`.
- **2-Way Matching (Services & IT Subscriptions)**: For non-physical line items, the engine validates `Billed Invoice Amount & Price` $\leftrightarrow$ `Approved PO Commitment & Line Schedule`.
- **Tolerance Engine Evaluation**: Minor price variances $\le 1.5\%$ or $\le \$50$ (e.g. minor shipping or fuel surcharges) pass automatically under pre-configured business unit tolerances.

### Step 8: Automated Exception Routing & Hold Resolution
Invoices that fail matching rules are systematically tagged with specific hold statuses and routed to designated owners:
- **Hold: Price Variance**: Triggered when invoice unit price exceeds PO unit price beyond the $1.5\%$ tolerance threshold. Routes to the Buyer and AP Supervisor for review (requesting a supplier credit memo or approving a formal price amendment).
- **Hold: Missing Goods Receipt**: Triggered when a physical goods invoice arrives before dock receiving is logged. The system places the voucher on hold and sends an automated task alert to the warehouse dock lead to confirm physical intake.
- **Hold: Quantity Variance**: Triggered when invoiced quantity exceeds dock received quantity. Routes to the supplier liaison to clarify whether backordered items were erroneously billed.
- *Resolution*: Once the hold condition is remedied (dock receipt recorded, price override approved, or credit memo applied), the hold releases automatically.

### Step 9: Payment Scheduling & Automated Disbursement
Validated, hold-free invoices are scheduled for disbursement based on supplier contractual payment terms (e.g., `Net 30`, `Net 45`, `2/10 Net 30`). The system executes an automated Payment Process Request (PPR) batch, aggregating mature invoices and generating electronic payment files (ACH / EFT) with built-in segregation of duties requiring supervisory release. Automated remittance advices are transmitted directly to suppliers.

### Step 10: Governance, Audit Logging & Procurement Analytics
All transactional events—from initial requisition submission to final payment settlement—are recorded in an immutable database audit log. Real-time Oracle Transactional Business Intelligence (OTBI) dashboards provide executive leadership with real-time analytics covering committed PO spend, cash requirements, supplier exception rates, and SLA compliance.

---

## 4. Exception Handling Matrix

| Exception Scenario | Detection Mechanism | Immediate System Action | Resolution Protocol | Target SLA |
| :--- | :--- | :--- | :--- | :--- |
| **Requisition Rejected** | Approver clicks "Reject" in workflow | Workflow halts; status set to `Rejected`; PR cannot convert to PO. | Approver enters mandatory comment; requester amends or cancels PR. | Immediate notification |
| **Price Variance ($> 1.5\%$)** | 3-Way Matching Engine | Invoice placed on `Hold: Price Variance`; payment blocked. | Routed to Buyer; Buyer secures supplier Credit Memo or AP Manager overrides. | $\le 2$ business days |
| **Missing Goods Receipt** | 3-Way Matching Engine | Invoice placed on `Hold: Missing Goods Receipt`; payment blocked. | Alert sent to Dock Lead; dock receipt logged or delivery expedited. | $\le 1$ business day |
| **Quantity Variance (Billed $>$ Received)** | 3-Way Matching Engine | Invoice placed on `Hold: Quantity Variance`; payment blocked. | AP Clerk contacts vendor for corrected invoice or warehouse verifies dock count. | $\le 3$ business days |
| **Duplicate Invoice Submitted** | Invoice Entry Validation | System rejects duplicate entry; raises error alert. | AP Specialist verifies voucher against previously paid records; cancels duplicate. | Immediate rejection |
| **Approver Inactivity ($> 48\text{ hrs}$)** | Workflow Timer Event | Reminder notification sent; auto-escalates after 72 hours. | Request escalates to next-level supervisor or designated peer delegate. | Automatic escalation |
