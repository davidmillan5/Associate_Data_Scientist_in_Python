# First import the libraries you will need
import pandas as pd


# Now use the csv file we will inspect Reference
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html
homelessness_dataframe = pd.read_csv('homelessness.csv')

# Print the info contained in the DataFrame

# DataFrame head()
print("DataFrame Head =")
print(homelessness_dataframe.head())

# DataFrame .info()
print("DataFrame Info = ")
print(homelessness_dataframe.info())

# DataFrame .shape -> return the number of rows and columns
print("DataFrame Shape =")
print(homelessness_dataframe.shape)

# DataFrame .describe() -> calculates a few summary statistics for each column
print("DataFrame Describe =")
print(homelessness_dataframe.describe())