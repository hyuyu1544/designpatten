"""Take Housing transaction for example."""
from mediator import Mediator, InteractiveObject


class HouseInfo:
    """House Infomation."""

    def __init__(
        self,
        area,
        price,
        # house_age,
        # room_num,
        # kitchen_num,
        # window_num,
        # bathroom_num,
        address,
        owner
    ):
        self.__area = area
        self.__price = price
        # self.__house_age = house_age
        # self.__room_num = room_num
        # self.__kitchen_num = kitchen_num
        # self.__window_num = window_num
        # self.__bathroom_num = bathroom_num
        self.__address = address
        self.__owner = owner

    def get_address(self):
        return self.__address

    def get_owner(self):
        return self.__owner
        # return self.__owner.get_name()

    def show_info(self):
        print(
            'area: {} mˆ2'.format(self.__area),
            'price: {} TWD'.format(self.__price)
        )


class HouseAgency(Mediator):

    def __init__(self):
        self.__house_list = []

    def add_house_list(self, house_info):
        self.__house_list.append(house_info)

    def remove_house_list(self, house_info):
        if house_info in self.__house_list:
            self.__house_list.remove(house_info)

    # def get_name(self):
    #     return self.__name
    def search_house(self, house_info):
        pass

    def sign_contract(self, house_info, period):
        pass

    def sign_contracts(self, period):
        pass


class HouseOwner:
    def __init__(self, name):
        self.__name = name
        self.__house_info = None

    def get_name(self):
        return self.__name

    def set_house_info(self, area, price, address):
        self.__house_info = HouseInfo(area, price, address, self)

    def publish_house_info(self, agency):
        agency.add_house_list(self.__house_info)
        print("I'm {}. I'm selling my house.".format(self.__name))
        self.__house_info.show_info()


class Customer:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def find_house(self, house_info, agency):
        pass

    def see_house(self, house_info):
        pass

    def sign_contract(self):
        pass
