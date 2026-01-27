# Import pandas

import pandas as pd

# General settings to show all rows and columns when needed
# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


# Call DataFrames reading .csv and .p files

movies = pd.read_csv('movies.csv', index_col=0)
financials = pd.read_csv('financials.csv', index_col=0)

casts = pd.read_pickle('casts.p')
casts.to_csv('casts.csv', index=False)

taglines = pd.read_pickle('taglines.p')
taglines.to_csv('taglines.csv', index=False)


# Create a Left Join Merge with Pandas
# https://pandas.pydata.org/docs/user_guide/merging.html
# https://pandas.pydata.org/docs/reference/api/pandas.merge.html#pandas.merge

movies_financials = pd.merge(movies, financials, how='left', on='id')
print(movies_financials.head())

# Count the number of rows in movies_financials with a null value in the budget column.

print(movies_financials.isna().sum())
print(movies_financials['budget'].isna().sum())

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isna().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)

# Print the whole DataFrame

print(movies_financials.head())

print(taglines.head())
print(taglines.shape)