import math


def factorial_calculator():
    number_text = input("Enter a non-negative integer: ")
    try:
        number = int(number_text)
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = math.factorial(number)
            print("Factorial:", result)
    except ValueError:
        print("Please enter a valid integer.")


def compound_interest():
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (in %): "))
        time = float(input("Enter time (in years): "))

        amount = principal * (1 + rate / 100) ** time
        ci = amount - principal

        print("Compound Interest:", round(ci, 2))
        print("Total Amount:", round(amount, 2))

    except ValueError:
        print("Please enter valid numeric inputs.")


def trigonometry_values():
    angle_text = input("Enter angle in degrees: ")
    try:
        angle_degrees = float(angle_text)
        angle_radians = math.radians(angle_degrees)

        print("sin(", angle_degrees, ") =", round(math.sin(angle_radians), 4))
        print("cos(", angle_degrees, ") =", round(math.cos(angle_radians), 4))
        print("tan(", angle_degrees, ") =", round(math.tan(angle_radians), 4))

    except ValueError:
        print("Please enter a valid number.")


def area_menu():
    print("Area of Geometric Shapes:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter your choice: ")

    if choice == "1":
        radius_text = input("Enter radius: ")
        try:
            radius = float(radius_text)
            area = math.pi * (radius ** 2)
            print("Area of Circle:", round(area, 2))
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        length_text = input("Enter length: ")
        width_text = input("Enter width: ")
        try:
            length = float(length_text)
            width = float(width_text)
            area = length * width
            print("Area of Rectangle:", round(area, 2))
        except ValueError:
            print("Please enter valid numbers.")

    elif choice == "3":
        base_text = input("Enter base: ")
        height_text = input("Enter height: ")
        try:
            base = float(base_text)
            height = float(height_text)
            area = 0.5 * base * height
            print("Area of Triangle:", round(area, 2))
        except ValueError:
            print("Please enter valid numbers.")
    else:
        print("Invalid choice.")
