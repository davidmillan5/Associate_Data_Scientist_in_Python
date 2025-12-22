# Import pandas as pd
import pandas as pd

# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Read csv file as a DataFrame and set the index to 0
temperatures = pd.read_csv('../Temperatures.csv', index_col=0)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index(['country', 'city'])

