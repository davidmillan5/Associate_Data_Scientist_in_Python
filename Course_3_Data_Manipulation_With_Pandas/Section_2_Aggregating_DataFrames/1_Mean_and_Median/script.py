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

# Print the info about the sales DataFrame
print(sales_dataFrame.info())

# Print the mean of weekly_sales
print(sales_dataFrame[['weekly_sales']].mean())

# Print the median of weekly_sales
print(sales_dataFrame[['weekly_sales']].median())