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
print(sales.head())

# Print the whole data in the tabular source
#print(sales)

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store', 'type'])
print(f"=========================================Drop duplicate store/type combinations============================")
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store', 'department'])
print(f"=========================================Drop duplicate store/department combinations============================")
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset=['date'])

# Print date col of holiday_dates
print(f"=========================================Print date col of holiday_dates============================")
print(holiday_dates[['date']])