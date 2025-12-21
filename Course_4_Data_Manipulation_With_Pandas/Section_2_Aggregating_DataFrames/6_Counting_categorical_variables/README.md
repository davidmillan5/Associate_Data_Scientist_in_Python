# Counting categorical variables

Counting is a great way to get an overview of your data and to 
spot curiosities that you might not notice otherwise. In this 
exercise, you'll count the number of each type of store and the 
number of each department number using the DataFrames you created 
in the previous exercise:

``````python

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])

``````