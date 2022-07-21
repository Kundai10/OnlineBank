from BankAccount import BankAccount

# the objects from BankAccount class are in this class because I realised that
# importing a class doesn't automatically import its objects
client1 = BankAccount(30, "Kundai", "3A")
client2 = BankAccount(30, "Jane", "3B")
client3 = BankAccount(30, "Tanu", "3C")
client4 = BankAccount(30, "Eli", "3D")
client5 = BankAccount(30, "Sarah", "3E")

# They all have a initial bank deposit of 30 dollars.
# The bank requires a new account holder to have an initial deposit of 30 dollars.

# the menu function contains instruction on how to perform an action.


def menu():
    print("Enter 1 if you want to view your account details")
    print("Enter 2 if you want to withdraw money from your account.")
    print("Enter 3 is you want to deposit money into your account.")
    print("Enter 4 if you want to transfer money to another person who holds an account in this bank.")
    print("Enter 5 if you want to exit.")

# the display_menu function contains instructions for the program to follow depending on
# who the owner of the account is.
# the owner inputs their account number instead of their names since no two people can have the same account number.


def display_money():
    identity = input("To log into your account please input your account number: ")

    if identity == "3A":
        client1.display()
    elif identity == "3B":
        client2.display()
    elif identity == "3C":
        client3.display()
    elif identity == "3D":
        client4.display()
    elif identity == "3E":
        client5.display()
    else:
        print("Invalid account number. Please input your account number.")

# the withdraw_cash function contains instructions for the program to follow depending on
# who the owner of the account is.


def withdraw_cash():
    identity = input("To log into your account please input your account number:  ")
    if identity == "3A":
        client1.withdraw()
    elif identity == "3B":
        client2.withdraw()
    elif identity == "3C":
        client3.withdraw()
    elif identity == "3D":
        client4.withdraw()
    elif identity == "3E":
        client5.withdraw()
    else:
        print("Invalid account number. Please input your account number.")

# the deposit_cash function contains instructions for the program to follow depending on
# who the owner of the account is.


def deposit_cash():
    identity = input("To log into your account please input your account number: ")
    if identity == "3A":
        client1.deposit()
    elif identity == "3B":
        client2.deposit()
    elif identity == "3C":
        client3.deposit()
    elif identity == "3D":
        client4.deposit()
    elif identity == "3E":
        client5.deposit()
    else:
        print("Invalid account number. Please input the correct account number for your bank account.")

# used the while loop to keep on prompting the user if he wants to perform any action.
# used the exit function to break out of the loop when the user does not want to perform any function.


while True:
    user = input("Do you want to perform any action? ").lower()
    # used conditional statements to control the flow of the program.
    if user == "yes":
        menu()
        choice = int(input("What choice do you want?: "))
        if choice == 1:
            display_money()
        elif choice == 2:
            withdraw_cash()
        elif choice == 3:
            deposit_cash()
        elif choice == 4:
            client1.transfer()
        elif choice == 5:
            exit()
        else:
            print("Choice selected is unrecognised.")
    else:
        exit()
