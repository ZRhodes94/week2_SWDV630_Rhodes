class CheckingAccount:
    def __init__(self, name, address, account_number, balance):
        self.name = name
        self.address = address
        self.__account_number = account_number
        self.__balance = balance

    def debit(self, amount):
        self.__balance += amount
        print(f"{amount: .2f} was added to your account balance.")
        self.check_balance()

    def credit(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount: .2f} was removed from your account balance.")
            self.check_balance()
        
        elif amount >= self.__balance:
            print(f"Insufficent funds in account number {self.__account_number}.")
            self.check_balance()

    def check_balance(self):
        print(f"{self.name}, your account balance is {self.__balance: .2f}\n")

def main():
    myAccount = CheckingAccount("Zach", "123 Sesame Street", 123456789, 0.00)

    myAccount.debit(1000.00)
    myAccount.debit(150000.00)
    myAccount.credit(150000.00)
    myAccount.credit(1050.00)
    myAccount.debit(1500.00)
    myAccount.debit(1000.00)
    myAccount.credit(1250.00)


main()