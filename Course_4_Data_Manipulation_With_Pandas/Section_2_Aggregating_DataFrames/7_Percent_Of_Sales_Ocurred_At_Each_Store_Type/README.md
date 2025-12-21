# What percent of sales occurred at each store type?
While .groupby() is useful, you can calculate grouped summary statistics without it.

Walmart distinguishes three types of stores: "supercenters," 
"discount stores," and "neighborhood markets," encoded in this 
dataset as type "A," "B," and "C." In this exercise, you'll 
calculate the total sales made at each store type, without 
using .groupby(). You can then use these numbers to see what 
proportion of Walmart's total sales were made at each type.