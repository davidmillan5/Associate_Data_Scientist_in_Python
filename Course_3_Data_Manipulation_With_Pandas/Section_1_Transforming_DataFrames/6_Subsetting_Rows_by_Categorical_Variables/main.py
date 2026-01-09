# Import pandas as pd

print("1. Import pandas as pd")
import pandas as pd

# Show all columns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Show all rows
pd.set_option('display.max_rows', None)


# Create a DataFrame base on the homelessness.csv file
print("2. Handle csv files as df")
homelessness_df = pd.read_csv("homelessness.csv", index_col=0)
print(homelessness_df)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness_df[['state']].isin(canu)
mojave_homelessness = homelessness_df[mojave_homelessness]
# See the result
print(mojave_homelessness)