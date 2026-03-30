import pandas as pd

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print(df.head())

# Shape of dataset
print("Rows:", df.shape[0], "Columns:", df.shape[1])

# Data types and non-null counts
print(df.info())

# Check missing values
print(df.isnull().sum())

# Option 1: Fill missing values with average of the column
df_filled = df.fillna(df.mean(numeric_only=True))

# Option 2: Drop rows with missing values
#df_dropped = df.dropna()

# Average values
print("Column-wise averages:\n", df_filled.mean(numeric_only=True))

# Highest values
print("Column-wise maximums:\n", df_filled.max(numeric_only=True))

# Lowest values
print("Column-wise minimums:\n", df_filled.min(numeric_only=True))

total_revenue = df['Total_Sales'].sum()
print(f'Total Revenue: ₹{total_revenue:,.2f}')

#find the best product
#sum of total sales for each product
product_revenue = df_filled.groupby("Product")["Total_Sales"].sum()
print(product_revenue)

#top products by sale
top_products = product_revenue.sort_values(ascending=False)
print("Products ranked by revenue:\n", top_products)

#best product by sale
best_product = top_products.index[0]
best_revenue = top_products.iloc[0]
print(f"\nBest product: {best_product} with revenue {best_revenue}")

