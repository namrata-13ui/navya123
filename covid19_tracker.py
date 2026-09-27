import pandas as pd

# Read COVID data
df = pd.read_csv("covid_data.csv")

print("----- COVID-19 Data -----")
print(df)

print("\n----- Total Cases -----")
print(df["Total_Cases"].sum())

print("\n----- Total Deaths -----")
print(df["Deaths"].sum())

print("\n----- Total Recoveries -----")
print(df["Recovered"].sum())

print("\n----- Country with Highest Cases -----")
highest = df.loc[df["Total_Cases"].idxmax()]
print(highest["Country"])