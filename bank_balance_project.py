class Account:
    def __init__(self, name, balance, account_no):
        self.name = name
        self.balance = balance
        self.account_no = account_no
    
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Rs {amount} was debited.")
        print(f"Total balance is Rs {self.balance}")
        
    def credit(self, amount):
        self.balance += amount
        print(f"Rs {amount} was credited.")
        print(f"Total balance is Rs {self.balance}")
    
    

# Example usage
a1 = Account("Rohan", 9000, 1)
print(f"Initial Balance: Rs {a1.balance}")
a1.debit(500)
a1.credit(2000)
