# მომხმარებელს შეეკითხეთ ექაუნთძე შესასვლელი პაროლი, სანამ ის არ შემოიტანს სწორ პაროლს მას
#  ხელახლა გაუმეორეთ რომ შემოიტანოს პაროლი თუ სწორად შემოიტანს დაბეჭდოს რომ ექაუნთზე შევიდა


s=password = input("Enter password: ")
reenter= input("Reenter passwored:")
while  reenter == password :
   print("Welcome to your account!")
   
print("Incorrect password. Please try again.")
password = input("Enter password: ")
