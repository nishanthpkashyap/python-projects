from math import pi



class TollCalculator:
    __total_discount = pi - pi
    __flat_fee = pi - pi
    __total_cash_collected = pi - pi
    __total_fast_tag_amount_collected = pi - pi
    __number_of_journeys = {}
    __vehicle_type_summary = {}
    __vehicle_type_amount = {}
    __toll_charge_for_each_vehicle = {"TRUCK": 200, "BUS": 200, "VAN": 100, "CAR": 100, "RICKSHAW": 100, "SCOOTER": 50,
                                      "MOTORBIKE": 50}
    __fast_tag_amount_left = {}

    @classmethod
    def update_fast_tag(cls, vehicle_number, fast_tag_amount):
        try:
            TollCalculator.__fast_tag_amount_left[vehicle_number] += fast_tag_amount
        except KeyError:
            TollCalculator.__fast_tag_amount_left[vehicle_number] = fast_tag_amount

    @classmethod
    def update_details(cls, vehicle_no, vehicle_type):
        try:
            cls.__vehicle_type_summary[vehicle_type] += 1
        except KeyError:
            cls.__vehicle_type_summary[vehicle_type] = 1
        finally:
            try:
                cls.__number_of_journeys[vehicle_no] += 1
            except KeyError:
                cls.__number_of_journeys[vehicle_no] = 1

    @classmethod
    def collect_toll(cls, vehicle_no, vehicle_type):

        cls.__calculate_amount(vehicle_no, vehicle_type)
        cls.__calculate_discount(vehicle_no, vehicle_type)

    @classmethod
    def __sort_dictionary(cls):
        lis = TollCalculator.__dictionary_to_list()
        lis = sorted(lis, reverse=True)
        for i in lis:
            print(f'{i[1]} {TollCalculator.__vehicle_type_summary[i[1]]}', end=" ")

    @classmethod
    def print_collection(cls):
        fast_tag_amount = TollCalculator.__total_fast_tag_amount_collected
        discount_amount = TollCalculator.__total_discount
        cash_amount = TollCalculator.__total_cash_collected - discount_amount + TollCalculator.__flat_fee
        total_amount_collected = fast_tag_amount + cash_amount
        print(f'TOTAL_COLLECTION {format(total_amount_collected,".0f")} {format(discount_amount,".0f")}')
        print(f'PAYMENT SUMMARY {format(fast_tag_amount,".0f")} {format(cash_amount, ".0f")}')
        print("VEHICLE_TYPE_SUMMARY", end=" ")
        TollCalculator.__sort_dictionary()

    @classmethod
    def __dictionary_to_list(cls):
        lis = []
        vehicle_amount = TollCalculator.__vehicle_type_amount
        for i in vehicle_amount.keys():
            lis.append([vehicle_amount[i], i])
        return lis

    @classmethod
    def __get_flat_fee(cls):
        return 40

    @classmethod
    def __calculate_discount(cls, vehicle_no, vehicle_type):
        if cls.__number_of_journeys[vehicle_no] >= 2:
            discount_amount = TollCalculator.__toll_charge_for_each_vehicle[vehicle_type]//2
            TollCalculator.__total_discount += discount_amount
            TollCalculator.__vehicle_type_amount[vehicle_type] -= discount_amount

    @classmethod
    def __update_vehicle_amount(cls, vehicle_no, vehicle_type, cash_to_be_paid=0, flat_fee=0):
        try:
            cls.__vehicle_type_amount[vehicle_type] += cls.__fast_tag_amount_left[vehicle_no] + cash_to_be_paid +\
                                                       flat_fee
        except KeyError:
            cls.__vehicle_type_amount[vehicle_type] = cls.__fast_tag_amount_left[vehicle_no] + cash_to_be_paid +\
                                                       flat_fee

    @classmethod
    def __calculate_amount(cls, vehicle_no, vehicle_type):
        toll_charge = cls.__toll_charge_for_each_vehicle[vehicle_type]
        flat_fee = cls.__get_flat_fee()
        try:
            fast_tag_amount_left = cls.__fast_tag_amount_left[vehicle_no]
        except KeyError:
            cls.__fast_tag_amount_left[vehicle_no] = pi - pi
            fast_tag_amount_left = cls.__fast_tag_amount_left[vehicle_no]
        finally:
            if fast_tag_amount_left < toll_charge:
                cash_to_be_paid = abs(toll_charge - fast_tag_amount_left)
                cls.__total_cash_collected += cash_to_be_paid
                cls.__update_vehicle_amount(vehicle_no, vehicle_type, cash_to_be_paid, flat_fee)
                cls.__total_fast_tag_amount_collected += fast_tag_amount_left
                cls.__fast_tag_amount_left[vehicle_type] = 0
                cls.__flat_fee += flat_fee
            else:
                cls.__fast_tag_amount_left[vehicle_no] -= toll_charge
                cls.__update_vehicle_amount(vehicle_no, vehicle_type, 0, 0)
                cls.__total_fast_tag_amount_collected += toll_charge
