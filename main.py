import time_module
import math_module
import random_module
import uuid_module
import file_module
import explore_module


def time_menu():
    while True:
        print("\n========================")
        print("Time and Date Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format a date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            time_module.show_current_datetime()
        elif choice == "2":
            time_module.difference_between_dates()
        elif choice == "3":
            time_module.format_date()
        elif choice == "4":
            time_module.stopwatch()
        elif choice == "5":
            time_module.countdown_timer()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


def math_menu():
    while True:
        print("\n========================")
        print("Mathematical Operations:")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry values")
        print("4. Area of shapes")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            math_module.factorial_calculator()
        elif choice == "2":
            math_module.compound_interest()
        elif choice == "3":
            math_module.trigonometry_values()
        elif choice == "4":
            math_module.area_menu()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def random_menu():
    while True:
        print("\n========================")
        print("Random Operations:")
        print("1. Random number")
        print("2. Random choice from list")
        print("3. Random password")
        print("4. Random OTP")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            random_module.random_number()
        elif choice == "2":
            random_module.random_choice_from_list()
        elif choice == "3":
            random_module.random_password()
        elif choice == "4":
            random_module.random_otp()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def uuid_menu():
    while True:
        print("\n========================")
        print("UUID Operations:")
        print("1. Generate UUID (v4)")
        print("2. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            uuid_module.generate_uuid()
        elif choice == "2":
            break
        else:
            print("Invalid choice.")


def file_menu():
    while True:
        print("\n========================")
        print("File Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            file_module.create_file()
        elif choice == "2":
            file_module.write_file()
        elif choice == "3":
            file_module.read_file()
        elif choice == "4":
            file_module.append_file()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def explore_menu():
    print("\n========================")
    print("Explore Module Attributes using dir():")
    explore_module.explore_module_attributes()


def main_menu():
    while True:
        print("\n========================")
        print("Welcome to Multi-Utility Toolkit")
        print("========================\n")
        print("Choose an option:")
        print("1. Time and Date Operations")
        print("2. Mathematical Operations")
        print("3. Random Operations")
        print("4. UUID Operations")
        print("5. File Operations")
        print("6. Explore Module Attributes (dir)")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            time_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_menu()
        elif choice == "7":
            print("Thank you for using the Multi-Utility Toolkit.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()

