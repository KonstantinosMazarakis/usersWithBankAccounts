class BankAccount:
    accounts = []
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        if amount <= 0:
            return self
        else:
            self.balance = self.balance + amount
            return self

    def withdraw(self, amount):
        if amount <= 0: 
            return self
        elif amount > self.balance:
            return self

        self.balance = self.balance - amount
        return self
    def display_account_info(self):
        print(f"interest rate is: {self.int_rate} Balance is : {self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self
    @classmethod
    def all_accounts(cls):
        for account in cls.accounts:
            print(f"interest is {account.int_rate} and balance is {account.balance}")

class User:
    user = []
    def __init__(self , name, email_address = None):
        self.name = name
        self.email = email_address
        User.user.append(self)
        self.account = {"checkings" : BankAccount(), "savings" : BankAccount()}

    def make_deposit(self, amount, account_name):
        self.account[account_name].deposit(amount)
        return self

    def make_withdraw(self, amount, account_name):
        self.account[account_name].withdraw(amount)
        return self

    @classmethod
    def printEverything(cls):
        for users in cls.user:
            print(f'User: {users.name} The Checkings Balance is {users.account["checkings"].balance}')
            print(f'User: {users.name} The Savings Balance is {users.account["savings"].balance}')


kostas = User("kostas")
kostas.make_deposit(100 ,"checkings")
kostas.make_deposit(4400 ,"savings")
adriyana = User("adriyana")
adriyana.make_deposit(500 ,"checkings")
adriyana.make_deposit(5300 ,"savings")

User.printEverything()


