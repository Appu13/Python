'''
Created on 11-Feb-2021

A simple ATM simulator

@author: Appu13
'''



balance = 500

while True:
    
    # Menu preparation
    print("************************************************")
    print("\t WELCOME TO COW UNITED BANK")
    print("************************************************\n")
    print("\nMENU\n")
    print("1) WITHDRAW")
    print("2) ADD TO ACCOUNT")
    print("3) TRANSFER TO ANOTHER ACCOUNT")
    print("4) BALANCE ENQUIRY")
    print("5) QUIT")
    
    # Input from the user
    choice = int(input("\nEnter your choice: "))
    
    if choice == 1:
        amt = float(input("Enter the amount to withdraw: "))
        if amt > balance:
            print("Insufficient balance")
            continue
        else:
            balance -= amt
            print("Please collect your cash before you leave")
            continue
    
    if choice == 2:
        amt = float(input("Enter the amount to add to account: "))
        balance += amt
        print("Transaction successful")
        continue
    
    if choice == 3:
        amt = float("Enter the amount to Transfer: ")
        if amt > balance:
            print("Insufficient balance")
            continue
        else:
            balance -= amt
            print("Transfer successful")
            continue
    
    if choice == 4:
        print("Your bank balance ", balance)
        continue
    
    if choice == 5:
        print("Thank you for using our facility")
        break
