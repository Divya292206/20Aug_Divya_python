# def create_account():
#     global balance, name
#     name = input("Enter your name: ")
#     balance = 0
#     print(f"Account created successfully for {name} with ₹{balance} balance.")

# def deposit():
#     global balance
#     amount = float(input("Enter amount to deposit: "))
#     if amount > 0:
#         balance += amount
#         print(f"₹{amount} deposited successfully. Total balance: ₹{balance}")
#     else:
#         print("Invalid amount.")

# def withdraw():
#     global balance
#     amount = float(input("Enter amount to withdraw: "))
#     if amount <= balance:
#         balance -= amount
#         print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{balance}")
#     else:
#         print("Insufficient balance!")

# def check_balance():
#     print(f"Current balance: ₹{balance}")

# # ---------- MAIN PROGRAM ----------
# balance = 0
# name = ""

# while True:
#     print("\n=== Simple Banking System ===")
#     print("1. Create Account")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Check Balance")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         create_account()
#     elif choice == "2":
#         deposit()
#     elif choice == "3":
#         withdraw()
#     elif choice == "4":
#         check_balance()
#     elif choice == "5":
#         print("Thank you for using our bank!")
#         break
#     else:
#         print("Invalid choice, try again.")


