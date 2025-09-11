class Payment:
    def pay(self,amount):
        print(f"{amount} paid")
class CashPayment(Payment):
    def pay(self,amount):
        print(f"{amount} paid in cash")
class CardPayment(Payment):
    def pay(self,amount):
        print(f"{amount} paid using credit/debit card")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"{amount} paid using upi")
l=[CardPayment(),CardPayment(),UPIPayment()]
for i in l:
    i.pay(1000)