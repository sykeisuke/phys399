import numpy as np
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

# 1. Replace precipitation for Mexico with NaN
df.loc[2, "annual_precip_mm"] = np.nan
print(df)

# 2. Drop missing row 
df_drop = df.dropna()
print(df_drop)

# 3. Selection
selected = df_drop.loc[(df_drop["avg_temp_C"] > 20) & (df_drop["annual_precip_mm"] > 1000)]
print(selected)

