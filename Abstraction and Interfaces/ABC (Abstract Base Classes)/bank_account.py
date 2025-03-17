"""You've just landed a job at BankTech, a startup that provides innovative banking solutions to various clients. Your company is developing a new banking system that handles different types of bank accounts like Savings Account, Checking Account, and Business Account. Your manager just came in and gave you a task to implement the system using Object-Oriented Programming (OOP) concepts in Python.

Objective:
Write a Python program that implements the concepts of abstraction, inheritance, and polymorphism.

Task:
Abstraction:
Create an abstract class BankAccount that cannot be instantiated, but has common attributes and methods for all accounts, such as accountNumber, accountHolderName, balance, deposit(amount), and withdraw(amount).
Inheritance:
Create specific account classes (like SavingsAccount, CheckingAccount, BusinessAccount) that inherit from the BankAccount class and have additional attributes and methods unique to them. For example, the SavingsAccount class could have an additional attribute interest_rate and a method add_interest() to add the interest to the account balance.
Polymorphism:
Implement a method account_type() in the BankAccount class that can be overridden in each subclass to return the appropriate account type. For example, the SavingsAccount class's account_type() method could return "Savings Account".
Instantiation:
Create instances of SavingsAccount, CheckingAccount, and BusinessAccount, and call their account_type() methods.
Display Information:
Once you have completed all the steps, display the account details neatly for the user to read on the console.
Tips:
Remember to import the abc module for creating an abstract class.
Always handle potential exceptions, especially when working with data conversions.
Expected Output in terminal

Account Number: 123456 Account Holder Name: John Doe Account Type: Savings Account Balance: $5000 Interest Rate: 2.5%

Bonus
create a Terminal User interface that presents the user with these options after entering the correct pin:
display balance and information

withdraw money:

mow much would you like to withdraw?
deposit money:

mow much would you like to deposit?
switch account: (View the same option for whatever account is selected, but show the information of that account)"""

from abc import ABC, abstractmethod

#Abstract class for BankAccount
class BankAccount(ABC):
    
    def __init__(self, account_number: str, account_holder_name: str, balance: float):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    @abstractmethod
    def account_type(self) -> str:
        pass

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):

        if amount > 0 and amount <= self.balance:

            self.balance -= amount

            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:

            print("Invalid withdrawal amount.")

    def display_info(self):

        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Account Type: {self.account_type()}")
        print(f"Balance: ${self.balance:.2f}")




class SavingsAccount(BankAccount):

    def __init__(self, account_number: str, account_holder_name: str, balance: float, interest_rate: float):
        super().__init__(account_number, account_holder_name, balance)
        self.interest_rate = interest_rate

    def account_type(self) -> str:

        return "Savings Account"
    
    def add_interest(self):

        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Added interest: ${interest:.2f}. New balance: ${self.balance:.2f}")
class CheckingAccount(BankAccount):

    def __init__(self, account_number: str, account_holder_name: str, balance: float):
        super().__init__(account_number, account_holder_name, balance)

    def account_type(self) -> str:
        return "Checking Account"
class BusinessAccount(BankAccount):

    def __init__(self, account_number: str, account_holder_name: str, balance: float):
        super().__init__(account_number, account_holder_name, balance)

    def account_type(self) -> str:
        return "Business Account"

#TerminalInterface

def terminal_interface(account: BankAccount):

    while True:

        print("\n--- Menu ---")
        print("1. Display Balance and Information")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            account.display_info()
        elif choice == "2":
            amount = float(input("How much would you like to withdraw? $"))
            account.withdraw(amount)
        elif choice == "3":
            amount = float(input("How much would you like to deposit? $"))
            account.deposit(amount)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":

    #Create accounts
    savings_account = SavingsAccount("123456", "John Doe", 5000.0, 2.5)
    checking_account = CheckingAccount("654321", "Jane Smith", 3000.0)
    business_account = BusinessAccount("987654", "Acme Corp", 10000.0)

   
    pin = input("Enter your PIN: ")

    if pin == "1234":  


        #Let the user choose an account
        print("\nSelect an account:")
        print("1. Savings Account")
        print("2. Checking Account")
        print("3. Business Account")
        account_choice = input("Enter your choice: ")

        if account_choice == "1":
            terminal_interface(savings_account)

        elif account_choice == "2":
            terminal_interface(checking_account)
        elif account_choice == "3":

            terminal_interface(business_account)
        else:
            print("Invalid choice.")
    else:
        print("Incorrect PIN. Access denied.")