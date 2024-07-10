available_amt = 5000

name = input("Enter yout name: ")
message = """How may I help you

Choose any option
type 1 >>> CHECK BALANCE
type 2 >>> DEPOSIT
type 3 >>> WITHDRAWL"""

print("Hello", name, message)

task = int(input("Enter your option: "))

if (task>=1 and task<=3) :
    print("Welcome to virtual bank program")

    if task==1 :
        # check balance
        print("Your available balance is :", available_amt, 'INR')
    
    elif task==2 :
        # deposit amount
        deposit_amt = int(input("Enter deposit amount: "))
        
        if (deposit_amt>0) :
            available_amt += deposit_amt
            print('Successfully deposit amount', deposit_amt, 'INR to your account')
            print("Your current balance is :", available_amt, 'INR')
        else :
            # invalid amount input
            print("Invalid deposit amount")
    
    else :
        # withdrawl amount
        withdrawl_amt = int(input("Enter withdrawl amount: "))
        
        if (withdrawl_amt<=available_amt) :
            available_amt -= withdrawl_amt
            print('Successfully withdraw amount', withdrawl_amt, 'INR from your account')
            print("Your current balance is :", available_amt, 'INR')
        else :
            # invalid amount input
            print("Insufficient balance")

else :
    print("Invalid option\n")
