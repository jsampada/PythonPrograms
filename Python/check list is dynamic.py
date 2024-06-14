l=[]
while(True):
    data=int(input("enter data"))
    l.append(data)
    print("do you want to addd data")
    print("press 1 to add data or press 2 to not add: ")
    choice=(int(input()))
    if choice==1:
        continue
    else:
        break
print(l)