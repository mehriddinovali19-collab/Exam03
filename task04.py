import json

name = input("Name: ")
age = input("Age: ")

with open("data.json", "r") as file:
    data = json.load(file)

data.append({
    "name": name,
    "age": age
})
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
print("Saqlandi!")