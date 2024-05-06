n=496
tem=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i

if tem==sum:
    print("perfect num")
else:
    print("not perfect")
