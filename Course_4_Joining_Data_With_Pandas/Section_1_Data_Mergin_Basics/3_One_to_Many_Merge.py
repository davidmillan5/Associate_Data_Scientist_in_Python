# Import pandas
import pandas as pd

# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


licenses = pd.read_csv('business_owners.csv', index_col=0)
biz_owners = pd.read_csv('business_owners.csv', index_col=0)

# Starting with the licenses table on the left, merge it to the biz_owners table on the column account, and save the
# results to a variable named licenses_owners.

licenses_owners = licenses.merge(biz_owners, on='account')
print(licenses_owners.head())

# Group licenses_owners by title and count the number of accounts for each title. Save the result as counted_df
counted_df = licenses_owners.groupby(['title_x']).agg({'account':'count'})
print(counted_df.head())

# Sort counted_df by the number of accounts in descending order, and save this as a variable named sorted_df.
sorted_df = counted_df.sort_values('account', ascending=False)
print(sorted_df)

