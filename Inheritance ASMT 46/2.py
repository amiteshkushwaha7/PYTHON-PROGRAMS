class Account:
    roi = 0
    def __init__(self, accountNo, balance):
        self.accountNo = accountNo
        self.balance = balance
    
    def inputAccount(self, accountNo, balance):
        self.account = accountNo
        self.balance = balance
    
    @staticmethod
    def setRoi(cls,roi):
        cls.roi = roi
    
    def getAccout(self):
        print("Account Numb:",self.accountNo)
        print("Balance:",self.balance)
        print("ROI:",self.roi)
        
class FixedDeposit(Account):
    def __init__(self, accountNo, balance, roi, time):
        self.time = time
        super().__init__(accountNo, balance)   #Account.__intit(self,accoutNo,balance)
        Account.roi = roi
    
    def setTime(self,time):
        self.time = time
    
    def getTime(self):
        print("Time:",self.time)
        
    def setFixedDeposite(self,accountNo, balance, roi, time):
        self.time = time
        super().__init__(accountNo, balance)  #Account__init__(self,accountNo,balance)
        Account.roi = roi
    
    def getFixedDeposite(self):
        super().getAccout()
        print("Time:",self.time)
    
    def SI(self):
        return (self.balance * Account.roi * self.time)/100

obj = FixedDeposit(1234,100,10,10)
print(obj.SI())
obj.getFixedDeposite()
