import math

class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def get_area(self) -> float:
        return self._width * self._height

    def get_perimeter(self) -> float:
        return 2 * (self._width + self._height)

    def get_diagonal(self) -> float:
        return math.sqrt(self._width ** 2 + self._height ** 2)

    def get_width(self) -> float:
        return self._width

    def get_height(self) -> float:
        return self._height


def print_rectangle_properties(rectangle):
    print("Width:", rectangle.get_width())
    print("Height:", rectangle.get_height())
    print("Area:", rectangle.get_area())
    print("Perimeter:", rectangle.get_perimeter())
    print("Diagonal:", rectangle.get_diagonal())
    print()


if __name__ == "__main__":
    rect1 = Rectangle(5.0, 3.0)
    rect2 = Rectangle(7.2, 4.5)

    print_rectangle_properties(rect1)
    print_rectangle_properties(rect2)
