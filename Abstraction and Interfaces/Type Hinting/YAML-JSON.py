from typing import Dict, Union, Literal, List
import json

#Defining Config type using all type system capabilities
#dict[str, Union[...]] creates a flexible configuration structure where:
#Keys are always strings -> [str,
#values can be: strings, integers, string lists or nested dictionaries -> str, int, List[str], Dict
#nested dictionaries can contain: boolean values, floating-point numbers
#or specific string values (Literal) -> Union[bool, float, Literal["enable", "disable"]]
Config = Dict[
    str,
    Union[
        str,
        int,
        List[str],
        Dict[str, Union[bool, float, Literal["enable", "disable"]]]  # literal for exact values
    ]
]

def validate_config(config: Config) -> bool:
    """Validates configuration structure and types against requirements
    Must contain all mandatory keys and all values must have correct types
    Returns True only if all checks pass"""
    required_keys = {"api_key", "timeout", "plugins", "settings"}  #mandatory fields
    if not all(key in config for key in required_keys):
        return False
    
    #Type checking with isinstance and Literal values
    return (isinstance(config["api_key"], str) and 
            isinstance(config["timeout"], int) and
            isinstance(config["plugins"], list) and
            all(isinstance(p, str) for p in config["plugins"]) and
            isinstance(config["settings"], dict) and
            config["settings"].get("mode") in ["enable", "disable", None])  #Literal check

def save_config(config: Config, path: str) -> None:
    """Serializes configuration to JSON file
    Uses pretty formatting (indent=2) and creates/overwrites file at specified path"""
    with open(path, 'w') as f:
        json.dump(config, f, indent=2)

def load_config(path: str) -> Config:
    """Here we load configuration from JSON file
    Returns parsed configuration dictionary and file must exist and contain valid JSON of matching format"""
    with open(path) as f:
        return json.load(f)

if __name__ == "__main__":
    #Complete config with all supported types
    valid_config: Config = {
        "api_key": "12345",  #API token
        "timeout": 10,  #in seconds
        "plugins": ["plugin1", "plugin2"],  #active plugins list
        "settings": {
            "debug": False,  #debug flag
            "threshold": 0.5,  #Threshold value
            "mode": "enable"  #Operation mode only enable/disable
        }
    }   
    
    print("Config valid?", validate_config(valid_config))  #should be True
    
    #Working through full cycle: save → load → use
    save_config(valid_config, "config.json")  #save to disk
    loaded_config = load_config("config.json")  #load from disk
    print("Loaded config:", loaded_config)  #Should match original