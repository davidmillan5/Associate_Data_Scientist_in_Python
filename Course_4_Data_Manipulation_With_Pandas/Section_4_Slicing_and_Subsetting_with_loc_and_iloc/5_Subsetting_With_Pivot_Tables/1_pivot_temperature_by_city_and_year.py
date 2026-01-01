# Import pandas as pd
import pandas as pd

# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Read csv file as a DataFrame and set the index to 0
temperatures = pd.read_csv('../Temperatures.csv', index_col=0)

# First We need to identify the types of data we have in each feature
print(temperatures.info())

# After that we have to convert the data type of date to datetime
temperatures['date'] = pd.to_datetime(temperatures['date'])

# Verify that thew change really did happen
print(temperatures.info())

# After te change was apply to the data type, we can keep working on it

# Add a year column to temperatures
temperatures['year'] = temperatures['date'].dt.year
#print(temperatures['year'])

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(
    'avg_temp_c',
    index=['country', 'city'],
    columns='year',
)

print(temp_by_country_city_vs_year)