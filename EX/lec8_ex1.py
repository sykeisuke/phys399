import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV
df = pd.read_csv("lec8_ex1.csv")
#print(df.head())
print(df.dtypes)

df_2022 = df.loc[(df["Year"] == 2022) & (df["University ID"] == "141574")]
plt.figure(figsize=(6,6))
plt.pie(df_2022["share"], labels=df_2022["IPEDS Race"], autopct="%1.1f%%")
plt.title("UH Mānoa Enrollment Share by Race (2022)")
plt.show()

hawaiian = df.loc[(df["University ID"] == "141574") & (df["IPEDS Race ID"] == "hawaiian")]
plt.plot(hawaiian["Year"], hawaiian["share"])
plt.title("UH Mānoa: Native Hawaiian Share (2012–2023)")
plt.xlabel("Year")
plt.ylabel("Share (%)")
plt.grid(True)
plt.show()

# 2. Select Year2022
df_selected = df.loc[(df["IPEDS Race ID"] == "hawaiian") & (df["University ID"] == "141574")]
#df_selected = df.loc[(df["Year"] == 2022) & (df["University ID"] == "141574")]
print(df_selected)
