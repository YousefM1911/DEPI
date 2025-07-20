import random

banks= ["NBE" , "AlexBank" , "QatarBank"]
print("Welcome to", random.choice(banks))


def create_account():
    name = input(" Enter your name: ")
    while True:
        try:
            balance = float(input(" Enter initial balance: "))
            return name, balance
        except ValueError:
            print(" Please enter a valid number.")

def check_balance(name, balance):
    print(f"{name}, your current balance is: {balance:.2f}")
    return balance

def deposit(balance):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount < 0:
            print(" Cannot deposit a negative amount.")
        else:
            balance += amount
            print(f" Deposited ${amount:.2f}")
    except ValueError:
        print(" Invalid input.")
    return balance

def withdraw(balance):
    try:
        amount = float(input(" Enter amount to withdraw: "))
        if amount < 0:
            print(" Cannot withdraw a negative amount.")
        elif amount > balance:
            print(" Insufficient balance!")
        else:
            balance -= amount
            print(f" Withdrawn ${amount:.2f}")
    except ValueError:
        print(" Invalid input.")
    return balance

def main_menu(name, balance):
    while True:
        print("Main Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input(" Enter your choice: ")

        if choice == "1":
            balance = check_balance(name, balance)
        elif choice == "2":
            balance = deposit(balance)
            balance = check_balance(name, balance)
        elif choice == "3":
            balance = withdraw(balance)
            balance = check_balance(name, balance)
        elif choice == "4":
            print(f"\n Thank you, {name}, for banking with us. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")
