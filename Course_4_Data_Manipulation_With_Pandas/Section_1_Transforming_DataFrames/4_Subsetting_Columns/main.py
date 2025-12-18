import pandas as pd

# Show all columns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Show all rows
pd.set_option('display.max_rows', None)

homelessness_df = pd.read_csv('homelessness.csv', index_col=0)

print(homelessness_df)


# Select the individuals column
print('Select the individuals column')
individuals = homelessness_df['individuals']

print(individuals.head())

# Select the state and family_members columns
print('Select the state and family_members columns')
state_fam = homelessness_df[['state', 'family_members']]

print(state_fam.head())


# Select only the individuals and state columns, in that order
print('Select only the individuals and state columns, in that order')
ind_state = homelessness_df[['individuals', 'state']]

print(ind_state.head())