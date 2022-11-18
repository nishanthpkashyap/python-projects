from sys import argv
from num import Num
from getInput import GetInput
from calculate_bill import CalculateBill


def main():
    num = Num()
    get_input = GetInput()
    calculate_bill = CalculateBill()
    if len(argv) != num.get_two():
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        inputs = line.split(" ")
        if inputs[0] == "ADD_ITEM":
            inp = get_input.get_add_item(inputs)
            calculate_bill.calculate_bill(inp)
        elif inputs[0] == "PRINT_BILL":
            discount, amount = calculate_bill.print_bill()
            print(f'TOTAL_DISCOUNT {format(discount, ".2f")}')
            print(f'TOTAL_AMOUNT_TO_PAY {format(amount, ".2f")}')


if __name__ == "__main__":
    main()
