# Global variables     
account_number = ""
name = ""
balance = 0.0

def create_account():
    global account_number, name, balance
    account_number = input("Enter a new Account Number: ")
    name = input("Enter Account Holder Name: ")
    balance = 0.0
    print("\n Account created successfully!")
    print("Account Number:", account_number)
    print("Account Holder:", name)
    print("Current Balance: ", balance)

def deposit():
    global balance
    acc = input("Enter your Account Number: ")
    if acc == account_number:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"{amount} deposited successfully. New balance: {balance}")
        else:
            print(" Invalid deposit amount.")
    else:
        print(" Account not found!")

def withdraw():
    global balance
    acc = input("Enter your Account Number: ")
    if acc == account_number:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"{amount} withdrawn successfully. Remaining balance: {balance}")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found!")

def check_balance():
    acc = input("Enter your Account Number: ")
    if acc == account_number:
        print(f"Account Holder: {name}")
        print(f"Current Balance: ₹{balance}")
    else:
        print("Account not found!")

# --------- MAIN PROGRAM ----------
while True:
    print("\n=== SIMPLE BANKING SYSTEM ===")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("👋 Thank you for using our bank!")
        break
    else:
        print("Invalid choice. Try again.")

