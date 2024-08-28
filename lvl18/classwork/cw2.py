# 2) მომხმარებელს შემომატანინეთ რიცხვი და შემდეგ დაბეჭდეთ მომხმარებლის შემოტანილი რიცხვი არის თუ არა ხუთის ჯერადი 
number=int(input("Enter number :"))
solve= (number%5)
print(number)
if solve == 0 :
    print("5 ის ჯერადი")
else:
    print("არ არის 5 ის ჯერადი")