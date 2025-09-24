import pandas as pd

data = {
    "region": ["Egypt", "Sudan", "Mexico", "India", "Japan", 
               "Canada", "Brazil", "Australia", "Germany", "South Korea"],
    "avg_temp_C": [30.4, 29.2, 21.0, 25.0, 16.0, 
                   5.0, 24.0, 22.0, 9.0, 12.5],
    "annual_precip_mm": [50, 100, 800, 1200, 1500, 
                         600, 1800, 400, 900, 1200]
}

df = pd.DataFrame(data)
print(df)

# 1. Selection
warm_regions = df[(df["avg_temp_C"] > 20) & (df["annual_precip_mm"] > 1000)]
print(warm_regions)

# 2. Save as CSV
warm_regions.to_csv("warm_regions.csv", index=False)
