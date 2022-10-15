from sys import argv
from toll_calculator import TollCalculator
fast_tag_amount = {}


def get_fast_tag_amount(line):
    return int(line[2])


def get_vehicle_number(line):
    return line[1]


def get_vehicle_type(line):
    return line[1]


def get_vehicle_no_for_toll_calc(line):
    return line[2]


def main():
    toll_calculator = TollCalculator()
    global fast_tag_amount
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        statement = line.split(" ")
        if len(statement) > 1:
            statement[2] = statement[2][:-1]
        what_to_do = statement[0]
        if what_to_do == "FASTAG":
            TollCalculator.update_fast_tag(get_vehicle_number(statement), get_fast_tag_amount(statement))
        elif what_to_do == "COLLECT_TOLL":
            vehicle_no = get_vehicle_no_for_toll_calc(statement)
            vehicle_type = get_vehicle_type(statement)
            TollCalculator.update_details(vehicle_no, vehicle_type)
            TollCalculator.collect_toll(vehicle_no, vehicle_type)
        elif what_to_do == "PRINT_COLLECTION":
            TollCalculator.print_collection()


if __name__ == "__main__":
    main()
