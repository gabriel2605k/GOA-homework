# 1) შექმენით რიცხვებით სავსე სია, შემდეგ დაწერეთ კოდი რომელიც დაბეჭდავს ამ 
# სიიდან ყველაზე უდიდეს რიცხვს გამოგადგებათ for loop ი კარგად დაფიქრდით და გაიაზრეთ
numbers = [142,411,2435,3124,45462,512412,625232,1124124,4412,232,62,346,43,6312331246,3436,634633643634]
largest_number = numbers[0]  
for num in numbers:
    if num > largest_number:
        largest_number = num
print("largest number is:", largest_number)