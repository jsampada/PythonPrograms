# 8.	Implement a program that checks whether a given string is a palindrome or not.
# [Note : A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, disregarding spaces, punctuation, and capitalization.]
# Example: Input: "Madam", Output: True
a=input("enetr value")
b=a[::-1]
if a==b:
    print("true")
else:
    print("false")