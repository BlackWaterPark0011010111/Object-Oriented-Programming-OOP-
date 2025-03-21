from password_generator_factory import PasswordGeneratorFactory

# запуск, чтобы пользователь мог выбрать генератор
if __name__ == "__main__":
    print("выберите тип пароля:")
    print("1 - только буквы (Alpha)")
    print("2 - буквы и цифры (AlphaNumeric)")
    
    choice = input("введите 1 или 2: ")
    generator_type = "Alpha" if choice == "1" else "AlphaNumeric" if choice == "2" else None

    if generator_type:
        generator = PasswordGeneratorFactory.create_object(generator_type)
        if generator:
            length = int(input("введите длину пароля: "))
            print("сгенерированный пароль:", generator.generate(length))
    else:
        print("неправильный ввод, попробуйте снова")
