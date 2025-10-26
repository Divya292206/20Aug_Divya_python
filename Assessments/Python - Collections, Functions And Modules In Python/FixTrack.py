# Simple FixTrack Program (No Enumerate)

repair_orders = []

def add_order():
    print("\n--- Add Repair Order ---")
    name = input("Enter Customer Name: ")
    device = input("Enter Device Type: ")
    issue = input("Enter Issue: ")
    due_date = input("Enter Due Date: ")

    order = {"name": name, "device": device, "issue": issue, "due_date": due_date}
    repair_orders.append(order)
    print("Repair Order Added Successfully!\n")

def show_orders():
    if len(repair_orders) == 0:
        print("No repair orders found.\n")
    else:
        print("\n--- Repair Orders ---")
        i = 0
        while i < len(repair_orders):
            o = repair_orders[i]
            print(str(i + 1) + ". " + o["name"] + " - " + o["device"] + " - " + o["issue"] + " - Due: " + o["due_date"])
            i = i + 1
        print()

def generate_bill():
    if len(repair_orders) == 0:
        print("No orders available.\n")
        return

    show_orders()
    num = int(input("Enter order number to bill: ")) - 1
    if num < 0 or num >= len(repair_orders):
        print("Invalid order number.\n")
        return

    parts = float(input("Enter Parts Cost: "))
    repair_fee = float(input("Enter Repair Fee: "))
    discount = float(input("Enter Discount (if any): "))
    tax = 0.18 * (parts + repair_fee - discount)
    total = parts + repair_fee - discount + tax

    print("\n--- FIXTRACK BILL ---")
    print("Customer:", repair_orders[num]["name"])
    print("Device:", repair_orders[num]["device"])
    print("Issue:", repair_orders[num]["issue"])
    print("Due Date:", repair_orders[num]["due_date"])
    print("Parts Cost: ₹", parts)
    print("Repair Fee: ₹", repair_fee)
    print("Discount: ₹", discount)
    print("Tax (18%): ₹", round(tax, 2))
    print("-------------------------")
    print("Total Amount: ₹", round(total, 2))
    print("-------------------------\n")

def main():
    while True:
        print("1. Add Repair Order")
        print("2. View All Orders")
        print("3. Generate Bill")
        print("4. Exit")

        ch = input("Enter your choice: ")

        if ch == "1":
            add_order()
        elif ch == "2":
            show_orders()
        elif ch == "3":
            generate_bill()
        elif ch == "4":
            print("Thank you for using FixTrack!")
            break
        else:
            print("Invalid choice! Try again.\n")

main()
