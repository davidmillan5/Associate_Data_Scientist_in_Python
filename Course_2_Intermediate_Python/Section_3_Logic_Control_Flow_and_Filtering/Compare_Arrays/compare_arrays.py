# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
my_house_greater = my_house >= 18
print(my_house_greater)
# my_house less than your_house
house_comparison = my_house < your_house
print(house_comparison)