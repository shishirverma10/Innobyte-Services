import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data with the correct encoding
file_path = 'C:/Users/shish/Downloads/Amazon Sale Report.csv'  # Update this path if necessary
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Handle missing values
df = df.dropna(subset=['Order ID', 'Date', 'Status', 'Amount'])

# Convert 'Date' column to datetime with the appropriate format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Set errors='coerce' to handle invalid dates gracefully

# Drop rows with invalid dates
df = df.dropna(subset=['Date'])

# Remove duplicates
df = df.drop_duplicates()

# Display the cleaned dataframe info
print(df.info())

# Sales Overview
sales_over_time = df.groupby('Date')['Amount'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=sales_over_time, x='Date', y='Amount')
plt.title('Sales Over Time')
plt.show()

# Product Analysis
product_distribution = df['Category'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=product_distribution.index, y=product_distribution.values)
plt.title('Product Category Distribution')
plt.xticks(rotation=45)
plt.show()

# Fulfillment Analysis
fulfillment_distribution = df['Fulfilment'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=fulfillment_distribution.index, y=fulfillment_distribution.values)
plt.title('Fulfillment Method Distribution')
plt.show()

# Geographical Analysis
sales_by_region = df.groupby('ship-state')['Amount'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(data=sales_by_region, x='ship-state', y='Amount')
plt.title('Sales by State')
plt.xticks(rotation=45)
plt.show()
