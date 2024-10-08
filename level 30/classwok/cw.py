#  1) შექმენით მენტორების სახელების სია და ჩვეულებრივი სახელებისთვის
#  განკუთვნილი სია შემდეგ მომხმარებელს შემოატანინეთ სახელი თუ ეს სახელი
#  იქნება რომელიმე მენტორის სახელი ამ შემთხვევაში ეს სახელი დაემატოს მენტორებისთვის
#  განკუთვნილ სიაში სხვა შემთხვევაში
#  თუარიქნება ეს სახელი მენტორის სახელი დაემატოს ჩვეულებრივი სახელების
#  სიაში შემდეგ კი ორივე დაბეჭდეთ
mentor = ["gabrieli" ,"nika" , "luka" ,  "davit"]
print(mentor)
students = ["gabrieli" ,"davit" , "ana" , "elene" , "saba"]
print(students)
user=input("Enter name :")
if user == "gabrieli" or 'nika' or 'luka' or 'davit':
    mentor.append(user)
else:
    students.append(user)
