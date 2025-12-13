# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# compare
comparison = dr == True

# Use dr to subset cars: sel
sel = cars[comparison]

# Print sel
print(sel)