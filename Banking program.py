def _balance():
    print("******************")
    print(f"YOUR BALANCE IS ₹{balance:.2f} ")
    print("******************")#😒<_-__-_>   

def deposit():
    print("******************")
    amount = float(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT: "))
    print("******************")
    if amount<0:
        print("INSUFFICIENT AMOUNT TO DEPOSIT\n")
    else:
        global balance
        balance += amount
        return amount
    
def withdraw():
    amount = float(input("ENTER THE AMOUNT TO WITHDRAW: "))
    global balance
    if amount > balance:
        print("INSUFFICIENT AMOUNT")
    else:
        balance -= amount
        print(f"AMOUNT WITHDRRAWN {amount:.2f}")
        return balance
    

balance = 0
running = True 

while running:
    print("WELCOME TO OUR BANK")
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = (input("Enter to select (1-4): "))
    if choice == "1":
        _balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        running = False
    else:
        print("Invalid Selection")

print("THANK YOU PLEASE VISIT AGAIN")
    
