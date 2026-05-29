import json

name = input("Name of the new user: ")
age = input("Age of the new user: ")

with open("data.json", "r") as file:
    data = json.load(file)

data.append({
    "name": name,
    "age": age
})

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Foydalanuvchi JSON faylga qo'shildi!")