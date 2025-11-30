from datetime import datetime
import time

def show_current_datetime():
    now = datetime.now()
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted)


def difference_between_dates():
    first_date = input("Enter the first date (YYYY-MM-DD): ")
    second_date = input("Enter the second date (YYYY-MM-DD): ")

    try:
        d1 = datetime.strptime(first_date, "%Y-%m-%d")
        d2 = datetime.strptime(second_date, "%Y-%m-%d")
        difference = abs(d2 - d1)
        print("Difference:", difference.days, "days")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


def format_date():
    date_text = input("Enter a date (YYYY-MM-DD): ")
    try:
        d = datetime.strptime(date_text, "%Y-%m-%d")
        print("Choose output format:")
        print("1. DD-MM-YYYY")
        print("2. MM/DD/YYYY")
        print("3. Full format (04 January 2025)")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Formatted Date:", d.strftime("%d-%m-%Y"))
        elif choice == "2":
            print("Formatted Date:", d.strftime("%m/%d/%Y"))
        elif choice == "3":
            print("Formatted Date:", d.strftime("%d %B %Y"))
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


def stopwatch():
    input("Press Enter to start the stopwatch.")
    start = time.time()
    input("Press Enter to stop the stopwatch.")
    end = time.time()
    elapsed = end - start
    print("Elapsed time:", round(elapsed, 2), "seconds")


def countdown_timer():
    seconds_text = input("Enter time in seconds: ")
    try:
        seconds = int(seconds_text)
        while seconds > 0:
            print("Remaining:", seconds, "seconds", end="\r")
            time.sleep(1)
            seconds = seconds - 1
        print("\nTime is up.")
    except ValueError:
        print("Please enter a valid integer value.")


