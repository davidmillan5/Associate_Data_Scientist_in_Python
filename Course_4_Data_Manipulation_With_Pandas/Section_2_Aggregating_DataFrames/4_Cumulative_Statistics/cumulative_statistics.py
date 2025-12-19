# Import Pandas
import pandas as pd

# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Prepare CSV file into a DataFrame
sales_dataFrame = pd.read_csv('../sales_subset.csv', index_col=0)

# Print the head of the sales DataFrame
print(sales_dataFrame.head())

# Print the whole data in the tabular source
#print(sales_dataFrame)

sales_1_1 = sales_dataFrame[(sales_dataFrame['store'] == 1) & (sales_dataFrame['department'] == 1)]
print(sales_1_1.head())


# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values(by='date', ascending=True)

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
