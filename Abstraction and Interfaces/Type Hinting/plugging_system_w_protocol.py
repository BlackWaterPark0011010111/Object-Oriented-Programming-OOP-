from typing import Protocol, List

class Plugin(Protocol):
    def load(self) -> None:
        ...

    def run(self, data: str) -> str:
        ...

class UppercasePlugin:
    def load(self) -> None:
        print("Plugin loaded!")

    def run(self, data: str) -> str:
        return data.upper()

class ReversePlugin:
    def load(self) -> None:
        print("Reverse plugin loaded!")

    def run(self, data: str) -> str:
        return data[::-1]

def process_with_plugins(data: str, plugins: List[Plugin]) -> str:
    result = data
    for plugin in plugins:
        result = plugin.run(result)
    return result

# Пример
if __name__ == "__main__":
    plugins: List[Plugin] = [UppercasePlugin(), ReversePlugin()]
    print("Result:", process_with_plugins("hello", plugins))  # "OLLEH"