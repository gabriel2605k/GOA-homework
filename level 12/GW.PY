#bank account
print("creat new bank account")
name=print(input("Enter your new bank account name:"))
password=input("Enter your new bank account password:")

if input("Reenter your password:") ==  password :   
    print("New bank created")
else:
    if input("Try again !:") == password :
        print("New  bank account created")
    else :
        input("Try  again !") == password 
        if input("Try again !:") == password :
            print("New bank account created")
        else :
            print("you cant have another try!")

#new bank account balance

initial_balance = int(input("Enter initial deposit amount: "))
print ( " your balance is ", initial_balance)
if input("Reenter your password:") ==  password :   
    print("")
else:
    if input("Try again !:") == password :
        print("")
    else :
        input("Try  again !") == password 
        if input("Try again !:") == password :
            print("")
        else :
            print("you forgot !")

gamotana = "withdraw"
anserw = input ("do you want to deposit or withdraw? : ")
if anserw == "deposit" :
    d=int(input("enter the amount:"))
    print(initial_balance + d)
if anserw == "withdraw" :
    w=int(input("enter the amount:"))
    print("your balance now is ",initial_balance - w)

print("GOOD JOB!")