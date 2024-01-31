# target
# 6.Implement a binary search algorithm.
#  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]=
#  6
# Output: 5 (index of target)
t=int(input("enter t"))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numbers:
    if i==t:
        print(numbers.index(i))