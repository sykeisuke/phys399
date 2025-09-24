import pandas as pd

# Table 1 (from Exercise 2/3)
df1 = pd.DataFrame({
    "region": ["Egypt", "Sudan", "Mexico", "India", "Japan", 
               "Canada", "Brazil", "Australia", "Germany", "South Korea"],
    "avg_temp_C": [30.4, 29.2, 21.0, 25.0, 16.0, 5.0, 24.0, 22.0, 9.0, 12.5],
    "annual_precip_mm": [50, 100, 800, 1200, 1500, 600, 1800, 400, 900, 1200]
})

# Table 2 (new in Exercise 4)
df2 = pd.DataFrame({
    "region": ["Sweden", "Switzerland", "China", "France", "United States", 
               "United Kingdom", "Cuba", "UAE"],
    "avg_temp_C": [3.2, 6.5, 7.6, 11.7, 9.5, 9.2, 24.0, 28.2],
    "annual_precip_mm": [600, 1500, 650, 850, 700, 1200, 1300, 50]
})

# 1. Concatenate two tables
df = pd.concat([df1, df2], axis=0)
df = df.reset_index(drop=True)

print(df)

# 2. Selection
selected = df.loc[df["annual_precip_mm"] < 1000]
selected = selected.reset_index(drop=True)
print(selected)

