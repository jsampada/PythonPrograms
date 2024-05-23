L=[]
i=0
while(i<5):
    data=int(input("enter"))
    L.insert(i,data)
    i+=1
k=list(map(lambda num:num+10,L))
print(k)
