n=int(input("Enter number : "))
sum=0
while n!=0:
    rem=n%10
    sum=sum+rem
    n=n//10
print("sum of number is:",sum)