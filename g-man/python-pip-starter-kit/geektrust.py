from sys import argv
from gman import GMan
from number import Number
from get_input import GetInput


class MainClass:
    def __init__(self):
        self.__get_input = GetInput()
        self.__number = Number()
        self.__source = {}
        self.__destination = {}

    def main(self):

        if len(argv) != self.__number.get_two():
            raise Exception("File path not entered")
        file_path = argv[1]
        f = open(file_path, 'r')
        lines = f.readlines()

        for i in lines:
            line = i.split(" ")

            if line[0] == "SOURCE":
                self.__source = self.__get_input.get_source(line)

            elif line[0] == "DESTINATION":
                self.__destination = self.__get_input.get_destination(line)

            elif line[0] == "PRINT_POWER":
                g_man = GMan(self.__source, self.__destination)
                print(f'POWER {g_man.print_power()}')


if __name__ == "__main__":
    main_class = MainClass()
    main_class.main()
