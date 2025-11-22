import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV (auto-detect separator)
df = pd.read_csv("colombia_two_columns.csv")

# Ensure columns are correctly named
print(df.columns)

# Plot Year vs Population
plt.figure(figsize=(12, 6))
plt.plot(df["Year"], df["Population"])
plt.title("Population of Colombia Over Time")
plt.xlabel("Year")
plt.ylabel("Population")
plt.grid(True)
plt.tight_layout()
plt.show()
