def convertToBin(a):

   if a > 1:

       convertToBin(a//2)

   print(a % 2,end = '')


# decimal number

d = 34
convertToBin(d)

print()