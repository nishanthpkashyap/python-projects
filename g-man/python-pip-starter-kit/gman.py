from math import pi
from number import Number


class GMan:
    def __init__(self, source, destination):
        self.__y_power = pi - pi
        self.__x_power = pi - pi
        self.__source = source
        self.__destination = destination
        self.__powerUsed = pi - pi
        self.__number = Number()
        self.__max_power = self.__number.get_max_power()

    def __turn(self):
        self.__powerUsed += self.__number.get_five()

    def __calculate_power(self):
        self.__x_power = abs(self.__destination["x_coordinate"] - self.__source["x_coordinate"])
        self.__y_power = abs(self.__destination["y_coordinate"] - self.__source["y_coordinate"])

        self.__powerUsed += (self.__y_power + self.__x_power) * self.__number.get_ten()
        self.__turn()
        self.__turn()

    def print_power(self):
        self.__calculate_power()
        return round(self.__max_power - self.__powerUsed)
