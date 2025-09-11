class BankAccount:
    def __init__(self):
        self.__balance=0
    def deposit(self,amount):
        self.__balance+=amount
        print("successfully deposited")
    def withdraw(self,amount):
        if self.__balance-amount<0:
            print("Insuficient balance")
        else:
            self.__balance-=amount
            print("successfully withdrawed")
    def get_balance(self):
        print(f"current balance is {self.__balance}")
account=BankAccount()
account.deposit(1000)
account.deposit(500)
account.withdraw(1000)
account.withdraw(1000)
account.get_balance()