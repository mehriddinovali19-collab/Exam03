name = input("Enter your name: ")
age = input("Enter your age: ")

with open ("data.txt", "a") as file:
    file.write(f"{name} - {age} yosh\n")

print("Ma'lumot faylga saqlandi!")