from sys import argv
from stationery import Stationery

MAXIMUM_QUANTITY = {"TSHIRT": 2, "JACKET": 2, "CAP": 2, "NOTEBOOK": 3, "PENS": 3, "MARKERS": 3}


def main():
    # Sample code to read inputs from the file
    global MAXIMUM_QUANTITY
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()

    for line in lines:

        order = line.split(" ")

        if len(order) > 1:
            order[2] = int(order[2])

        stationery = Stationery()

        if order[0] == "PRINT_BILL":
            stationery.print_bill()

        elif order[0] == "ADD_ITEM":
            if order[2] <= MAXIMUM_QUANTITY[order[1]]:
                stationery.add_item(order)
            else:
                print("ERROR_QUANTITY_EXCEEDED")


if __name__ == "__main__":
    main()



