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

# Add total col as sum of individuals and family_members
homelessness_df['total'] = homelessness_df['individuals'] + homelessness_df['family_members']

# Add p_homeless col as proportion of total homeless population to the state population
homelessness_df['p_homeless'] = homelessness_df['total'] / homelessness_df['state_pop']

# See the result
print(homelessness_df)