num = int(input("Enter a number: "))
if num < 0:
    print("Error: Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial:", factorial)
