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

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness_df[homelessness_df['individuals'] > 10000]

# See the result
print("3.  Filter for rows where individuals is greater than 10000")
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = homelessness_df[homelessness_df['region'] == "Mountain"]

# See the result
print("4.  Filter for rows where region is Mountain")
print(mountain_reg)

# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = homelessness_df[(homelessness_df['family_members'] < 1000) & (homelessness_df['region'] == 'Pacific')]

# See the result
print(fam_lt_1k_pac)
