# Subsetting rows by categorical variables
Subsetting data based on a categorical variable often involves using the or operator (|) to select rows from multiple categories. This can get tedious when you want all states in one of three different regions, for example. Instead, use the .isin() method, which will allow you to tackle this problem by writing one condition instead of three separate ones.

````python
colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]
````