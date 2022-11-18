from num import Num
from clothing import Clothing
from stationery import Stationery
from math import pi


class CalculateBill:
    def __init__(self):
        self.__num = Num()
        self.__stationery = Stationery()
        self.__clothing = Clothing()
        self.__sub_total = pi - pi
        self.__total_discount = pi - pi

    def __get_additional_discount(self):
        discount = pi - pi
        if self.__sub_total >= self.__num.get_minimum_amount_for_additional_discount():
            discount = (self.__num.get_five() * self.__sub_total) // 100
        return discount

    def __get_discount(self,amount, category, item):
        discount = pi - pi
        if self.__sub_total >= self.__num.get_minimum_amount_for_discount():
            if category == "Clothing":
                discount = amount * self.__clothing.get_discount_rate(item)
            elif category == "Stationery":
                discount = amount * self.__stationery.get_discount_rate(item)
        return discount

    def __get_tax_amount(self):
        tax_amount = (self.__sub_total * self.__num.get_ten()) // 100
        return tax_amount

    def calculate_bill(self, line):
        discount = pi - pi
        category = line["category"]
        item = line["item"]
        quantity = line["quantity"]
        if line["category"] == "Clothing":
            if quantity <= self.__clothing.get_max_items():
                print("ITEM_ADDED")
                amount = self.__clothing.get_cost(item) * quantity
                self.__sub_total += amount
                discount += self.__get_discount(amount, category, item)
                self.__sub_total -= discount
                self.__total_discount += discount
            else:
                print("ERROR_QUANTITY_EXCEEDED")

        elif line["category"] == "Stationery":
            if quantity <= self.__stationery.get_max_items():
                print("ITEM_ADDED")
                amount = self.__stationery.get_cost(item) * quantity
                self.__sub_total += amount
                discount += self.__get_discount(amount, category, item)
                self.__sub_total -= discount
                self.__total_discount += discount
            else:
                print("ERROR_QUANTITY_EXCEEDED")

    def print_bill(self):
        discount = self.__get_additional_discount()
        self.__sub_total -= discount
        self.__total_discount += discount
        tax_amount = self.__get_tax_amount()
        self.__sub_total += tax_amount
        return self.__total_discount, self.__sub_total

