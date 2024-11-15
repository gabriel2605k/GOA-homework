# 2) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით 
# სავსე სია შემდეგ კი ამ ფუნქციამ უნდა დააბრუნოს უდიდესი რიცხვი ამ სიიდან
def search_biggest(nums):
    if not nums: 
        return None 
    biggest = num[0]  
    for num in nums:
        if num > biggest:
            biggest = num
    return biggest

სია = [3, 5, 1, 8, 2]
print(search_biggest(list))  
