import json

with open("data.json", "r") as file:
    data = json.load(file)

print("Name:", data["name"])
print("Course:", data["course"])

print("Skills:")
for skill in data["skills"]:
    print("-", skill)