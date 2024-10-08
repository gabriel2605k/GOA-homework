#3) შექმენით თავდაპირველად ცარიელი სია მომხმარებელს შემოატანინეთ რიცხვი
#შემდეგ კი 1-დან ამ რიცხვამდე დაამატეთ ყველა რიცხვი სიაში გამოიყენეთ for loop და append
num0 = []
num1 = int(input("Enter num :"))
for i in range(1, num1+1):
    num0.append(i)
print(num0)