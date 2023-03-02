#banking
class Bankaccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name,amount):
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.customer_name=customer_name
        self.amount=amount
    def deposit(self): 
        amount=float(input("Enter amount deposited:"))
        self.balance +=self.amount
        print("/n Amount deposited is:",self.amount)
    def withdraw(self):   
        if self.amount> self.balance:
          print("insufficient balance.")
        else:
          self.balance<self.amount
          print(f"{self.amount}has been withdrawn from your account.")  
    def check_balance(self):
        print(f"current balance is {self.balance}.")
    def customer_details(self):
        print("customer name",self.customer_name)
        print("account number",self.account_number)
        print("opening date",self.date_of_opening)
        print(f"balance: {self.balance}\n")
b=Bankaccount(12323,20,12,"brian",2300)
print(b.deposit())
print(b.withdraw())
print(b.check_balance())
print(b.customer_details())

