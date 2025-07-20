import random

banks = ["NBE", "AlexBank", "QatarBank"]
print("Welcome to", random.choice(banks))

name = input("Enter your name: ")

while True:
    try:
        balance = float(input("Enter initial balance: "))
        break
    except ValueError:
        print("Please enter a valid number.")

def deposit(balance):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount < 0:
            print("Cannot deposit a negative amount.")
        else:
            balance += amount
            print(f"Deposited ${amount:.2f}")
    except ValueError:
        print("Invalid input.")
    return balance

def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount < 0:
            print("Cannot withdraw a negative amount.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"Withdrawn ${amount:.2f}")
    except ValueError:
        print("Invalid input.")
    return balance

while True:
    print("\nMenu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        print(f"{name}, your balance is: ${balance:.2f}")
    
    elif choice == "2":
        balance = deposit(balance)
        print(f"Balance: ${balance:.2f}")

    elif choice == "3":
        balance = withdraw(balance)
        print(f"Balance: ${balance:.2f}")

    elif choice == "4":
        print(f"Thank you, {name}. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
