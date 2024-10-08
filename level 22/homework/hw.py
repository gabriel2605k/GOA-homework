#  2) პითონში აქამდე რაც კი გვისწავლია ყველაფრის გამოყენებით გააკეთეთ მაქსიმალურად დახვეწილი 
# რეგისტრაციის ფუნქციონალი, ეცადეთ რაც შეიძლება დახვეწოთ და გააუმჯობესოთ დაუმატოთ ბევრი 
# ფუნქციონალები და ასე შემდეგ, აუცილებლად გამოიყენეთ ლუპები
print("Creating GOOGLE account")

   
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
password = input("Enter your password: ")
phoneNumber = int(input("Enter your phone number: "))
reenter = input("Reenter your password: ")

while reenter != password:
      print("Incorrect password. Please try again.")
      reenter = input("Reenter your password: ")

print("Welcome to your account!")


inf = input("Do you wont to see your inf?: ")
if inf == "yes" :
      print("Firt Name: ",firstName)
      print("Last Name: ",lastName)
      print("Password: ",password)
      print("Phone number: ",phoneNumber)
      print(" ! GOODBEY ! ")
elif inf == "Yes" :
      print("Firt Name: ",firstName)
      print("Last Name: ",lastName)
      print("Password: ",password)
      print("Phone number: ",phoneNumber)
      print(" ! GOODBEY ! ")
elif inf == "YES" :
      print("Firt Name: ",firstName)
      print("Last Name: ",lastName)
      print("Password: ",password)
      print("Phone number: ",phoneNumber)
      print(" ! GOODBEY ! ")
else:
      print(" ! GOODBEY ! ")