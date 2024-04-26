def cube(num):
    return num ** 3

def main():
    try:
        num = float(input("Enter a number to calculate its cube: "))
        result = cube(num)
        print(f"The cube of {num} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
