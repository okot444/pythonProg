import math
import operator
class Geometric:

    def calculateArea(self):
        print("Calculating area")


class Square(Geometric):
    def __init__(self, a):
        self.side = a

    def _perimeter(self):
        print("Perimeter of Square {}: {}\n".format(self.side, self.side*4))

    def calculateArea(self):
        print("Area of Square {}: {}\n".format(self.side, pow(self.side, 2)))


geom = Geometric()
geom.calculateArea()
sq = Square(5)
sq.calculateArea()
sq._perimeter()
print("Check subclass: ", issubclass(Square, Geometric))
print("Check instance sq->Square: ", isinstance(sq, Square))
print("Check instance sq->Geometric: ", isinstance(sq, Geometric))
print("Check instance sq->dict: ", isinstance(sq, dict))
print("Geometric.__bases__: ", Geometric.__bases__)
print("Square.__bases__: ", Square.__bases__)

# Создайте класс Circle, унаследованный от класса Geometric, для которого определите атрибут radius.
# Сделайте атрибут radius приватным (с использованием двойного подчеркивания).
# Переопределите унаследованный метод calculateArea(), рассчитав площадь окружности
# (значение числа Пи доступно в библиотеке math).


class Circle (Geometric):
    def __init__(self, radius):
        self.__radius = radius

    def calculateArea(self):
        print("Area of Circle with radius={}: {:.3f}".format(self.__radius, 2*math.pi*self.__radius))


mycircle = Circle(5)
mycircle.calculateArea()


