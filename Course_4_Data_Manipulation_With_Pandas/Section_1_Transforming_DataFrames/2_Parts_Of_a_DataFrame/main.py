# First import the libraries you will need
import pandas as pd


# Now use the csv file we will inspect Reference
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html
homelessness_dataframe = pd.read_csv('homelessness.csv')

# Print the values of homelessness
print(homelessness_dataframe.values)

# Print the column index of homelessness
print(homelessness_dataframe.columns)

# Print the row index of homelessness
print(homelessness_dataframe.index)