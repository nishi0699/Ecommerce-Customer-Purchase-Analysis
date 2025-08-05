# E-commerce Data Analysis Project

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("ecommerce_sales_data.csv")

# Data Cleaning
# Check for missing values
print(df.isnull().sum())

# Convert 'OrderDate' to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Create new column for Month
df['Month'] = df['OrderDate'].dt.to_period('M')

# Drop duplicates if any
df.drop_duplicates(inplace=True)

# Exploratory Data Analysis
# ----------------------
# Top-selling products
top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print("Top-selling products:\n", top_products)

# Monthly sales trend
monthly_sales = df.groupby('Month')['TotalAmount'].sum()
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales by Payment Method
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='PaymentMethod', order=df['PaymentMethod'].value_counts().index)
plt.title('Orders by Payment Method')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Basic Statistical Analysis
# ----------------------

# Correlation heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df[['Quantity', 'Price', 'TotalAmount']].corr(), annot=True, cmap='Blues')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# Average Order Value
aov = df['TotalAmount'].mean()
print(f"Average Order Value (AOV): ₹{aov:.2f}")

# Customer Lifetime Value (CLV) - simplified as total spend per customer
clv = df.groupby('CustomerID')['TotalAmount'].sum().sort_values(ascending=False)
print("Top 5 Customers by Lifetime Value:\n", clv.head())

#Transfering final dataFrame to CSV
df.to_csv("ecommerce_sales_data.csv", index=False)