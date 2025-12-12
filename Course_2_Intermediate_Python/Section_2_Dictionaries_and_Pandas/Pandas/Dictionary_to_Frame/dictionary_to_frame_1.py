# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary with empty lists
my_dict = {
    "country": [],
    "drives_right": [],
    "cars_per_cap": []
}

counter = 0
while counter <= len(names) - 1:
    my_dict["country"].append(names[counter])
    my_dict['drives_right'].append(dr[counter])
    my_dict['cars_per_cap'].append(cpc[counter])
    counter += 1


# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)