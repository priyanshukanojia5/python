#this is the classic opps problem on private variables and methods in python. 
# In this example, we have a class BankAccount with a private variable __balance.
#  The deposit and withdraw methods are used to modify the balance,
#  while the show_balance method is used to display the current balance.
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)
    
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance-=amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)

b = BankAccount(5000)
b.withdraw(1000)
b.deposit(2000)
b.show_balance()