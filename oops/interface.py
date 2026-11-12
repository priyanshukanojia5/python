from abc import ABC, abstractmethod

class payment:
    @abstractmethod
    def pay(self,amount):
        pass
class upi(payment):
     def pay(self,amount):
         print("upi", amount)

class card(payment):
     def pay(self,amount):
         print("card", amount)

p1=upi()
p2=card()

p1.pay(1000)
p2.pay(2000)