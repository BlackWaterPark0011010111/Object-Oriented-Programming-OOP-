from typing import Dict, Union, Literal, List
import json

# Определяем тип Config с использованием всех возможностей системы типов
# Dict[str, Union[...]] создает гибкую структуру конфигурации, где:
# - Ключи всегда строки
# - Значения могут быть: строками, числами, списками строк или вложенными словарями
# Вложенные словари могут содержать: булевы значения, числа с плавающей точкой 
# или конкретные строковые значения (Literal)
Config = Dict[
    str,
    Union[
        str,
        int,
        List[str],
        Dict[str, Union[bool, float, Literal["enable", "disable"]]]  # Literal для точных значений
    ]
]

def validate_config(config: Config) -> bool:
    """Проверяет структуру и типы конфигурации на соответствие требованиям
    Убеждается, что:
    - Присутствуют все обязательные ключи
    - Все значения имеют правильный тип
    Возвращает True только если все проверки пройдены"""
    required_keys = {"api_key", "timeout", "plugins", "settings"}  # Обязательные поля
    if not all(key in config for key in required_keys):
        return False
    
    # Проверка типов с использованием isinstance и Literal значений
    return (isinstance(config["api_key"], str) and 
            isinstance(config["timeout"], int) and
            isinstance(config["plugins"], list) and
            all(isinstance(p, str) for p in config["plugins"]) and
            isinstance(config["settings"], dict) and
            config["settings"].get("mode") in ["enable", "disable", None])  # Проверка Literal

def save_config(config: Config, path: str) -> None:
    """Сериализует конфигурацию в JSON файл
    Использует красивое форматирование (indent=2)
    Создает или перезаписывает файл по указанному пути"""
    with open(path, 'w') as f:
        json.dump(config, f, indent=2)

def load_config(path: str) -> Config:
    """Загружает конфигурацию из JSON файла
    Возвращает распарсенный словарь конфигурации
    Файл должен существовать и содержать валидный JSON соответствующего формата"""
    with open(path) as f:
        return json.load(f)

# Демонстрация работы с конфигурацией
if __name__ == "__main__":
    # Полноценный пример конфига, демонстрирующий все поддерживаемые типы
    valid_config: Config = {
        "api_key": "12345",  # Токен для API
        "timeout": 10,  #в секундах
        "plugins": ["plugin1", "plugin2"],  # Список активных плагинов
        "settings": {
            "debug": False,  # Флаг отладки
            "threshold": 0.5,  # Пороговое значение
            "mode": "enable"  # Режим работы (только "enable"/"disable")
        }
    }  
    
    print("Конфиг валиден?", validate_config(valid_config))  # Должно быть True
    
    # Полный цикл: сохраняем → загружаем → используем
    save_config(valid_config, "config.json")  # Сохраняем на диск
    loaded_config = load_config("config.json")  # Загружаем с диска
    print("Загруженный конфиг:", loaded_config)  # Должен совпадать с оригиналом