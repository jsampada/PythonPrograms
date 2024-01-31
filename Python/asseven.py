#2.	Write a function that takes a list/array of integers as input and returns a new list/array containing only the even numbers from the original list/array.
#Example: Input: [1, 2, 3, 4, 5, 6], Output: [2, 4, 6]

lst1=[1, 2, 3, 4, 5, 6]
lst2=[]
for i in lst1:
    if i%2==0:
        lst2.append(i)
print(lst2)
