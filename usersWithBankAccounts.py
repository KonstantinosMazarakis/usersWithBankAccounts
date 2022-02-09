class BankAccount:
    accounts = []
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
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
    @classmethod
    def printEverything(cls):
        for users in cls.user:
            print(f'User: {users.name} The Checkings Balance is {users.account["checkings"].balance}')
            print(f'User: {users.name} The Savings Balance is {users.account["savings"].balance}')


# {"checkings" : BankAccount()}
kostas = User("kostas")
kostas.account["checkings"].deposit(100)
kostas.account["savings"].deposit(4400)
adriyana = User("adriyana")
adriyana.account["checkings"].deposit(500)
adriyana.account["savings"].deposit(5300)

User.printEverything()


# kostas.account["checkings"].display_account_info()
# kostas.account.deposit(66)

# kostas.account.display_account_info()