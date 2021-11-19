class ATM(object):

    def __init__(self, name, account_number, card_number, type, balance):
        self.name = name
        self.account_number = account_number
        self.card_number = card_number
        self.type = type
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance = self.balance - amount
        print("Your balance is now: ", self.balance)
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Your balance is now: ", self.balance)
    
    def balanceInquiry(self):
        print("Your balance is: ", self.balance)

    def typeOfAccount(self):
      print("This account is a ", self.type, "account")


Vishesh = ATM("Vishesh", 73487, 99834984, "savings", 49369)
Friend1 = ATM("Friend1", 69846, 69835696, "savings", 3323)

Vishesh.withdrawal(2000)
Friend1.deposit(39098)
