class Account:
    balance = 0
    def __init__(self,balance):
        self.balance = balance
    
    def deposite(self,amout):
        self.balance = amout
        
    def withdraw(self,amount):
        self.balance = self.balance - amount
        print(amount,"debited")
        print("Remain Balance:",self.balance)
    
class MinBalanceAccount(Account):
    def __init__(self, minimum_balance):
        self.minimum_balance = minimum_balance
    
    def withdraw(self, amount):
        if self.balance - self.minimum_balance >= amount:
            super().withdraw(amount)
        else:
            print("Withdraw failed")
            
        
obj = MinBalanceAccount(100)
obj.deposite(1000)
obj.withdraw(900)
obj.withdraw(600)