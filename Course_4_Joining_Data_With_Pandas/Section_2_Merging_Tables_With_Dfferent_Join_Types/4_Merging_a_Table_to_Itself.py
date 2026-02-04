"""


"""

import pandas as pd
import matplotlib.pyplot as plt


# General settings to show all rows and columns when needed
# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

crews = pd.read_csv('Crews.csv')

crews_self_merged = crews.merge(crews, how='inner', on='id', suffixes=('_dir', '_crew'))
#print(crews_self_merged)

# Create a Boolean index to select the appropriate
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') &
     (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

print(direct_crews.head())