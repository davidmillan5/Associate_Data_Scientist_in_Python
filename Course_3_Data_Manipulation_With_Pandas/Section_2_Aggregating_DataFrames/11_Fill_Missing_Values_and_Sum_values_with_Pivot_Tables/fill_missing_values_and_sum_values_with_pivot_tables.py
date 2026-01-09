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

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values='weekly_sales', index='department', columns = 'type', fill_value= 0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value= 0, margins=True))