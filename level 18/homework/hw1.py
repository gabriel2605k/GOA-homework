# 1) შექმენით ბანკის სისტემა სადაც იქნება ძალიან ბევრი პირობები 
# გამოიყენებთ if, elif და else -ს, გამოიყენებთ ასევე განვლილ მასალასაც
print("log in your bank account")
print("old bank account inf. name gabi  Nick_name gabo)secret ")
name=input("Enter Name or nick Name:")
if name == "gabi":
    print("correct")
    balance= int(input("Enter your account balance:"))
    print(balance)
gamotana = "withdraw"
anserw = input ("do you want to deposit or withdraw? : ")
if anserw == "deposit" :
    d=int(input("enter the amount:"))
    print(balance + d)
if anserw == "withdraw" :
    w=int(input("enter the amount:"))
    print("your balance now is ",balance - w)

elif name == "gabo" :
    print("correct")
    balance= int(input("Enter your account balance:"))
    print(balance)
gamotana = "withdraw"
anserw = input ("do you want to deposit or withdraw? : ")
if anserw == "deposit" :
    d=int(input("enter the amount:"))
    print(balance + d)
if anserw == "withdraw" :
    w=int(input("enter the amount:"))
    print("your balance now is ",balance - w)