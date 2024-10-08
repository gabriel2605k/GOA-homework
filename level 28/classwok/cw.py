#    1) შექმენით ერთიდან 10მდე რიცხვებით სავსე სია, შემდეგ 
# დაბეჭდეთ ამ სიიდან მხოლოდ ლუწი რიცხვები,  გამოიყენეთ მათი ინდექსები
numbers = list(range(1, 11))
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i])