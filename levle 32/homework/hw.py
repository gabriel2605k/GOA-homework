# 1) შექმენით რიცხვებით სავსე სია, შემდეგ დაწერეთ კოდი რომელიც დაბეჭდავს ამ 
# სიიდან ყველაზე უდიდეს რიცხვს გამოგადგებათ for loop ი კარგად დაფიქრდით და გაიაზრეთ
numbers = [1,2,3,4,5,62,2,1,4,232,62,346,43,6346,3436,634633643634]
largest_number = numbers[0]  
for num in numbers:
    if num > largest_number:
        largest_number = num
print("largest number is:", largest_number)