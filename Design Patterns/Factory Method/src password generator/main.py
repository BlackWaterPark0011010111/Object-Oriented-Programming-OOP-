from password_generator_factory import PasswordGeneratorFactory

def display_menu():
    print("\n Password Generator")
    print("1 - Letters only (Alpha)")
    print("2 - Letters and numbers (AlphaNumeric)")
    print("3 - Exit")

def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (8-64): "))
            if 8 <= length <= 64:
                return length
            print("please enter a number between 8 and 64")
        except ValueError:
            print("invalid input. enter a number.")
