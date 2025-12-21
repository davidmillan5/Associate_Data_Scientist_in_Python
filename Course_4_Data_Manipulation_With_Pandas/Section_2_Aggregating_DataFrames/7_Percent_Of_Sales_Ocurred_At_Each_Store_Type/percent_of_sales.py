# Import Pandas
import pandas as pd

# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Prepare CSV file into a DataFrame
sales = pd.read_csv('../sales_subset.csv', index_col=0)

# Print the head of the sales DataFrame
print(f"================================================= Sales Head =============================================")
print(sales.head())

# Print the whole data in the tabular source
print(f"================================================ Table ====================================================")
print(sales)

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()
print(sales_all)

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
print(sales_A)

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()
print(sales_B)

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()
print(sales_C)

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)