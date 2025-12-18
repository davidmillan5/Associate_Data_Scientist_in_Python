# Import Pandas
import pandas as pd

# Create a DataFrame
homelessness_df = pd.read_csv("homelessness.csv")

# Sort homelessness by individuals
homelessness_ind = homelessness_df.sort_values("individuals", ascending=True)

# Print the top few rows
print(homelessness_ind.head())


# Sort homelessness by descending family members
homelessness_fam = homelessness_df.sort_values("family_members", ascending=False)

print(homelessness_fam.head())


# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness_df.sort_values(by =[ 'region', 'family_members'],
ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())