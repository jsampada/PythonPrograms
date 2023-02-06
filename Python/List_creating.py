list=[1,2,3,4,5,6,7,8,9,10]
print(list)
list1=([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(list1)
lst= range(3, 20, 2)
for n in lst:
  print(n)

#list repeatation
final_lst=list1*2
print(final_lst)
#list count
print(final_lst.count(10))
#index
print(final_lst.index(20))
#min,max,sum function
print(max(final_lst))
print(min(final_lst))
print(sum(final_lst))
#append function
final_lst.append(21)
print(final_lst)

#extend
final_lst.extend([22,23,24,25])
print(final_lst)

#insert
final_lst.insert(1,3)
print(final_lst)

#remove
final_lst.remove(3)
print(final_lst)

#
