from abc import ABC, abstractmethod
import math

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimetr(self):
        return 4 * self.__side

class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def  area(self):
        return self.__length * self.__width

    def perimetr(self):
        return 2 * (self.__width + self.__length)

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimetr(self):
        return 2 * math.pi * self.__radius


figures = [Square(5), Rectangle(4, 6), Circle(3)]
for figure in figures:
    print(f"{figure.__class__.__name__}")
    print(f"Площа: {figure.area():.2f}")
    print(f"Периметр: {figure.perimetr() :.2f}")
    print("-" * 20)
