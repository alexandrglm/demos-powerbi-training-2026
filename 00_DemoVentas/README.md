# DEMO 1 – Sales

The goal of this demo project was to establish the same (or as similar as possible) database to those used in the theoretical examples throughout the [first training](https://github.com/alexandrglm/myLearningCorner/tree/main/BI_DataScience)

It has no intrinsic value as a data model or for its ETL process; rather, its purpose lied in showcasing how to use and represent data using each and every existing type of visual representation object/graphic available.

---

## Data Model Overview

The data model contains no relationships; it consists of a single complete, consolidated table containing all data. 

### Variables & Fields Included:

* **Time Series:** Dates and Years (the table is structured around temporal metrics).
* **Customer Segment:** Target segments for this fictional company (*SMEs, Large Enterprises, Primary Sector / Government, Internal Partners*).
* **Sales Channel:** Online, Distributor, Public Tender, B2B.
* **Product:** Six distinct bicycle models.
* **Discounts Applied:** Non-numeric categories (*High, Low, Medium, None*), each mapped to a corresponding numerical percentage.
* **Units Sold**
* **Manufacturing Cost**
* **Retail Price (RRP)**
* **Discounted Sales Count:** Number of sales transactions that involved discounts.
* **Gross Sales**
* **Net Sales**
* **Cost of Goods Sold (COGS):** Based on manufacturing cost.
* **Delivery Lead Time:** Measured in days.
* **Order Status:** Delivered on time, Delivered with errors, Delayed.
* **Returns:** Whether the order was returned or not.
* **Customer Satisfaction:** NPS ratings scaled from 1 to 5.
* **Payment Terms:** Cash payment for non-deferred orders; installment terms in days for 3 possible options (*1 month, 2 months, 3 months*).
* **Country of Sale:** Various countries across 3 continents.

---

## Structure & Visual Objects Catalogued

Each page contains examples of all visual objects, preceded by an index at the beginning and a summary overview:

### 1. Lists & Data Grids
* **Tables**
* **Matrices**

### 2. Comparative Charts
* **Line Charts**
* **Area Charts**
* **Bar and Column Charts**
* **Clustered Bar and Clustered Column Charts**

### 3. Composition Charts
* **Stacked Bar and Stacked Column Charts**
* **100% Stacked Bar and 100% Stacked Column Charts**
* **Combo / Combo-bar Charts**

### 4. Part-to-Whole Charts
* **Pie Charts**
* **Donut Charts**
* **Funnel Charts**
* **Waterfall Charts**
* **TreeMaps**

### 5. Geographical Charts & Maps
* **Basic / Bubble Maps**
* **Choropleth (Filled) Maps**
* **Shape Maps**

### 6. Dashboards & Scorecards
* **KPIs**
* **Radial Gauge Charts**
* **Cards**
* **Multi-row Cards**

### 7. Other Visuals
* **Ribbon Charts**
* **Scatter Plots**
* **Bubble Scatter Plots**
* **Decomposition Trees**
* **Key Influencers**

---

## Files

Included `.pbix` and `.xlsx` Excel source file used:

* [`Demo-00_PowerBI_Ventas_Decenal.pbix`](./Demo-00_PowerBI_Ventas_Decenal.pbix)
* [`1-3_Transformados_1_Calculados_ifefor_PowerBI_dataset001_ejemplo_MASTER.xlsx`](./1-3_Transformados_1_Calculados_ifefor_PowerBI_dataset001_ejemplo_MASTER.xlsx)


