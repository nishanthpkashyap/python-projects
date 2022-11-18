class GetInput:
    def __init__(self):
        self.__add_item = {}

    def get_add_item(self, line):
        self.__add_item = {"command": line[0], "item": line[1], "quantity": int(line[2][0]),
                           "category": self.__get_category(line[1])}
        return self.__add_item

    def __get_category(self, item):
        if item == "CAP" or item == "JACKET" or item == "TSHIRT":
            return "Clothing"
        elif item == "NOTEBOOK" or item == "PENS" or item == "MARKERS":
            return "Stationery"
