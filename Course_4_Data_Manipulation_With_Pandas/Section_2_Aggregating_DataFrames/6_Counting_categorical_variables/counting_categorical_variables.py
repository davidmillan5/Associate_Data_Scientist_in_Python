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

print(f"=================================== Store types =========================================")
print(store_types)

# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
print(f"=========================================Count the number of stores of each type============================")
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize=True)
print(f"=========================================Get the proportion of stores of each type============================")
print(store_props)

# Count the number of stores for each department and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(f"=========================================Count the number of stores for each department and sort============================")
print(dept_counts_sorted)

# Get the proportion of stores in each department and sort
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
print(f"=========================================Get the proportion of stores in each department and sort============================")
print(dept_props_sorted)