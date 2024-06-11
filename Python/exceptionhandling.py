a=int(input("enter num"))
b=int(input("enter num"))
try:
    c=a/b
except Exception as e:
    print("no is not div by 0")
print(c)
print("program end")