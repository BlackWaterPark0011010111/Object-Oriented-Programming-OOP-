from password_generator import AlphaGenerator, AlphaNumericGenerator

#фабричный класс для создания генераторов паролей
class PasswordGeneratorFactory:
    @staticmethod
    def create_object(generator_type):
        if generator_type == "Alpha":
            return AlphaGenerator()
        elif generator_type == "AlphaNumeric":
            return AlphaNumericGenerator()
        else:
            print("ошибка: неизвестный тип генератора")
            return None
