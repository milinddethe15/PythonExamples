from abc import ABC, abstractmethod
from random import randint

class Account(ABC):
    @abstractmethod
    def create_account():
        pass

    @abstractmethod
    def authenticate_account():
        pass

    @abstractmethod
    def withdraw():
        pass

    @abstractmethod
    def deposit():
        pass

    @abstractmethod
    def check_balance():
        pass

    @abstractmethod
    def delete_account():
        pass

class Saving_account(Account):
    def __init__(self):
        self.savingAccount = {}
    
    def create_account(self, name, intialDeposite):
        self.accountNumber = randint(1000000,9999999)
        self.savingAccount[self.accountNumber] = [name, intialDeposite]
        print(f"You have successfully created your account. Your account number is {self.accountNumber}.")

    def authenticate_account(self,name,accountNumber):
        if accountNumber in self.savingAccount.keys():
            if self.savingAccount[self.accountNumber][0] == name:
                print("Authentication Successful!")
                self.accountNumber = accountNumber
                return True
        else : 
            print("Authentication failed")
            return False        
    
    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.savingAccount[self.accountNumber][1]:
            print("Insuffient amount")
            userInput = input("Do you want to take loan?[y/n] ")
            if userInput == "y" or userInput == "Y":
                loanAmount = (self.savingAccount[self.accountNumber][1] - withdrawAmount)* -1
                print(f"Loan amount = {loanAmount}")
                self.savingAccount[self.accountNumber][1] -= withdrawAmount
                self.check_balance()
        else:
            self.savingAccount[self.accountNumber][1] -= withdrawAmount
            print("Withdraw Successful!")
            self.check_balance()
    
    def deposit(self, depositAmount):
        self.savingAccount[self.accountNumber][1] += depositAmount
        self.check_balance()

    def check_balance(self):
        print(f"Available balance: {self.savingAccount[self.accountNumber][1]}")

    def delete_account(self):
        if self.savingAccount[self.accountNumber][1] == 0:
            del self.savingAccount[self.accountNumber] , self.accountNumber
            print("You have successfully deleted your account.")
            return True
        else:
            print("To delete, clear all your balance from account.")
            self.check_balance()
    
saving_account = Saving_account()

while True:
    print('-'*100)
    print("WELCOME TO CITY BANK")
    print('-'*100)
    print("Enter 0 to create account.\nEnter 1 to access existing account.\nEnter 2 to exit.")
    userInput = int(input())
    if userInput == 0 : 
        name = input("Enter your name: ")
        initialDeposite = int(input("Enter intial deposit: "))
        saving_account.create_account(name,initialDeposite)
    if userInput == 1:
        name = input("Enter your name: ")
        accountNumber = int(input("Enter your account number: "))
        authenticationStatus = saving_account.authenticate_account(name, accountNumber)
        if authenticationStatus is True: 
            while True:
                print('-'*100)
                print("logged in!")
                print('-'*100)
                print("Enter 0 to Withdraw.\nEnter 1 to Desposit.\nEnter 2 to Check Balance.\nEnter 3 to delete your account.\nEnter 4 to Exit.")
                userInput = int(input())
                if userInput == 0:
                    withdrawAmount = int(input("Enter the withdraw Amount: "))
                    saving_account.withdraw(withdrawAmount)
                if userInput == 1:
                    despositAmount = int(input("Enter the deposit Amount: "))
                    saving_account.deposit(despositAmount)
                if userInput == 2: 
                    saving_account.check_balance()
                if userInput == 3:
                    if saving_account.delete_account(): break
                if userInput == 4:
                    break
    if userInput == 2:
        exit()