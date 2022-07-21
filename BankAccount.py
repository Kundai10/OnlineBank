class BankAccount:

    # The BankAccount class contains the client's attributes.

    def __init__(self, bank_balance, client_name, account_number):
        self.bank_balance = bank_balance
        self.client_name = client_name
        self.account_number = account_number
    # the display method contains instructions on what it is supposed to display when a user wants to
    # view their bank account.

    def display(self):
        print("Your Bank Balance is: ", self.bank_balance)
        print("Bank Account Holder's name: ", self.client_name)
        print("Bank Account Number: ", self.account_number)
        print(" ")
    # the withdraw method contains instructions on how to withdraw money from a user's account.
    # used the for loop to store the updated bank balance for a certain account after each withdrawal.

    def withdraw(self):
        withdrawal_amount = int(input("Enter the amount you want to withdraw: "))
        for element in range(1):
            if withdrawal_amount < self.bank_balance:
                self.bank_balance -= withdrawal_amount
                print(f"You are now left with {self.bank_balance} dollars")
            else:
                print("You have insufficient funds.")
    # the deposit method contains instructions on how to deposit money in a certain account
    # used the for loop to store the updated bank balance for a certain account after each deposit

    def deposit(self):

        for element in range(1):
            deposit_amount = int(input("Enter the  amount you want to deposit: "))
            self.bank_balance += deposit_amount
            print(self.bank_balance)
    # the transfer method contains instructions on how to transfer from one client to another within
    # the same bank.

    def transfer(self):
        amount = int(input("How much do you want to transfer:? "))
        if amount < self.bank_balance:
            self.bank_balance -= amount
            receiver = input("What account number are you sending cash to?: ")
            if receiver == "3B":
                print(f"You have sent {amount} dollars to, {client2.client_name}")
            elif receiver == "3A":
                print(f"You have sent {amount} dollars to", client1.client_name)
            elif receiver == "3C":
                print(f"You have sent {amount} dollars to", client3.client_name)
            elif receiver == "3D":
                print(f"You have sent {amount}", client4.client_name)
            elif receiver == "3E":
                print(f"You have sent {amount} dollars to", client5.client_name)
        else:
            print("You have insufficient funds")

# below are the BankAccount's objects.


client1 = BankAccount(30, "Kundai", "3A")
client2 = BankAccount(30, "Jane", "3B")
client3 = BankAccount(30, "Tanu", "3C")
client4 = BankAccount(30, "Eli", "3D")
client5 = BankAccount(30, "Sarah", "3E")
