class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance 


    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} so'm qo'shildi. Yangi balans: {self.balance}")
    

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi. Qolgan balans: {self.balance}")
        else:
            print("Balans yetarli emas")

account = BankAccount("Ali", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)