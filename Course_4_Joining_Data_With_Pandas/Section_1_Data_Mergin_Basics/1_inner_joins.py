import pandas as pd


# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)



taxi_owners = pd.read_csv('taxi_owners.csv', index_col=0)
taxi_veh = pd.read_csv('taxi_vehicles.csv', index_col=0)

print(taxi_owners.head())
print()
print('==============================================================')
print()
print(taxi_veh.head())
print()
print('==============================================================')
print()

# Merge the taxi_owners and taxi_veh dataframes

taxi_own_veh = taxi_owners.merge(taxi_veh, how='inner', on='vid', suffixes=('_own', '_veh'))
print(taxi_own_veh.head())


print(taxi_own_veh['fuel_type'].value_counts())