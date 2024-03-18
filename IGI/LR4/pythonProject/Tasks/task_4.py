import abc
from abc import ABC
import sys
from termcolor import colored, cprint


class Shape(abc.ABC):
    @abc.abstractmethod
    def get_area(self):
        pass


class ShapeColor:

    def __init__(self, color):
        self.__color = color

    def set_color(self, new_color):
        self.__color = new_color

    def get_color(self):
        return self.__color

    def del_color(self):
        del self.__color

    color = property(set_color,get_color, del_color)


class SquareMixin:
    def add_size(self, size):
        self.__size = size

    def get_area(self):
        return self.__size ** 2

    def get_perimetr(self):
        return self.__size * 4


class Square(SquareMixin, Shape):
    def __str__(self):
        return '{0} shape, area: {1}'.format(self.__class__.__name__,  self.get_area())


class Hexagon(Shape, ABC):

    def __init__(self, a, color):
        self.__shape_color = ShapeColor(color)
        self.__signature = ""
        self.__string_representation = []
        if a > 0:
            self.__a = a

    def get_area(self):
        if self.__a > 0:
            return 3 * 3 ** 0.5 / 2 * self.__a ** 2

    def print_figure(self):
        pass

    def __str__(self):
        return '{0} shape, color: {1}, size: {2}, area: {3}'.format(self.__class__.__name__, self.__shape_color,self.__a, self.get_area())

    def save_in_file(self, path_to_file):
        with open(path_to_file, 'w+') as file:
            try:
                file.writelines(self.__string_representation)
                file.close()
            except BaseException:
                print('Something went wrong')

    def get_signature(self):
        return self.__signature

    def sign_figure(self, text):
        if text != "":
            self.__signature = text


def task4():
    hexagon = Hexagon(12, 432)
    print(hexagon, hexagon.get_area())
    hexagon.print_figure()

    square = Square()
    square.add_size(12)
    print(square.get_area())
    print(square.get_perimetr())
    print(square)
