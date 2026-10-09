class account:
    def __init__(self,bal,acc_no):
        self.balance = bal
        self.account_no = acc_no

    def debit(self,amount):
        self.balance -= amount
        print("₹",amount,"was debited from the account")
        print("Total Balance : ",self.balance)

    def set_password(self,password):   
        self.__password = password   # used to private(like) attribules
  
    def credit(self,amount):
        self.balance += amount
        print("₹",amount,"was credited to the account")
        print("Total Balance : ",self.balance)

    def get_balance(self):
        return self.balance
        
account1 = account(1000,1)
account1.set_password("12np")
account2 = account(2000,2)
account1.debit(10000)
account1.credit(10000)
print(account1.get_balance())