def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.

    Formula: BMI = weight (kg) / (height (m) * height (m))
    """
    bmi = weight / (height * height)
    return bmi


def interpret_bmi(bmi):
    """
    Interpret BMI value and return corresponding category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are in the {category} category.")


if __name__ == "__main__":
    main()
