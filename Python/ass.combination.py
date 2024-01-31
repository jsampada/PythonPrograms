# 5.	Write a program to find all pairs of elements in a list that sum up to a given target value.
# numbers = [2, 4, 5, 3, 1, 6, 8, 9, 7]
# target_sum = 10
# Output: [(4, 6), (5, 5), (3, 7), (1, 9)]

numbers = [2, 4, 5, 3, 1, 6, 8, 9, 7]
num2=[]
for i in numbers:
    for j in numbers:
        if i==j & j==i:
            break;
        elif i+j==10:
             num2.append([i,j])
print(num2)
