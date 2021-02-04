"""Create banking system:
#Parent class :
Taking user as a parent class and add user details , also print user details
#Child class "
Taking bank account as a child class and deposit, withdraw money and print balance in account
Ques 2 : Create banking application using OOPs concept and perform following operations:-
1. Account holder can deposit amount.
2. Account holder can withdraw amount.
3. Account holder can view total available balance.
"""


# Parent Class
class User:
    """Initializing the class"""
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        """Method prints user's details"""
        print('User personal details: \n')
        print('Name ', self.name)
        print('Age ', self.age)
        print('Gender ', self.gender)


# Child Class
class BankAccount(User):
    """Initializing the class"""
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)
        self.balance: int = 0

    def deposit(self, amount: int):
        """This method takes the amount you put in as deposit"""
        self.balance = self.balance + amount
        print('Account balance has been updated : Rs.', self.balance)

    def withdraw(self, amount: int):
        """This method takes the amount you put to withdraw"""
        if self.balance >= amount:
            self.balance -= amount
            print('Account balance has been updated : Rs.', self.balance)
        else:
            print('Insufficient funds | Balance Available : Rs.', self.balance)

    def print_balance(self):
        """This method is used to print balance"""
        print('Current balance is : Rs.', self.balance)


if __name__ == '__main__':

    account = BankAccount('Sheeba', 20, 'Female')
    account.deposit(1000)
    account.deposit(1000)
    account.deposit(1000)
    account.deposit(1000)
    account.print_balance()
    account.withdraw(500)
    account.print_balance()
    account.withdraw(10000)
    account.show_user_details()

"""Output:
Account balance has been updated : Rs. 1000
Account balance has been updated : Rs. 2000
Account balance has been updated : Rs. 3000
Account balance has been updated : Rs. 4000
Current balance is : Rs. 4000
Account balance has been updated : Rs. 3500
Current balance is : Rs. 3500
Insufficient funds | Balance Available : Rs. 3500
User personal details: 

Name  Sheeba
Age  20
Gender  Female

"""