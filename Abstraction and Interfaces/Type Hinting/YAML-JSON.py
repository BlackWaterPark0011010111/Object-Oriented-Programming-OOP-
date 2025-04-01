from typing import Dict, Union, Literal, List
import json

Config = Dict[
    str,
    Union[
        str,
        int,
        List[str],
        Dict[str, Union[bool, float]]
    ]
]

def validate_config(config: Config) -> bool:
    required_keys = {"api_key", "timeout", "plugins"}
    if not all(key in config for key in required_keys):
        return False
    return isinstance(config["api_key"], str) and isinstance(config["timeout"], int)

# Пример
if __name__ == "__main__":
    valid_config: Config = {
        "api_key": "12345",
        "timeout": 10,
        "plugins": ["plugin1", "plugin2"]
    }
    print("Is valid?", validate_config(valid_config)) 