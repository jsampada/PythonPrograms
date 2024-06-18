lst =[1,1,2,2,4,4,5,6,7,8,1,2,3,4,4,6,7]
#using set
no_duplicate=list(set(lst))
print(no_duplicate)
print(lst)
#without using set
no_duplicate=[]
for ele in lst:
    if ele not in no_duplicate:
        no_duplicate.append(ele)
print(no_duplicate)



str1="my name  is is sampada sampada joshi joshi"
str2=[]
# l=str1.split()
# print(l)
new_string =""
for word in str1.split():
    if word not in str2:
        str2.append(word)
print(str(str2))

for word in str2:
    new_string = new_string + word+" "

print(new_string)
print(" ".join(str2))




nums = [1, 2, 3, 4, 5,1,2,3]
def find_duplicates(nums):
    new_list =[]
    duplicates =[]
    for no in nums:
        if no not in new_list:
            new_list.append(no)
        elif no in new_list:
            duplicates.append(no)
    del new_list
    return duplicates


print(find_duplicates(nums))