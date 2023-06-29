'''my_list=[1,2,3,4,5,6,7,8,9,10]
counter=0
for i in my_list:
    counter=counter+i
print(counter)

print("*****************************")
for i in range(1,11,1):
    print(i)
print("*****************************")
for i in range(1,11,1):
    print("email in email list")
print("*****************************")
for _ in range(1,11,1):
    print(_)
print("*****************************")
#reverce
for i in range(11,1,-1):
    print(i)

print("*****************************")
#convert into list
print(list(range(10)))
for i in range(11,1,-1):
    print(list(range(10)))'''

for i,char in enumerate("Hi Sampada"):
    print(i,char)

for i,char in enumerate(list(range(100))):
    if char is 50:
        print(f'index of 50 =',i)
