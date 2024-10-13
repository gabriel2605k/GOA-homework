# 2) შექმენით სია სადაც იქნება 10 სახელი
#  შემდეგ ამ სიიდან ამოშლით ყველა იმ სახელს
#  რომელიც იწყება ა ასოზე და დაბეჭდეთ გაფილტრული სია
name_list = ['gabreli','gio','nika', 'ana' , 'anano' , 'luka' , ' gaga' , 'mari' , 'elene','emili']
final_list= []

for i in range(len(name_list)):
    if name_list[i][0] == 'a':
        final_list.append(name_list[i])
print(final_list)