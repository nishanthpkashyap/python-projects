class Stationery:
    def __init__(self):
        self.__notebook_cost = 200
        self.__notebook_discount_rate = 0.2
        self.__pens_cost = 300
        self.__pens_discount_rate = 0.1
        self.__markers_cost = 500
        self.__markers_discount_rate = 0.05
        self.__max_items = 3

    def get_max_items(self):
        return self.__max_items

    def get_cost(self, item):
        if item == "NOTEBOOK":
            return self.__notebook_cost
        elif item == "PENS":
            return self.__pens_cost
        elif item == "MARKERS":
            return self.__markers_cost

    def get_discount_rate(self, item):
        if item == "NOTEBOOK":
            return self.__notebook_discount_rate
        elif item == "PENS":
            return self.__pens_discount_rate
        elif item == "MARKERS":
            return self.__markers_discount_rate