from typing import Dict, Union, Literal, List
import json

# Определяем тип Config с использованием всех возможностей системы типов
# Dict[str, Union[...]] создает гибкую структуру конфигурации, где:
# - Ключи всегда строки ->[str,
# - Значения могут быть: строками, числами, списками строк или вложенными словарями ->  str,int,List[str], Dict
# Вложенные словари могут содержать: булевы значения, числа с плавающей точкой 
# или конкретные строковые значения (Literal) ->Union[bool, float, Literal["enable", "disable"]]
Config = Dict[
    str,
    Union[
        str,
        int,
        List[str],
        Dict[str, Union[bool, float, Literal["enable", "disable"]]]  #literal- для точных значений
    ]
]

def validate_config(config: Config) -> bool:
    """Проверяет структуру и типы конфигурации на соответствие требованиям
    должны присутствовать все обязательные ключи и все значения имеют правильный тип
    Возвращает True только если все проверки пройдены"""
    required_keys = {"api_key", "timeout", "plugins", "settings"}  #обязательные поля
    if not all(key in config for key in required_keys):
        return False
    
    # Проверка типов с isinstance и Literal значений
    return (isinstance(config["api_key"], str) and 
            isinstance(config["timeout"], int) and
            isinstance(config["plugins"], list) and
            all(isinstance(p, str) for p in config["plugins"]) and
            isinstance(config["settings"], dict) and
            config["settings"].get("mode") in ["enable", "disable", None])  #проверка Literal

def save_config(config: Config, path: str) -> None:
    """Сериализуем конфигурацию в JSON файл
    Использует красивое форматирование (indent=2) и создает или перезаписывает файл по указанному пути"""
    with open(path, 'w') as f:
        json.dump(config, f, indent=2)

def load_config(path: str) -> Config:
    """Здесь мы загружаем конфигурацию из JSON файла
    Возвращает распарсенный словарь конфигурации и файл должен существовать и содержать валидный JSON соответствующего формата"""
    with open(path) as f:
        return json.load(f)

if __name__ == "__main__":
    # Полноценный конфиг,все поддерживаемые типы
    valid_config: Config = {
        "api_key": "12345",  # токен для API
        "timeout": 10,  #в секундах
        "plugins": ["plugin1", "plugin2"],  #список активных плагинов
        "settings": {
            "debug": False,  # флаг отладки
            "threshold": 0.5,  # Пороговое значение
            "mode": "enable"  # Режим работы только если enable/disable
        }
    }  
    
    print("Конфиг валиден?", validate_config(valid_config))  #должно быть True
    
    # прорабатываем полный цикл, сохраняем → загружаем → используем
    save_config(valid_config, "config.json")  # сохраняем на диск
    loaded_config = load_config("config.json")  # загрузка с диска
    print("Загруженный конфиг:", loaded_config)  # Должен совпадать с оригиналом 