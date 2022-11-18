class Num:
    def __init__(self):
        self.__two = 2
        self.__five = 5
        self.__ten = 10
        self.__two_hundred = 200
        self.__thousand = 1000
        self.__three_thousand = 3000

    def get_minimum_amount_for_discount(self):
        return self.__thousand

    def get_minimum_amount_for_additional_discount(self):
        return self.__three_thousand

    def get_two(self, ):
        return self.__two

    def get_five(self):
        return self.__five

    def get_ten(self):
        return self.__ten

    def get_max_power(self):
        return self.__two_hundred
