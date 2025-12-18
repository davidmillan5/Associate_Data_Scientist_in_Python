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

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness_df["indiv_per_10k"] = 10000 * homelessness_df['individuals'] / homelessness_df['state_pop']
print(homelessness_df)

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness_df[homelessness_df["indiv_per_10k"] > 20]
print(high_homelessness)
# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values(by= "indiv_per_10k",ascending=False)
print("high_homelessness_srt --->")
print(high_homelessness_srt)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state', 'indiv_per_10k']]

# See the result
print(result)