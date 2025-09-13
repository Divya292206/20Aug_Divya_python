#ATM Pin Check

correct_pin = 2922
attempts = 0

while attempts < 3:
    pin = int(input("Enter your 4-digit PIN: "))
    if pin == correct_pin:
        print("PIN accepted. Access granted.")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {3 - attempts} attempts left.")

else:
    print("Too many incorrect attempts. Your account is locked.")
