# Import pandas as pd
import pandas as pd

# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Read csv file as a DataFrame and set the index to 0
temperatures = pd.read_csv('../Temperatures.csv', index_col=0)

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
#temperatures_bool = temperatures[temperatures["date"].between("2010-01-01", "2011-12-31")]
date_range = pd.date_range("2010-01-01", "2011-12-31")
temperatures_bool = temperatures.loc[(temperatures["date"] >= "2010-01-01") &(temperatures["date"] <= "2011-12-31")]
#temperatures_bool = temperatures[temperatures["date"].isin(date_range)]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index('date').sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc['2010-01-01':'2011-12-31'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['2010-08-01':'2011-02-28'])