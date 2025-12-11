# Banking System using OOP and Multiple Inheritance (No Constructors)

class Bank:
    def create_account(self):
        self.account_number = input("Enter Account Number: ")
        self.name = input("Enter Account Holder Name: ")
        self.type = input("Enter Account Type (Savings/Current): ")
        self.balance = 0.0
        print("\nAccount created successfully!\n")

    def show_details(self):
        print("=== Account Details ===")
        print("Account Number:", self.account_number)
        print("Account Holder:", self.name)
        print("Account Type:", self.type)3
        print("Balance:", self.balance)
        print("========================\n")


class Deposit(Bank):
    def deposit(self):
        acc = input("Enter your Account Number: ")
        if acc == self.account_number:
            amount = float(input("Enter amount to deposit: "))
            if amount >= 2000:
                self.balance += amount
                print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}\n")
            else:
                print("Deposit amount must be at least ₹2000.\n")
        else:
            print("Account not found!\n")


class Withdraw(Deposit):
    def withdraw(self):
        acc = input("Enter your Account Number: ")
        if acc == self.account_number:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}\n")
            else:
                print("Insufficient balance.\n")
        else:
            print("Account not found!\n")


class PrintStatement(Withdraw):
    def statement(self):
        print("\n==== ACCOUNT STATEMENT ====")
        self.show_details()


# Create object of final derived class
wt = PrintStatement()

# Menu-driven program
while True:
    print("=== SIMPLE BANKING SYSTEM ===")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        wt.create_account()

    elif choice == "2":
        wt.deposit()

    elif choice == "3":
        wt.withdraw()

    elif choice == "4":
        wt.statement()

    elif choice == "5":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Please try again.\n")
