PRICE_BEFORE_DISCOUNT = 0
TOTAL_DISCOUNT = 0.00
PRICE_AFTER_DISCOUNT = 0.00
TOTAL_AMOUNT_TO_PAY = 0.00


class Stationery:

    def __init__(self):
        self.__SALES_TAX = 0.1
        self.__ADDITIONAL_DISCOUNT = 0.05

    def add_item(self, order):
        print("ITEM_ADDED")
        self.__prepare_bill(order)

    def __prepare_bill(self, order):
        global TOTAL_DISCOUNT
        global PRICE_BEFORE_DISCOUNT

        discount_for_each_item = {"TSHIRT": 0.1, "JACKET": 0.05, "CAP": 0.2, "NOTEBOOK": 0.2, "PENS": 0.1,
                                  "MARKERS": 0.05}
        value_of_each_item = {"TSHIRT": 1000, "JACKET": 2000, "CAP": 500, "NOTEBOOK": 200, "PENS": 300, "MARKERS": 500}

        sub_total = order[2] * value_of_each_item[order[1]]
        PRICE_BEFORE_DISCOUNT = PRICE_BEFORE_DISCOUNT + sub_total

        discount = sub_total * discount_for_each_item[order[1]]
        TOTAL_DISCOUNT = TOTAL_DISCOUNT + discount

    def print_bill(self):
        global TOTAL_DISCOUNT
        global PRICE_AFTER_DISCOUNT
        global TOTAL_AMOUNT_TO_PAY

        minimum_price_before_discount = 1000
        minimum_price_for_extra_discount = 3000

        if PRICE_BEFORE_DISCOUNT >= minimum_price_before_discount:
            PRICE_AFTER_DISCOUNT = PRICE_BEFORE_DISCOUNT - TOTAL_DISCOUNT
        else:
            PRICE_AFTER_DISCOUNT = PRICE_BEFORE_DISCOUNT
            TOTAL_DISCOUNT = 0.00

        if PRICE_AFTER_DISCOUNT >= minimum_price_for_extra_discount:
            TOTAL_DISCOUNT = TOTAL_DISCOUNT + (PRICE_AFTER_DISCOUNT * self.__ADDITIONAL_DISCOUNT)
            PRICE_AFTER_DISCOUNT = PRICE_AFTER_DISCOUNT * (1 - self.__ADDITIONAL_DISCOUNT)
        TOTAL_AMOUNT_TO_PAY = PRICE_AFTER_DISCOUNT * (1 + self.__SALES_TAX)
        print(f'TOTAL_DISCOUNT  {format(TOTAL_DISCOUNT, ".2f")}')
        print(f'TOTAL_AMOUNT_TO_PAY  {format(TOTAL_AMOUNT_TO_PAY, ".2f")}')
