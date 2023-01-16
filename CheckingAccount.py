class CheckingAccount:
    def __init__(self, name, address, account_number, balance):
        self.name = name
        self.address = address
        self.__account_number = account_number
        self.__balance = balance

    def debit(self, amount):
        self.__balance += amount
        print(f"{amount: .2f} was added to your account balance.\n")

    def credit(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount: .2f} was removed from your account balance.\n")
        
        elif amount >= self.__balance:
            print("Insufficent funds in account.")

    def check_balance(self):
        print(f"Your account balance is {self.__balance: .2f}\n")

def main():
    myAccount = CheckingAccount("Zach", "123 Sesame Street", 123456789, 0.00)

    myAccount.debit(1000)
    myAccount.debit(150000)
    myAccount.credit(150000)
    myAccount.check_balance()

main()