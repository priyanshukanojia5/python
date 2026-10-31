# class bank:
#     def __init__(self,account, name , balance):
#         self.account=account
#         self.name=name
#         self.balance=balance
    
#     def show (self):
#         print("account:",self.account)
#         print("name:",self.name)
#         print("balance:",self.balance)

# a=bank(2324,"anuj",40000)
# b=bank(3422,"priyanshu",50000)

# a.show()
# b.show()

class Bank:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def show(self):
        # Display account details
        print(f"name:{self.name} , account_no:{self.account_no}, balance:{self.balance}")

    def deposit(self, amount):
        # Add amount to balance
        self.balance += amount
        self.show()
 
 
    def withdraw(self, amount):
        # Check balance and withdraw
        if amount<=self.balance:
            self.balace=self.balance-amount
        else:
            print("insufficient balance")
            self.show()

# Create the object
a1=Bank(234,"anuj",1000)
a2=Bank(2345,"priyanshu",2000)

# Call show(), deposit(), withdraw(), and show() again
a1.show()
a1.deposit(500)
a1.withdraw(200)
a1.show()

a2.show()
a2.deposit(1000)
a2.withdraw(500)
a2.show()