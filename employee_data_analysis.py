import pandas as pd

# Employee data
data = {
    "Name": ["Namrata", "Rahul", "Priya", "Aman", "Sneha"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [45000, 40000, 55000, 50000, 42000],
    "Experience": [1, 2, 3, 4, 2]
}

df = pd.DataFrame(data)

print("----- Employee Data -----")
print(df)

print("\n----- Average Salary -----")
print(df["Salary"].mean())

print("\n----- Highest Salary -----")
print(df["Salary"].max())

print("\n----- Lowest Salary -----")
print(df["Salary"].min())

print("\n----- Employees by Department -----")
print(df["Department"].value_counts())

print("\n----- Employees with Experience >= 3 Years -----")
print(df[df["Experience"] >= 3])