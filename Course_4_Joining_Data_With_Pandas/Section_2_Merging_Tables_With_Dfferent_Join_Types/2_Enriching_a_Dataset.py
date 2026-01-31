# Import pandas

import pandas as pd

# General settings to show all rows and columns when needed
# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Call DataFrames reading .csv and .p files
movies = pd.read_csv('movies.csv', index_col=0)
financials = pd.read_csv('financials.csv', index_col=0)
casts = pd.read_pickle('casts.p')
casts.to_csv('casts.csv', index=False)
taglines = pd.read_pickle('taglines.p')
taglines.to_csv('taglines.csv', index=False)

# print movies dataframe
#print(movies)

#Create a dataframe just for toystory
# official documentation https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html
toy_story = movies[movies['title'].str.contains('Toy Story', case=False, na=False)]

print('========= Toy Story DataFrame ==========')
print(toy_story)

print('========== taglines =====================')
print(taglines.head())


# Inner Join in pandas

toystory_tag = toy_story.merge(taglines, how='left', on='id')
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, how='inner', on='id')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)