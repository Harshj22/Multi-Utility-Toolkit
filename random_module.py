import random
import string

def random_number():
    start_text = input("Enter start of range: ")
    end_text = input("Enter end of range: ")

    try:
        start = int(start_text)
        end = int(end_text)
        if start > end:
            print("Start should be less than or equal to end.")
        else:
            value = random.randint(start, end)
            print("Random Number:", value)
    except ValueError:
        print("Please enter valid integer values.")


def random_choice_from_list():
    items_text = input("Enter items separated by commas: ")
    items = [item.strip() for item in items_text.split(",") if item.strip() != ""]
    if not items:
        print("No items provided.")
        return

    choice = random.choice(items)
    print("Random Choice:", choice)


def random_password():
    length_text = input("Enter password length: ")
    try:
        length = int(length_text)
        if length <= 0:
            print("Length should be positive.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid integer.")


def random_otp():
    otp = "".join(str(random.randint(0, 9)) for _ in range(6))
    print("Generated OTP:", otp)

