import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('Ecommerce_Dataset_20K.xlsx')

print("28. Plot a bar chart of total Net Revenue by Main Category")

import matplotlib.pyplot as plt

cat_rev = df.groupby('Main Category')['Net Revenue (₹)'].sum()
cat_rev.plot(kind='bar', color='steelblue')
plt.title('Revenue by Category')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.show()

print("29.Plot a histogram of Customer Age distribution")

plt.hist(df['Customer Age'], bins=20, color='green', edgecolor='black')
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

print("30.Create a pie chart of orders by Payment Method")

pay = df['Payment Method'].value_counts()
plt.pie(pay, labels=pay.index, autopct='%1.1f%%')
plt.title('Orders by Payment Method')
plt.show()

print("31.Scatter plot of Unit Price vs Net Revenue colored by Main Category")
# import seaborn as sns

plt.scatter(df['Unit Price (₹)'], df['Net Revenue (₹)'], alpha=0.3, color='orange')
plt.title('Unit Price vs Net Revenue')
plt.xlabel('Unit Price')
plt.ylabel('Net Revenue')
plt.show()

print("32.Plot a heatmap of correlation between numerical columns")

import seaborn as sns

nums = df.select_dtypes(include='number')
sns.heatmap(nums.corr(), cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

print("33.Create a boxplot of Net Revenue by Customer Segment")
sns.boxplot(data=df, x='Customer Segment', y='Net Revenue (₹)')
plt.title('Revenue by Customer Segment')
plt.xticks(rotation=30)
plt.show()

print("34.Display summary statistics for all numerical columns")
print(df.describe().round(2))

print("35.Find the month with highest total Net Revenue")

df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Month_Year'] = df['Order Date'].dt.to_period('M')
best_month = df.groupby('Month_Year')['Net Revenue (₹)'].sum().idxmax()
print("Best Month:", best_month)

print("36.Calculate the Return Rate (% of orders with Return Requested = Yes)")
return_rate = (df['Return Requested'] == 'Yes').sum() / len(df) * 100
print(f"Return Rate: {return_rate:.2f}%")

print("37.Find correlation between Review Score and Order Satisfaction")
corr = df['Review Score'].corr(df['Order Satisfaction'])
print(f"Correlation: {corr:.4f}")

print("38.Find the top 3 states by number of orders placed")
top_states = df['Shipping State'].value_counts().head(3)
print(top_states)

print("39.Export filtered Electronics orders to a CSV file")
electronics = df[df['Main Category'] == 'Electronics']
electronics.to_csv('electronics_orders.csv', index=False)
print("File saved!")

print("40.Export a grouped summary report to a new Excel file")
summary = df.groupby('Main Category').agg(
    Total_Orders=('Order ID', 'count'),
    Total_Revenue=('Net Revenue (₹)', 'sum'),
    Avg_Margin=('Profit Margin %', 'mean')
).reset_index()

summary.to_excel('category_summary_report.xlsx', index=False)
print("Report exported!")



























