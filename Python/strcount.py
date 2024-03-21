# def count_letters(S):
#   a={}
#   for i in S:
#     a[i]=S.count(i)
#   return a
#   """if _name_ == "_main_":
#     S = input()
#     d = count_letters(S)"""


str=input("enter paln")
str1=str[::-1]
if str==str1:
  print("p")
else:
  print("not p")


str1=input("enter string : ")
b=str1[::-1]
if str1==b:
    print("palindrome")
else:
    print("not palindrome")