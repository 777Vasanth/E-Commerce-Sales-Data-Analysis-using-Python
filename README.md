# E-Commerce Sales Data Analysis using Python

## Project Overview
This project focuses on analyzing a large-scale E-Commerce dataset containing 20,000+ customer orders using Python. The objective of this analysis is to discover revenue trends, customer purchasing behavior, payment preferences, profitability insights, and customer segmentation patterns through Exploratory Data Analysis (EDA) and data visualization techniques.

The project also includes automated report generation and exporting filtered datasets into CSV and Excel formats.

---

# Objectives
- Analyze revenue across product categories
- Understand customer demographics and behavior
- Identify popular payment methods
- Study profitability and revenue relationships
- Compare customer segments based on spending patterns
- Perform correlation analysis on numerical features
- Generate automated business summary reports

---

# Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Excel Dataset

---

# Dataset Information
The dataset contains:
- Customer Details
- Product Information
- Revenue and Profit Data
- Payment Methods
- Ratings and Satisfaction Scores
- Delivery Information
- Return Request Details

Total Records: 20,000+

---

# Analysis Performed

## Revenue Analysis
- Total Net Revenue by Main Category
- Highest Revenue Generating Month
- Revenue Distribution by Customer Segment

## Customer Analysis
- Customer Age Distribution
- Customer Segment Comparison
- Review Score and Satisfaction Correlation

## Payment Analysis
- Orders by Payment Method
- EMI Usage Analysis

## Product and Pricing Analysis
- Unit Price vs Net Revenue Relationship
- Profit Margin Analysis
- Correlation Heatmap of Numerical Features

## Reporting
- Exported Electronics Orders to CSV
- Generated Category Summary Excel Report

---

# Key Insights
- Electronics category generated the highest overall revenue.
- UPI was the most preferred payment method among customers.
- Premium and VIP customers contributed higher median revenue.
- Positive correlation observed between Review Score and Order Satisfaction.
- Higher unit prices generally resulted in increased Net Revenue.
- Certain customer segments showed significantly higher purchasing behavior.

---

# Visualizations Included
- Bar Chart
- Histogram
- Pie Chart
- Scatter Plot
- Heatmap
- Boxplot

---

# Project Structure

```text
ecommerce-sales-analysis/
│
├── data/
│   └── Ecommerce_Dataset_20K.xlsx
│
├── notebook/
│   └── ecommerce_analysis.ipynb
│
├── outputs/
│   ├── revenue_by_category.png
│   ├── customer_age_distribution.png
│   ├── payment_method_analysis.png
│   ├── correlation_heatmap.png
│   └── revenue_segment_boxplot.png
│
├── reports/
│   ├── electronics_orders.csv
│   └── category_summary_report.xlsx
│
└── README.md
```

---

# Sample Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# Future Improvements
- Build an interactive Power BI dashboard
- Add machine learning sales prediction
- Deploy analysis as a web application
- Perform customer churn prediction
- Add advanced KPI dashboards

---

# Author
Vasanth
