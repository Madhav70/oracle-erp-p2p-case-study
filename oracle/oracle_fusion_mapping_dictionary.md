# Oracle Fusion Cloud Architecture & Object Mapping Dictionary

**Client Organization**: Northstar Manufacturing Ltd.  
**Target ERP Standard**: **Oracle Fusion Cloud ERP (Procurement & Financials)**  
**Version Alignment**: Oracle Fusion Cloud Applications 24D / 25A  
**Architecture Standard**: Purged legacy EBS terms (AME replaced with Fusion BPM Worklist / AMX)

---

## 1. Terminology Modernization: Fusion Cloud vs. Legacy EBS

To ensure strict alignment with modern Oracle Fusion Cloud ERP standards, the following table clarifies the official Fusion Cloud nomenclature used across all project deliverables:

| Functional Area | Legacy Oracle E-Business Suite (EBS) | Modern Oracle Fusion Cloud ERP (Target) |
| :--- | :--- | :--- |
| **Approval Routing** | Approvals Management Engine (AME) | **Oracle Fusion BPM Worklist / Human Workflow (BPM / AMX)** |
| **Procurement Intake** | iProcurement | **Oracle Self-Service Procurement Cloud** |
| **PO Management** | Core Purchasing (PO Forms) | **Oracle Purchasing Cloud & Buyer Work Center** |
| **Dock Receiving** | Oracle Inventory Receiving Forms | **Oracle Receiving Cloud / Inventory Management** |
| **Payables Matching** | Payables Match Window (APXINWKB) | **Oracle Payables Cloud & Matching Engine Worklist** |
| **Operational Analytics** | Discoverer / Standard Reports | **Oracle Transactional Business Intelligence (OTBI)** |

---

## 2. Dataset to Oracle Fusion Cloud Schema Mapping

Every entity and column in the synthetic datasets maps directly to the underlying Oracle Fusion Cloud database tables and REST API resources:

### 2.1 Suppliers (`suppliers.csv`)
* **Oracle Fusion Cloud Physical Tables**: `POZ_SUPPLIERS`, `POZ_SUPPLIER_SITES_ALL_M`
* **Fusion REST API Resource**: `/fscmRestApi/resources/11.13.18.05/suppliers`

| CSV Field Name | Oracle Fusion Cloud Column | Data Type | Business Description |
| :--- | :--- | :--- | :--- |
| `supplier_id` | `POZ_SUPPLIERS.SEGMENT1` | VARCHAR2(30) | Vendor identification number |
| `supplier_name` | `POZ_SUPPLIERS.VENDOR_NAME` | VARCHAR2(360) | Legal operating vendor name |
| `category` | `POZ_SUPPLIERS.BUSINESS_RELATIONSHIP` | VARCHAR2(30) | Commodity spend categorization |
| `payment_terms` | `POZ_SUPPLIER_SITES_ALL_M.TERMS_NAME`| VARCHAR2(50) | Contractual settlement terms |
| `lead_time_days`| `POZ_SUPPLIER_SITES_ALL_M.LEAD_TIME` | NUMBER | Vendor fulfillment latency in days |
| `is_active` | `POZ_SUPPLIERS.ENABLED_FLAG` | VARCHAR2(1) | Master record activation flag (Y/N) |

---

### 2.2 Requisitions (`requisitions.csv`)
* **Oracle Fusion Cloud Physical Tables**: `POR_REQUISITION_HEADERS_ALL`, `POR_REQUISITION_LINES_ALL`
* **Fusion REST API Resource**: `/fscmRestApi/resources/11.13.18.05/purchaseRequisitions`

| CSV Field Name | Oracle Fusion Cloud Column | Data Type | Business Description |
| :--- | :--- | :--- | :--- |
| `pr_id` | `POR_REQUISITION_HEADERS_ALL.REQUISITION_NUMBER` | VARCHAR2(64) | Requisition document reference |
| `pr_date` | `POR_REQUISITION_HEADERS_ALL.CREATION_DATE` | TIMESTAMP | Requisition entry timestamp |
| `requester_name`| `POR_REQUISITION_HEADERS_ALL.PREPARER_ID` | NUMBER(18) | Employee ID of request originator |
| `estimated_amount`| `POR_REQUISITION_LINES_ALL.AMOUNT` | NUMBER | Total estimated requisition commitment |
| `approval_status`| `POR_REQUISITION_HEADERS_ALL.DOCUMENT_STATUS` | VARCHAR2(30) | Fusion status: APPROVED, REJECTED, IN_PROCESS |
| `approver` | `POR_REQUISITION_HEADERS_ALL.LAST_APPROVED_BY`| NUMBER(18) | BPM Worklist assigned approver |

---

### 2.3 Purchase Orders (`purchase_orders.csv`)
* **Oracle Fusion Cloud Physical Tables**: `PO_HEADERS_ALL`, `PO_LINES_ALL`, `PO_LINE_LOCATIONS_ALL`
* **Fusion REST API Resource**: `/fscmRestApi/resources/11.13.18.05/purchaseOrders`

| CSV Field Name | Oracle Fusion Cloud Column | Data Type | Business Description |
| :--- | :--- | :--- | :--- |
| `po_id` | `PO_HEADERS_ALL.SEGMENT1` | VARCHAR2(30) | Purchase order unique identifier |
| `pr_id` | `PO_LINES_ALL.REQUISITION_NUMBER` | VARCHAR2(64) | Parent requisition traceability reference |
| `supplier_id` | `PO_HEADERS_ALL.VENDOR_ID` | NUMBER(18) | Supplier master foreign key |
| `buyer_name` | `PO_HEADERS_ALL.AGENT_ID` | NUMBER(18) | Assigned procurement specialist |
| `po_date` | `PO_HEADERS_ALL.SUBMIT_DATE` | TIMESTAMP | Order issuance timestamp |
| `po_amount` | `PO_HEADERS_ALL.APPROVED_AMOUNT` | NUMBER | Committed contractual order value |
| `matching_type` | `PO_LINE_LOCATIONS_ALL.MATCH_OPTION` | VARCHAR2(25) | P (Purchase Order / 2-Way) or R (Receipt / 3-Way) |
| `po_status` | `PO_HEADERS_ALL.DOCUMENT_STATUS` | VARCHAR2(30) | Lifecycle state: OPEN, CLOSED, IN_PROCESS |

---

### 2.4 Receipts (`receipts.csv`)
* **Oracle Fusion Cloud Physical Tables**: `RCV_SHIPMENT_HEADERS`, `RCV_SHIPMENT_LINES`, `RCV_TRANSACTIONS`
* **Fusion REST API Resource**: `/fscmRestApi/resources/11.13.18.05/receivingReceiptRequests`

| CSV Field Name | Oracle Fusion Cloud Column | Data Type | Business Description |
| :--- | :--- | :--- | :--- |
| `receipt_id` | `RCV_SHIPMENT_HEADERS.RECEIPT_NUM` | VARCHAR2(30) | Dock intake receiving slip number |
| `po_id` | `RCV_TRANSACTIONS.PO_HEADER_ID` | NUMBER(18) | Associated purchase order foreign key |
| `receipt_date` | `RCV_TRANSACTIONS.TRANSACTION_DATE` | TIMESTAMP | Warehouse dock intake timestamp |
| `receiving_clerk`| `RCV_SHIPMENT_HEADERS.EMPLOYEE_ID` | NUMBER(18) | Warehouse clerk recording delivery |
| `received_qty_pct`| `RCV_TRANSACTIONS.QUANTITY` | NUMBER | Physical units accepted at dock |
| `inspection_status`| `RCV_TRANSACTIONS.INSPECTION_STATUS_CODE`| VARCHAR2(30) | ACCEPTED, REJECTED, PARTIAL |

---

### 2.5 Invoices & Holds (`invoices.csv`)
* **Oracle Fusion Cloud Physical Tables**: `AP_INVOICES_ALL`, `AP_INVOICE_LINES_ALL`, `AP_HOLDS_ALL`, `AP_HOLD_CODES`
* **Fusion REST API Resource**: `/fscmRestApi/resources/11.13.18.05/invoices`

| CSV Field Name | Oracle Fusion Cloud Column | Data Type | Business Description |
| :--- | :--- | :--- | :--- |
| `invoice_id` | `AP_INVOICES_ALL.INVOICE_NUM` | VARCHAR2(50) | Accounts Payable voucher number |
| `po_id` | `AP_INVOICE_LINES_ALL.PO_HEADER_ID` | NUMBER(18) | Referenced PO commitment |
| `invoice_amount`| `AP_INVOICES_ALL.INVOICE_AMOUNT` | NUMBER | Total billed liability payable |
| `due_date` | `AP_INVOICES_ALL.PAYMENT_DUE_DATE` | DATE | Scheduled payment maturity date |
| `match_status` | `AP_HOLDS_ALL.HOLD_LOOKUP_CODE` | VARCHAR2(30) | Standard Fusion Hold Codes: `PRICE VARIANCE`, `QTY ORD`, `NO REC` |
| `payment_status`| `AP_INVOICES_ALL.PAYMENT_STATUS_FLAG` | VARCHAR2(1) | Y (Fully Paid), N (Unpaid), P (Partial) |
| `paid_date` | `AP_INVOICES_ALL.PAID_DATE` | DATE | Disbursement execution date |
| `payment_reference`| `AP_INVOICES_ALL.CHECK_NUMBER` | VARCHAR2(100) | Commercial banking settlement trace (ACH/EFT) |
