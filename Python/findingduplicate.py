lst1=['a','b','c','b','d','c']
duplicate=[]
for i in lst1:
    if lst1.count(i)>1:
        if i not in duplicate:
            duplicate.append(i)
print(duplicate)