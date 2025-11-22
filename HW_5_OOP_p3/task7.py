# 7. Создайте протокол Shape, который требует реализации метода area() для вычисления площади фигуры. Реализуйте несколько классов, таких как Circle, Rectangle и Triangle, которые будут реализовывать данный протокол. 
# Напишите функцию, которая принимает объекты, реализующие протокол Shape, и выводит их площадь.
# Протокол Shape должен содержать метод area().
# Классы Circle, Rectangle и Triangle должны реализовывать метод area(), соответствующий их геометрической форме.
# Функция print_area() должна принимать объект, реализующий протокол Shape, и выводить площадь.


from typing import Protocol
import math

class Shape(Protocol):
    def area(self) -> float:
        ...


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


def print_area(shape: Shape):
    print("Площадь равна:", shape.area())


circle = Circle(5)
rect = Rectangle(4, 6)
tri = Triangle(3, 8)

print_area(circle)
print_area(rect)
print_area(tri)
