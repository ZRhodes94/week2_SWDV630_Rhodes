class CheckingAccount:
    def __init__(self, name, address, account_number, balance):
        self.name = name
        self.address = address
        self._account_number = account_number
        self._balance = balance

    def debit(self, amount):
        self._balance += amount
        print(f"{amount: .2f} was added to your account balance.\n")

    def credit(self, amount):
        self._balance -= amount
        print(f"{amount: .2f} was removed from your account balance.\n")

    def check_balance(self):
        print(f"Your account balance is {self._balance: .2f}\n")

def main():
    myAccount = CheckingAccount("Zach", "123 Sesame Street", 123456789, 0.00)

    myAccount.debit(1000)
    myAccount.debit(150000)
    myAccount.credit(150000)
    myAccount.check_balance()

main()