# Import pandas as pd
import pandas as pd

# Read csv file as a DataFrame and set the index to 0
temperatures = pd.read_csv('../Temperatures.csv', index_col=0)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index(['country', 'city'])

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level=['country','city'], ascending=[True, False]))
