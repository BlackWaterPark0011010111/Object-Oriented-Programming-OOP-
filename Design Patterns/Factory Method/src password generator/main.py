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

def main():
    while True:
        display_menu()
        choice = input("your choice (1-3): ").strip()
        
        if choice == '3':
            print("bye!")
            break
            
        generator_type = None
        if choice == '1':
            generator_type = "Alpha"
        elif choice == '2':
            generator_type = "AlphaNumeric"
        else:
            print("invalid choice. try again.")
            continue
        

if __name__ == "__main__":
    main()