# 2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაითვალეთ ამ რიცხვამდე ყველა ნატურალური რიცხვის ჯამი
n = int(input("Enter a number: "))

jumber = 0
for i in range(1, n + 1):
    jumber += i

# Print the result
print(jumber)