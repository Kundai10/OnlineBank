from BankAccount import BankAccount
import datetime


# imported the Bank Account class so that I can inherit its methods and attributes in the subclasses
# imported the datetime module so that I can calculate the months between two dates.

# the Savings Account inherits from the BankAccount class
class SavingsAccount(BankAccount):
    def __init__(self, bank_balance, client_name, account_number):
        super().__init__(bank_balance, client_name, account_number)
        # used super()__init__ so that that the SavingsAccount accesses the Parent's init functionality

    # the interest method calculates interest

    def interest(self):
        try:
            # used try, except to handle errors.
            # used the except ValueError so that it provides an exception when a
            # user inputs a string where an integer is required.
            print(" ")
            print("You are now at the CALCULATING INTEREST section")
            rate = 0.03
            time = int(input("Enter the number of months the money has been in your Savings Account: "))
            result = rate * time * savings_account.bank_balance

            print(
                f"The {savings_account.bank_balance} dollars you deposited for {time} months, has gained {result} dollars interest")
            savings_account.bank_balance += result
            print(f"Your balance is now {savings_account.bank_balance} dollars.")
            choice = input("Would you like to check if you are eliglible to withdraw your savings?: ").lower()

            if choice == "yes":
                savings_account.withdraw()
            else:
                print("Thank you for using Dangote Bank. See you again next time.")

        except ValueError:
            print("There seems to be an error with the way you entered the months")
            print("Enter the months as a number, no words,eg. enter 2 ")

    # the withdraw method checks if a user can withdraw money.

    def withdraw(self):
        try:
            # used try, except to handle errors.
            # used the except ValueError so that it provides an exception when a
            # user inputs a string where an integer is required.
            print("To check if you can withdraw, please provide the date you deposited money and today's date.")
            print("--------------------------------------------------------------------------------------")
            deposit_year = int(input("Enter the year you deposited cash: "))
            deposit_month = int(input("Enter the month you deposited cash: "))
            deposit_day = int(input("Enter deposit day: "))

            print("----------------------------------------------------------------------------------------")
            print("Below please input Today's date.")
            withdraw_year = int(input("Enter the year: "))
            withdraw_month = int(input("Enter the month: "))
            withdraw_day = int(input("Enter today's day: "))
            #
            withdrawal_date = datetime.date(withdraw_year, withdraw_month, withdraw_day)
            deposit_date = datetime.date(deposit_year, deposit_month, deposit_day)
            num_months = (withdrawal_date.year - deposit_date.year) * 12 + (withdrawal_date.month - deposit_date.month)
            print(" ")
            print(f"Your money has spent {num_months} months in your Savings Account.")
            # if months are greater than 6, then the user can withdraw
            # that's what the question prompt required.
            if num_months > 6:
                user_choice = input("You are eligible to withdraw.Would you like to withdraw your money?: ")
                if user_choice == "yes":
                    super().withdraw()
                    # called the withdraw method from the Parent Class.
                else:
                    print("Thank you for using Dangote Bank. See you again next time.")
            else:
                print("Sorry you cannot withdraw at this time. You can only withdraw after 6 months.")
        except ValueError:
            print("It seems like there is an error in the way you entered the dates.")
            print("For year print it as 2020. For the month, if it is April, please input 4, if it is May, input 5")
            print("If it is 3rd of January, simply input 3 for the day.Don't add a zero before the dates like 03")

    # the add_money method displays the receipt after a user deposits money

    def add_money(self):
        print(" ")
        print("Thank you for using Dangote Bank. Your deposit has been successful")
        print("Below is your deposit receipt.")
        # called the display method from the Parent class.
        super().display()
        print(" ")
        # used conditional statements to control the flow of the program.
        user_choice = input("Would you like to calculate how much interest your Savings have gained?: ").lower()
        if user_choice == "yes":
            savings_account.interest()
        else:
            choice = input("Would you like to check if you are elliglible to withdraw your savings instead?: ").lower()
            if choice == "yes":
                savings_account.withdraw()
            else:
                print("Thank you for using Dangote Bank. See you again next time.")


# the CurrentAccount inherits from the BankAccount


class CurrentAccount(BankAccount):
    def __init__(self, bank_balance, client_name, account_number):
        super().__init__(bank_balance, client_name, account_number)
        # the super()__init__ allows the CurrentAccount to access BankAccount's init functionality
    # the add_money method displays a receipt after a deposit has been made

    def add_money(self):
        print(" ")
        print("Thank you for using Dangote Bank. Your deposit has been successful")
        print("Below is your deposit receipt.")
        # called the display method from the Parent class.
        super().display()

    # the interest function calculates the interest gained

    def interest(self):
        try:
            print(" ")
            print("You are now at the CALCULATING INTEREST section")
            rate = 0.01
            time = int(input("Enter the number of months the money has been in your Current Account: "))
            # formula for calculating interest
            result = rate * time * current_account.bank_balance

            print(
                f"The {current_account.bank_balance} dollars you deposited for {time} months, has gained {result} dollars interest")
            current_account.bank_balance += result
            print(f"Your balance is now {current_account.bank_balance} dollars.")
            withdraw_choice = input("Would you like to withdraw from your Current Account: ").lower()
            # called the withdraw method from the Parent class.
            if withdraw_choice == "yes":
                super().withdraw()
            else:
                print("Thank you for using Dangote Bank. See you next time.")
        except ValueError:
            print("There seems to be an error with the way you entered the months")
            print("Enter the months as a number, no words, eg enter 2 ")

    # used try, except to handle errors.
    # used the except ValueError so that it provides an exception when a
    # user inputs a string where an integer is required.

    # the withdraw method allows the user to withdraw money

    def withdraw(self):
        # used try, except to handle errors.
        # used the except ValueError so that it provides an exception when a
        # user inputs a string where an integer is required
        try:
            print("To check how much interest your deposit has gained provide the date you deposited and today's date.")
            print("--------------------------------------------------------------------------------------")
            deposit_year = int(input("Enter the year you deposited cash: "))
            deposit_month = int(input("Enter the month you deposited cash: "))
            deposit_day = int(input("Enter deposit day: "))

            print("----------------------------------------------------------------------------------------")
            print("Below please input Today's date.")
            withdraw_year = int(input("Enter the year: "))
            withdraw_month = int(input("Enter the month: "))
            withdraw_day = int(input("Enter today's day: "))
            # procedure of calculating number of months between dates
            withdrawal_date = datetime.date(withdraw_year, withdraw_month, withdraw_day)
            deposit_date = datetime.date(deposit_year, deposit_month, deposit_day)
            num_months = (withdrawal_date.year - deposit_date.year) * 12 + (withdrawal_date.month - deposit_date.month)
            print(" ")
            print(f"Your money has spent {num_months} months in your Current Account.")

            # if the money has been there for 1 month or more, then it can calculate interest gained.
            # that's what the question prompt required.
            if num_months >= 1:
                current_account.interest()
            else:
                print("The money you deposited hasn't gained interest yet. Please wait for one month.")
        except ValueError:
            print("It seems like there is an error in the way you entered the dates.")
            print("For year print it as 2021. For the month, if it is April, please input 4, if it is May, input 5")
            print("If it is the 3rd of January, simply input 3 for the day. Please don't add a zero before your dates.")


print("Select the account you wish to make a deposit\n 1.The Savings Account\n 2.The Current Account")
try:
    # used try, except to handle errors.
    # used the except ValueError so that it provides an exception when a
    # user inputs a string where an integer is
    choose_account = int(input(
        "Enter 1 if you want to deposit in a savings account. Enter 2 if you want to deposit in a current account: "))
    if choose_account == 1:
        # placed the objects of each class under conditional statements.
        # the attributes are not hardcoded. The user gets to input their details.
        print(" ")
        print("Welcome to Dangote Bank. This is the SAVINGS ACCOUNT section.")
        print(" ")
        bank_balance = int(input("Enter the amount you want to deposit in your Savings Account: "))
        client_name = input("Enter your name: ")
        account_number = input("Enter your bank account number: ")

        savings_account = SavingsAccount(bank_balance, client_name, account_number)
        savings_account.add_money()

    elif choose_account == 2:
        # placed the objects of each class under conditional statements.
        # the attributes are not hardcoded. The user gets to input their detals.
        print(" ")
        print("Welcome to Dangote Bank. This is the CURRENT ACCOUNT section.")
        print(" ")
        bank_balance = int(input("Enter the amount you want to deposit in your Current Account: "))
        client_name = input("Enter your name: ")
        account_number = input("Enter your bank account number: ")

        current_account = CurrentAccount(bank_balance, client_name, account_number)
        current_account.add_money()

        user = input("Do you want to check how much interest your deposit has gained?: ").lower()
        if user == "yes":
            current_account.withdraw()
        else:
            print("Thank you for using Dangote Bank. See you next time.")
    else:

        print("The selected option does not exist.")
except ValueError:
    print("There seems to be an error with how you selected your deposit account or entered your deposit balance")
    print("Please input your balance as a number, such as 2 or 100. No words involved.")
    print("Please input your choice for an account, simply as 1 or 2. No words please.")
