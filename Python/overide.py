n=[1,2,3,7,5]
a=sorted(n)
print(a)
for i in range(len(a)):
    if a[i]!=i+1:
        print("missing value is",i+1)
        break


