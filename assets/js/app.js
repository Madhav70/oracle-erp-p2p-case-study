/**
 * Northstar Manufacturing Ltd. - Oracle ERP P2P Implementation Case Study
 * Interactive Application Engine (app.js)
 */

document.addEventListener('DOMContentLoaded', () => {
    initTabs();
    initAccordions();
    initRequirementsFilter();
    initRiskFilter();
    initTransactionTable();
    initSmoothScroll();
});

/* ==========================================================================
   1. Tab Navigation System
   ========================================================================== */
function initTabs() {
    const tabHeaders = document.querySelectorAll('.tabs-header');
    
    tabHeaders.forEach(header => {
        const buttons = header.querySelectorAll('.tab-btn');
        const container = header.parentElement;
        const panes = container.querySelectorAll('.tab-pane');
        
        buttons.forEach(btn => {
            btn.addEventListener('click', () => {
                const targetId = btn.getAttribute('data-target');
                
                buttons.forEach(b => b.classList.remove('active'));
                panes.forEach(p => p.classList.remove('active'));
                
                btn.classList.add('active');
                const targetPane = container.querySelector(`#${targetId}`);
                if (targetPane) {
                    targetPane.classList.add('active');
                }
            });
        });
    });
}

/* ==========================================================================
   2. Accordions (Glossary & Deep-Dive Notes)
   ========================================================================== */
function initAccordions() {
    const accordionTriggers = document.querySelectorAll('.accordion-trigger');
    
    accordionTriggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const item = trigger.parentElement;
            const isOpen = item.classList.contains('open');
            
            // Toggle current
            if (isOpen) {
                item.classList.remove('open');
            } else {
                item.classList.add('open');
            }
        });
    });
}

/* ==========================================================================
   3. Searchable Requirements Table
   ========================================================================== */
function initRequirementsFilter() {
    const searchInput = document.getElementById('reqSearchInput');
    const priorityFilter = document.getElementById('reqPriorityFilter');
    const tableBody = document.getElementById('requirementsTableBody');
    
    if (!searchInput || !tableBody) return;
    
    function filterRows() {
        const query = searchInput.value.toLowerCase().trim();
        const selectedPriority = priorityFilter ? priorityFilter.value : 'ALL';
        const rows = tableBody.querySelectorAll('tr');
        let visibleCount = 0;
        
        rows.forEach(row => {
            const text = row.textContent.toLowerCase();
            const priority = row.getAttribute('data-priority') || '';
            
            const matchesQuery = query === '' || text.includes(query);
            const matchesPriority = selectedPriority === 'ALL' || priority === selectedPriority;
            
            if (matchesQuery && matchesPriority) {
                row.style.display = '';
                visibleCount++;
            } else {
                row.style.display = 'none';
            }
        });
        
        const countSpan = document.getElementById('reqMatchCount');
        if (countSpan) {
            countSpan.textContent = `${visibleCount} requirements shown`;
        }
    }
    
    searchInput.addEventListener('input', filterRows);
    if (priorityFilter) {
        priorityFilter.addEventListener('change', filterRows);
    }
}

/* ==========================================================================
   4. Filterable Risk Register
   ========================================================================== */
function initRiskFilter() {
    const searchInput = document.getElementById('riskSearchInput');
    const categoryFilter = document.getElementById('riskCategoryFilter');
    const severityFilter = document.getElementById('riskSeverityFilter');
    const tableBody = document.getElementById('riskTableBody');
    
    if (!searchInput || !tableBody) return;
    
    function filterRisks() {
        const query = searchInput.value.toLowerCase().trim();
        const selectedCat = categoryFilter ? categoryFilter.value : 'ALL';
        const selectedSev = severityFilter ? severityFilter.value : 'ALL';
        const rows = tableBody.querySelectorAll('tr');
        let visibleCount = 0;
        
        rows.forEach(row => {
            const text = row.textContent.toLowerCase();
            const cat = row.getAttribute('data-category') || '';
            const sev = row.getAttribute('data-severity') || '';
            
            const matchesQuery = query === '' || text.includes(query);
            const matchesCat = selectedCat === 'ALL' || cat === selectedCat;
            const matchesSev = selectedSev === 'ALL' || sev === selectedSev;
            
            if (matchesQuery && matchesCat && matchesSev) {
                row.style.display = '';
                visibleCount++;
            } else {
                row.style.display = 'none';
            }
        });
        
        const countSpan = document.getElementById('riskMatchCount');
        if (countSpan) {
            countSpan.textContent = `${visibleCount} risks displayed`;
        }
    }
    
    searchInput.addEventListener('input', filterRisks);
    if (categoryFilter) categoryFilter.addEventListener('change', filterRisks);
    if (severityFilter) severityFilter.addEventListener('change', filterRisks);
}

/* ==========================================================================
   5. Interactive Sample Transactions Table
   ========================================================================== */
const SAMPLE_TRANSACTIONS = [
    { id: "INV-40001", po: "PO-20001", sup: "ByteCloud Software Solutions", type: "2-Way Match", amt: 2058.04, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-528107" },
    { id: "INV-40002", po: "PO-20002", sup: "Ironclad Safety Gear Co", type: "3-Way Match", amt: 3698.28, status: "Matched (Within Tolerance)", hold: "Minor freight (+$48.37)", payStatus: "Paid", ref: "ACH-764995" },
    { id: "INV-40003", po: "PO-20003", sup: "CleanRoom Janitorial Supplies", type: "2-Way Match", amt: 1040.56, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-872319" },
    { id: "INV-40004", po: "PO-20004", sup: "Crestview Facilities Management", type: "2-Way Match", amt: 8901.55, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-516179" },
    { id: "INV-40005", po: "PO-20005", sup: "Ironclad Safety Gear Co", type: "3-Way Match", amt: 16690.27, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-651346" },
    { id: "INV-40006", po: "PO-20006", sup: "Solenoid Systems Corp", type: "3-Way Match", amt: 5242.28, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-559355" },
    { id: "INV-40007", po: "PO-20007", sup: "Kinetics Lubricants Inc", type: "3-Way Match", amt: 1516.53, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-896773" },
    { id: "INV-40008", po: "PO-20009", sup: "Starlight Industrial Gas", type: "3-Way Match", amt: 3889.10, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-935196" },
    { id: "INV-40009", po: "PO-20010", sup: "Crestview Facilities Management", type: "2-Way Match", amt: 11225.64, status: "Hold: Price Variance", hold: "Exceeds PO by +4.3% (+$458.45)", payStatus: "Paid (Override)", ref: "EFT-952040" },
    { id: "INV-40010", po: "PO-20011", sup: "Ironclad Safety Gear Co", type: "3-Way Match", amt: 10526.23, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-624227" },
    { id: "INV-40011", po: "PO-20012", sup: "Fleetlink Transport Services", type: "2-Way Match", amt: 9027.25, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-951437" },
    { id: "INV-40012", po: "PO-20013", sup: "Matrix Information Technologies", type: "2-Way Match", amt: 24469.96, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-572999" },
    { id: "INV-40013", po: "PO-20014", sup: "Vanguard Security Services", type: "2-Way Match", amt: 8423.69, status: "Matched (Within Tolerance)", hold: "Freight line (+$30.65)", payStatus: "Paid", ref: "ACH-779068" },
    { id: "INV-40014", po: "PO-20015", sup: "Quantum Sensor Tech", type: "3-Way Match", amt: 8408.96, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-640164" },
    { id: "INV-40015", po: "PO-20016", sup: "Ironclad Safety Gear Co", type: "3-Way Match", amt: 10185.73, status: "Hold: Missing Goods Receipt", hold: "Dock receipt not logged at entry", payStatus: "Approved for Payment", ref: "EFT-893265" },
    { id: "INV-40016", po: "PO-20017", sup: "Pinnacle Corrugated Boxes", type: "3-Way Match", amt: 21043.16, status: "Hold: Missing Goods Receipt", hold: "Dock receipt not logged at entry", payStatus: "Approved for Payment", ref: "EFT-569568" },
    { id: "INV-40017", po: "PO-20018", sup: "Vanguard Security Services", type: "2-Way Match", amt: 2013.69, status: "Matched (Within Tolerance)", hold: "Tolerance pass (+$23.92)", payStatus: "Paid", ref: "ACH-854541" },
    { id: "INV-40018", po: "PO-20019", sup: "Matrix Information Technologies", type: "2-Way Match", amt: 31711.32, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-829154" },
    { id: "INV-40019", po: "PO-20020", sup: "Dynamic Pneumatics Ltd", type: "3-Way Match", amt: 14442.40, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-893112" },
    { id: "INV-40020", po: "PO-20021", sup: "Titan Bearings & Drives", type: "3-Way Match", amt: 5142.21, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-501296" },
    { id: "INV-40021", po: "PO-20022", sup: "Solenoid Systems Corp", type: "3-Way Match", amt: 12178.85, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-865580" },
    { id: "INV-40022", po: "PO-20023", sup: "ByteCloud Software Solutions", type: "2-Way Match", amt: 24713.59, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-614205" },
    { id: "INV-40023", po: "PO-20024", sup: "Benchmark Electricals Ltd", type: "3-Way Match", amt: 3746.49, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-648684" },
    { id: "INV-40024", po: "PO-20025", sup: "Matrix Information Technologies", type: "2-Way Match", amt: 33797.84, status: "Matched", hold: "None", payStatus: "Paid", ref: "ACH-754456" }
];

function initTransactionTable() {
    const tableBody = document.getElementById('txTableBody');
    const searchInput = document.getElementById('txSearchInput');
    const statusFilter = document.getElementById('txStatusFilter');
    const countDisplay = document.getElementById('txMatchCount');
    
    if (!tableBody || !searchInput) return;
    
    function render(data) {
        tableBody.innerHTML = '';
        if (data.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="8" style="text-align: center; color: var(--neutral-600); padding: 2rem;">No matching transaction vouchers found.</td></tr>`;
            if (countDisplay) countDisplay.textContent = '0 records found';
            return;
        }
        
        data.forEach(item => {
            const tr = document.createElement('tr');
            
            let statusBadge = 'badge-success';
            if (item.status.includes('Hold: Price')) statusBadge = 'badge-warning';
            else if (item.status.includes('Hold: Missing')) statusBadge = 'badge-danger';
            else if (item.status.includes('Tolerance')) statusBadge = 'badge-info';
            
            tr.innerHTML = `
                <td><strong>${item.id}</strong></td>
                <td><code>${item.po}</code></td>
                <td>${item.sup}</td>
                <td><span class="badge badge-neutral">${item.type}</span></td>
                <td><strong>$${item.amt.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</strong></td>
                <td><span class="badge ${statusBadge}">${item.status}</span></td>
                <td style="font-size: 0.8rem; color: var(--neutral-600);">${item.hold}</td>
                <td><span class="badge ${item.payStatus.includes('Paid') ? 'badge-success' : 'badge-warning'}">${item.payStatus}</span></td>
            `;
            tableBody.appendChild(tr);
        });
        
        if (countDisplay) countDisplay.textContent = `${data.length} records displayed`;
    }
    
    function filterData() {
        const query = searchInput.value.toLowerCase().trim();
        const selectedStatus = statusFilter ? statusFilter.value : 'ALL';
        
        const filtered = SAMPLE_TRANSACTIONS.filter(item => {
            const matchText = (item.id + ' ' + item.po + ' ' + item.sup + ' ' + item.ref).toLowerCase();
            const matchesQuery = query === '' || matchText.includes(query);
            
            let matchesStatus = true;
            if (selectedStatus === 'MATCHED') matchesStatus = item.status.startsWith('Matched');
            else if (selectedStatus === 'HOLD_PRICE') matchesStatus = item.status.includes('Price');
            else if (selectedStatus === 'HOLD_RECEIPT') matchesStatus = item.status.includes('Missing');
            else if (selectedStatus === 'PAID') matchesStatus = item.payStatus.includes('Paid');
            
            return matchesQuery && matchesStatus;
        });
        
        render(filtered);
    }
    
    searchInput.addEventListener('input', filterData);
    if (statusFilter) statusFilter.addEventListener('change', filterData);
    
    // Initial Render
    render(SAMPLE_TRANSACTIONS);
}

/* ==========================================================================
   6. Smooth Scrolling & Active Nav Highlighting
   ========================================================================== */
function initSmoothScroll() {
    const navLinks = document.querySelectorAll('.nav-links a');
    
    window.addEventListener('scroll', () => {
        let current = '';
        const sections = document.querySelectorAll('section[id]');
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            if (window.scrollY >= sectionTop) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
}
