is_magician=False
is_expert=True
if is_expert and is_magician:
    print('You are a master magician')
elif is_expert and not is_magician:
    print('At list you are getting there')
elif not is_magician:
    print('you are not magician')

print(True==1) #true
print(''== 1) #false
print([]==1) #false
print(10==10.0) #true
print([]==[]) #true


print(True is True) #true
print('' == 1) #false
print([]==1) #false
print(10==10) #true
print([]==[]) #true
a=[1,2,3]
b=[1,2,3]
print(a is b)
print(a==b)