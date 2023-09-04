num =int(input("eneter num"))
reverse = int(str(num)[::-1])

if num == reverse:
    print('Palindrome')
else:
    print("Not Palindrome")