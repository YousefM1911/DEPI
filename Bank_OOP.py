import random

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount < 0:
                print("Cannot deposit a negative amount.")
            else:
                self.balance += amount
                print(f"Deposited ${amount:.2f}")
        except ValueError:
            print("Invalid input.")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount < 0:
                print("Cannot withdraw a negative amount.")
            elif amount > self.balance:
                print("Insufficient balance!")
            else:
                self.balance -= amount
                print(f"Withdrawn ${amount:.2f}")
        except ValueError:
            print("Invalid input.")

    def check_balance(self):
        print(f"{self.name}, your balance is: ${self.balance:.2f}")

banks = ["NBE", "AlexBank", "QatarBank"]
print("Welcome to", random.choice(banks))

name = input("Enter your name: ")
while True:
    try:
        balance = float(input("Enter initial balance: "))
        break
    except ValueError:
        print("Please enter a valid number.")

account = BankAccount(name, balance)

while True:
    print("\nMenu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        account.check_balance()

    elif choice == "2":
        account.deposit()

    elif choice == "3":
        account.withdraw()

    elif choice == "4":
        print(f"Thank you, {name}. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")