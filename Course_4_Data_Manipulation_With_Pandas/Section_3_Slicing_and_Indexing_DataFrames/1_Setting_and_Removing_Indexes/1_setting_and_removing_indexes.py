# Import Pandas

import pandas as pd

# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# handle dataframes

temperatures = pd.read_csv('../Temperatures.csv')

# Print table
#print(f"========== Printing The whole DataFrame here ==========")
#print(temperatures)

# print headers
#print(f"========== Printing The whole DataFrame headers here ==========")
#print(temperatures.head())


# Look at temperatures
#print(temperatures)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(f"========== Printing The whole DataFrame with index city here ==========")
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
#print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
#print(temperatures_ind.reset_index(drop=True))


