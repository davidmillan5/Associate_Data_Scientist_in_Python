"""
Other Joins
merge methods

- Right Joins
name_variable = dataframe.merge(dataFrame2, how='kind',left_on='feature', right_on='feature')

- Left Joins
- Inner Joins

- Outer Join
variable_name = dataframe1.merge(dataframe2, on='feature', how='outer', suffixes=('_feature', '_feature'))

"""

import pandas as pd
import matplotlib.pyplot as plt

"""
Right join to find unique movies
"""

# General settings to show all rows and columns when needed
# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


movies = pd.read_csv('movies.csv', index_col=0)
print(movies.head())

movie_to_genres = pd.read_csv('movie_to_genres.csv', index_col=0)
print(movie_to_genres.head())

action_filter = movie_to_genres[movie_to_genres['genre']=='Action']
print(action_filter.head())

action_movies = movies.merge(action_filter, how='right', left_on='id', right_on='movie_id')
print(action_movies)

scifi_filter = movie_to_genres[movie_to_genres['genre']=='Science Fiction']
print(scifi_filter.head())


scifi_movies = movies.merge(scifi_filter, how='right', left_on='id', right_on='movie_id')
print(scifi_movies)

action_scifi = action_movies.merge(scifi_movies, how='right', on='movie_id', suffixes=('_act', '_sci'))
print(action_scifi.head(20))


scifi_only = action_scifi[action_scifi['genre_act'].isnull()]
print(scifi_only.head(20))


movies_and_scifi_only = movies.merge(scifi_only, how='inner', left_on='id', right_on='movie_id')
print(movies_and_scifi_only.head(20))



"""
Popular Genres With Right Join
"""

print('================================ Popular Genres With Right Join =====================================')
print()
print()

print(movies.head(50))

#highest_rated_movies = movies.sort_values('popularity', ascending=False)
movies = movies.nlargest(10, 'popularity')
print(movies)

pop_movies = movies.merge(movie_to_genres, how='left', left_on='id', right_on='movie_id')
print(pop_movies)

# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, how='right',
                                      left_on='movie_id',
                                      right_on='id')

# Count the number of genres
genre_count = genres_movies.groupby('genre_x').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()