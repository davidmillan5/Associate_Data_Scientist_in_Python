import pandas as pd
import matplotlib.pyplot as plt


# General settings to show all rows and columns when needed
# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


movies = pd.read_csv('movies.csv', index_col=0)
ratings = pd.read_csv('ratings.csv', index_col=0)

print(movies.head())
print(ratings.head())


movies_ratings = movies.merge(ratings, on='id', how='left')


sequels = pd.read_csv('sequels.csv', index_col=0)
financials = pd.read_csv('financials.csv', index_col=0)

sequels_fin = sequels.merge(financials, how='left', on='id')

print(sequels_fin.head())

orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))
print(orig_seq.head())

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff
titles_diff = orig_seq[['title_org', 'title_seq', 'diff']]

print(titles_diff.head())

print(titles_diff.sort_values('diff', ascending=False).head())