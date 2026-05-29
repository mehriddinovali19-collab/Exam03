with open("data.txt", "r") as file:
    count = len(file.readlines())

    print(f"data.txt faylida {count} ta foydalanuvchi mavjud")
        