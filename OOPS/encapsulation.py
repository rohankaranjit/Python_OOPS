#ENCAPSULATION

class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"The amount is {self.__balance}")

    def get_balance(self):
        return self.__balance  

# Creating an object
acc = Account(5000)
acc.deposit(1000)  
print(acc.get_balance())
