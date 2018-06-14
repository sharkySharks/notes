"""
This class implements the __del__ method to decrement the
account counter when an account is deleted
"""

class BankAccount(object):  # Top tier class (super class)
    acct_cntr = 0         # class variable
    def __init__(self):   # This method runs during instantiation
        self.balance = 0  # instance variable
        BankAccount.acct_cntr += 1 # Accessing a class variable
    def withdraw(self, amount):  # a method
        self.balance -= amount
    def deposit(self, amount):     # another method
        self.balance += amount
    def __str__(self):
        return 'The balance for this account is ${:,.2f}'.format(
            self.balance)
    def __del__(self):
        try:
            BankAccount.acct_cntr -= 1
        except AttributeError:
            pass

class BankAccountWithMinBalance(BankAccount):
    def __init__(self, deposit, minBal):
        if deposit < minBal:
            print 'Deposit does not meet the minimum balance for this account. \n',
            print 'Minimum balance: {}'.format(minBal)
            return
        self.balance = deposit
        self.minimumBalance = minBal
        BankAccount.acct_cntr += 1

    def withdraw(self, amount):
        tmpBalance = self.balance - amount
        if tmpBalance < self.minimumBalance:
            raise ValueError, 'You cannot withdrawal below your minimum balance.'
        else:
            self.balance -= amount

    def __str__(self):
        return ('The balance on this account is ${:,.2f}.\n' +
                'The minimum balance is ${:,.2f}.').format(self.balance, self.minimumBalance)

a = BankAccount()  # Create a Bankaccount instance, print class variable
print 'Number of accounts -', BankAccount.acct_cntr
b = BankAccount()  # Create another instance and print class variable
print 'Number of accounts -', BankAccount.acct_cntr
del a    # delete an instance and print class variable again
print 'Number of accounts -', BankAccount.acct_cntr

c = BankAccountWithMinBalance(5000, 500)
print c  #  printing the class will, under the hood, call __str__
c.withdraw(450)
print c
try:
    c.withdraw(5000)
except ValueError, msg:
    print msg
print c
