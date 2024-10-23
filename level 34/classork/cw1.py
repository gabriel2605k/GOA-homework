#  2) შექმენით ფუნქცია რომელიც
#  მომხმარებელს ეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი
def num():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")
num()