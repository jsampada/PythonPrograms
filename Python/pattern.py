print("Number Pattern ")
row = 4
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")

print("Number Pattern ")
row = 4
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print('*', end=' ')
    print("")
'''
Number=int(input("enter a numner="))

for i in range(1,Number+1,1):
    sum=+i
print("sum is=",sum)
'''

s = 0
n = int(input("Enter number "))
for i in range(1, n + 1, 1):
    s += i
print("\n")
print("Sum is: ", s)

