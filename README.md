# Manufacturing Quality & Defect Intelligence Dashboard

## 1. Business Problem

In precision manufacturing and industrial assembly, undetected spikes in component defect rates lead to substantial scrap costs, rework bottlenecks, and delayed customer deliveries. Operations managers often rely on static, fragmented production logs that obscure **which supplier, shift, or product line** is driving quality degradation until end-of-quarter financial reviews.

**Objective:** Design an automated, interactive Business Intelligence solution to monitor plant-wide defect rates, quantify financial scrap impact in real time, and pinpoint root-cause anomalies across shifts and suppliers.

## 2. Solution Architecture & Tech Stack

This project simulates an end-to-end industrial analytics workflow using 100% synthetic operational data:

**Data Generation (`Python`, `pandas`, `numpy`):** Built a reproducible script (`generate_quality_data.py`) simulating 5,000 production batches across 12 months, covering 4 mechanical product lines, 3 shifts, and 3 external suppliers—with a realistic Q3 operational anomaly injected into the dataset.

**Data Modeling & Analytics (`Power BI`, `DAX`):** Structured a clean reporting model with custom DAX measures (`Defect Rate (%)`, `Scrap Cost ($)`, `MoM Defect Rate`) to ensure accurate dynamic filtering across time horizons and production segments.

**Executive Visualization:** Designed a two-page Power BI report separating high-level executive KPIs from granular root-cause diagnostics.

## 3. Key Analytical Findings

Analyzing the FY 2025 production dataset (621,000 total units produced) uncovered the following actionable insights:

1. **Overall Quality Baseline vs. Q3 Spike:** While the plant maintained a baseline defect rate of \~2.5% throughout Q1, Q2, and Q4, overall defects spiked sharply in **Q3 (July–September)**, pushing the annual defect rate to **2.75%** and total scrap cost to **\$2.71M**.

2. **Primary Failure Mode:** **Dimensional Errors** accounted for the highest volume of defective units (\~6.1K units), followed by **Surface Finish** issues (\~5.0K units).

3. **Root-Cause Isolation (Supplier & Shift Matrix):** Drilling down by supplier and shift revealed that **Supplier Beta** experienced a **6.51% defect rate during the Night Shift** (more than double the plant average), specifically driven by dimensional tolerances drifting out of specification during Q3.

## 4. Dashboard Preview

### Page 1: Executive Quality Overview

*Tracks total production volume, plant-wide defect rate, financial scrap impact, monthly defect trends, and Pareto failure categories.*

### Page 2: Supplier & Shift Root-Cause Diagnostic

*Enables operations and supplier quality engineers to filter by product line and date range to isolate shift-level and vendor-specific bottlenecks.*

## 5. Repository Structure

```text
├── assets/
│   ├── executive_overview.png       # High-res screenshot of Page 1
│   └── root_cause_diagnostic.png    # High-res screenshot of Page 2
├── generate_quality_data.py         # Python script to generate synthetic production data
├── manufacturing_quality_data.csv   # Generated dataset (5,000 batch records)
├── Manufacturing_Quality_BI.pbix    # Interactive Power BI Desktop report
└── README.md                        # Project documentation

```

## 6. How to Reproduce

1. **Regenerate Dataset (Optional):**

   ```bash
   python3 generate_quality_data.py
   
   ```

2. **Explore the Dashboard:**
   Open `Manufacturing_Quality_BI.pbix` in **Power BI Desktop** (free version) to interact with the date sliders, product line filters, and cross-filtering visuals.

*Note: All datasets, supplier names, and financial figures in this repository are entirely synthetic and created for portfolio demonstration purposes.*