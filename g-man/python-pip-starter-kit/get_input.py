class GetInput:
    def __init__(self):
        self.__source = {}
        self.__destination = {}

    def get_source(self, line):
        self.__source = {"x_coordinate": int(line[1]), "y_coordinate": int(line[2]), "direction": line[3][0]}
        return self.__source

    def get_destination(self, line):
        self.__destination = {"x_coordinate": int(line[1]), "y_coordinate": int(line[2])}
        return self.__destination
