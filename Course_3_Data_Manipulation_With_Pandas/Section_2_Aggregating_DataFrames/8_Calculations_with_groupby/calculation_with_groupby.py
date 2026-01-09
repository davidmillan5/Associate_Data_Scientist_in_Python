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

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
print(sales_by_type)

# Get proportion for each type
sales_propn_by_type = sales.groupby("type")["weekly_sales"].sum() / sum(sales_by_type)
print(sales_propn_by_type)

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(['type', 'is_holiday'])['weekly_sales'].sum()
print(sales_by_type_is_holiday)