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