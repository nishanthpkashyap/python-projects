class Clothing:
    def __init__(self):
        self.__tshirt_cost = 1000
        self.__tshirt_discount_rate = 0.1
        self.__cap_cost = 500
        self.__cap_discount_rate = 0.2
        self.__jacket_cost = 2000
        self.__jacket_discount_rate = 0.05
        self.__max_items = 2

    def get_max_items(self):
        return self.__max_items

    def get_cost(self, item):
        if item == "TSHIRT":
            return self.__tshirt_cost
        elif item == "JACKET":
            return self.__jacket_cost
        elif item == "CAP":
            return self.__cap_cost

    def get_discount_rate(self, item):
        if item == "TSHIRT":
            return self.__tshirt_discount_rate
        elif item == "JACKET":
            return self.__jacket_discount_rate
        elif item == "CAP":
            return self.__cap_discount_rate


