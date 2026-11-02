# # # class bank:
# # #     def __init__(self,account, name , balance):
# # #         self.account=account
# # #         self.name=name
# # #         self.balance=balance
    
# # #     def show (self):
# # #         print("account:",self.account)
# # #         print("name:",self.name)
# # #         print("balance:",self.balance)

# # # a=bank(2324,"anuj",40000)
# # # b=bank(3422,"priyanshu",50000)

# # # a.show()
# # # b.show()

# # class Bank:
# #     def __init__(self, account_no, name, balance):
# #         self.account_no = account_no
# #         self.name = name
# #         self.balance = balance

# #     def show(self):
# #         # Display account details
# #         print(f"name:{self.name} , account_no:{self.account_no}, balance:{self.balance}")

# #     def deposit(self, amount):
# #         # Add amount to balance
# #         self.balance += amount
# #         self.show()
 
 
# #     def withdraw(self, amount):
# #         # Check balance and withdraw
# #         if amount<=self.balance:
# #             self.balace=self.balance-amount
# #         else:
# #             print("insufficient balance")
# #             self.show()

# # # Create the object
# # a1=Bank(234,"anuj",1000)
# # a2=Bank(2345,"priyanshu",2000)

# # # Call show(), deposit(), withdraw(), and show() again
# # a1.show()
# # a1.deposit(500)
# # a1.withdraw(200)
# # a1.show()

# # a2.show()
# # a2.deposit(1000)
# # a2.withdraw(500)
# # a2.show() 

# #abstraction 
# from abc import ABC , abstractmethod
# class Animal(ABC):
#    @abstractmethod
#    def sound(self):
#       pass
   
# class Dog(Animal):
#    def sound (self):
#       print("dog is barking")

# class Cat(Animal):
#    def sound(self):
#       print("cat is meawing")

# s1=Dog()
# s2=Cat()

# s1.sound()
# s2.sound()


# Import tools for creating an abstract class
from abc import ABC, abstractmethod


# ABSTRACTION: Bank is an abstract class
class Bank(ABC):

    # Abstract method: Every bank must define its interest rate
    @abstractmethod
    def interest(self):
        pass  # Implementation will be provided by child classes


# INHERITANCE: SBI inherits from Bank
class SBI(Bank):

    # METHOD OVERRIDING: Implements the parent's interest() method
    def interest(self):
        print("SBI interest rate: 7%")


# INHERITANCE: HDFC also inherits from Bank
class HDFC(Bank):

    # METHOD OVERRIDING: Provides its own interest rate
    def interest(self):
        print("HDFC interest rate: 8%")


# CLASS: Account represents a bank account
class Account:

    # CONSTRUCTOR: Runs automatically when an object is created
    def __init__(self, name, balance):
        self.name = name          # Store account holder's name
        self.balance = balance    # Store account balance

    # METHOD OVERLOADING-LIKE BEHAVIOUR using a default argument
    def deposit(self, amount=0):
        self.balance += amount    # Add money to the existing balance
        print("Balance:", self.balance)


# OBJECTS: Create SBI and HDFC objects
s1 = SBI()
h1 = HDFC()

# Call each bank's interest() method
s1.interest()
h1.interest()

# Create an account with an initial balance of ₹10,000
a = Account("Priyanshu", 10000)

# Deposit ₹5,000 into the account
a.deposit(5000)

# Call deposit() without an amount; default amount is 0
a.deposit()
