# E-Commerce Customer & Order Analytics

## Project Overview

E-Commerce Customer & Order Analytics is a data analytics project that explores customer behavior, sales performance, product categories, marketing channels, discounts, returns, and delivery operations.

The project uses Python and Pandas for data cleaning, preprocessing, feature engineering, and exploratory data analysis (EDA). Power BI is used to create an interactive dashboard that presents business insights through KPIs, charts, and filters.

The goal is to understand how sales are performing, which customer and product segments contribute to business performance, and where operational improvements may be needed.

## Tools & Technologies

- **Python** — Data analysis and preprocessing
- **Pandas** — Data cleaning and manipulation
- **NumPy** — Numerical operations
- **VS Code** — Python development environment
- **Power BI Desktop** — Interactive dashboard development
- **CSV** — Dataset storage

## Dataset Overview

- **Dataset:** E-Commerce Customer & Order Analytics
- **Records:** 35,000 rows
- **Columns:** 23
- **Format:** CSV

The dataset contains information about orders, customers, products, payments, discounts, shipping, returns, ratings, and marketing channels.

### Important Columns

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Customer_ID | Customer identifier |
| Order_Date | Date of the order |
| Product_Category | Product category |
| Product_Name | Product name |
| Quantity | Number of units ordered |
| Unit_Price | Price per unit |
| Discount_Percent | Discount applied |
| Shipping_Cost | Shipping expense |
| Payment_Method | Payment method |
| Order_Status | Current order status |
| Delivery_Days | Delivery duration |
| Customer_Age | Customer age |
| Customer_Gender | Customer gender |
| City | Customer city |
| Region | Customer region |
| Customer_Type | Customer segment |
| Rating | Customer rating |
| Marketing_Channel | Channel associated with the order |
| Coupon_Used | Coupon usage information |
| Return_Flag | Indicates whether an order was returned |
| Order_Value | Recorded order value |

## Project Objectives

- Analyze overall sales performance.
- Identify top-performing product categories and products.
- Understand monthly sales trends.
- Analyze customer purchasing behavior.
- Compare sales across cities and regions.
- Evaluate marketing channel performance.
- Investigate the effect of discounts and coupon usage.
- Analyze order returns, delivery times, and customer ratings.
- Present key findings in an interactive Power BI dashboard.

## Python Data Cleaning & EDA

Python was used in VS Code to prepare the dataset for analysis.

### 1. Data Loading

Loaded the original CSV file into a Pandas DataFrame.

### 2. Data Inspection

- Checked dataset dimensions.
- Reviewed column names and data types.
- Identified missing values and calculated missing-value percentages.
- Checked duplicate records.
- Inspected important columns for data quality issues.

### 3. Data Cleaning

- Handled missing values using appropriate strategies.
- Used suitable replacement values for selected categorical columns.
- Used median or other appropriate values for selected numerical columns.
- Checked duplicate orders using the order identifier.
- Converted the order date column to datetime format.
- Standardized the dataset for further analysis.

### 4. Feature Engineering

Created additional analytical fields to support business analysis, including:

- Gross sales
- Discount amount
- Net sales
- Estimated profit, where applicable
- Delivery category
- Customer age group
- Month and year

These fields help analyze sales performance, customer segments, and operational trends.

### 5. Exploratory Data Analysis

Explored the dataset to answer business questions about:

- Monthly sales performance.
- Product and category contribution.
- Customer purchasing patterns.
- Regional sales distribution.
- Marketing channel performance.
- Discount and coupon usage.
- Return behavior.
- Delivery duration and customer ratings.

## Power BI Dashboard

The Power BI dashboard is organized into three pages.

### Page 1 — Business Overview

Provides a high-level summary of business performance.
<img width="934" height="552" alt="business_overview" src="https://github.com/user-attachments/assets/7c56136c-3f67-47cd-9d5e-61f437a6854e" />

Key areas:
- Total sales
- Total orders
- Customer count
- Average order value
- Monthly sales trends
- Sales distribution by product category
- Regional performance

### Page 2 — Sales & Product Analysis

Focuses on product performance and sales trends.
<img width="935" height="548" alt="sales_product_analysis" src="https://github.com/user-attachments/assets/43cd9e6b-493a-44da-9526-5f6a51a72528" />

Key areas:
- Sales by product category
- Top-performing products
- Monthly sales analysis
- Regional and city-level sales
- Marketing channel performance
- Discount and coupon analysis

### Page 3 — Customer & Operations Analysis

Focuses on customer behavior and order operations.
<img width="935" height="548" alt="sales_product_analysis" src="https://github.com/user-attachments/assets/f1d12128-5582-41cc-b9d9-a1a3a15ab43c" />


Key areas:
- Customer segment analysis
- Returning customer behavior
- Order returns
- Delivery performance
- Customer ratings
- Payment method distribution

The dashboard supports interactive exploration using slicers and visual interactions.

## Business Questions

This project explores questions such as:

1. How do sales change from month to month?
2. Which product categories contribute the most sales?
3. Which products perform best?
4. Which cities and regions generate higher sales?
5. Which marketing channels are associated with stronger sales?
6. How do discounts and coupons relate to average order value?
7. What proportion of customers place repeat orders?
8. What is the order return rate?
9. How do delivery times vary across orders?
10. How do customer ratings vary across products or categories?

## Business Value

The analysis can help businesses:

- Monitor sales performance and trends.
- Identify strong and weak product categories.
- Understand customer purchasing behavior.
- Evaluate marketing channel performance.
- Review discount and coupon usage.
- Monitor returns and delivery performance.
- Support data-driven decisions about sales and customer operations.

## Project Structure

```text
## Project Structure

```text
E-Commerce-Customer-Order-Analytics/
│
├── README.md
├── requirements.txt
├── sales.py
│
├── data/
│   └── ecommerce_datasets.zip
│
├── powerbi/
│   └── ecommerce_customer_order_analytics.pbix
│
└── screenshots/
    ├── business_overview.png
    ├── sales_product_analysis.png
    └── customer_operations_analysis.png
```

## How to Run the Python Analysis

### Step 1 — Install the Required Libraries

Open the VS Code terminal and run:

```bash
pip install -r requirements.txt
```

### Step 2 — Check the Project Files

Keep `sales.py` and the original dataset in the appropriate locations. If the CSV is stored in a different folder, update the file path in the Python script.

### Step 3 — Run the Python Script

```bash
python sales.py
```

The script performs the data preparation and analysis implemented in the Python file.

### Step 4 — Open the Power BI Dashboard

Open the `.pbix` file in Power BI Desktop to explore the dashboard and its available filters.

## Skills Demonstrated

- Python programming
- Pandas data cleaning
- Missing-value handling
- Duplicate detection
- Data type conversion
- Feature engineering
- Exploratory data analysis
- Customer and product analytics
- Sales and marketing analysis
- Power BI dashboard development
- Data visualization
- Business insight communication

## Conclusion

The E-Commerce Customer & Order Analytics project demonstrates an end-to-end analytics workflow, from raw data preparation in Python to interactive reporting in Power BI. It combines customer, product, sales, marketing, and operational analysis to help translate business data into useful insights.
