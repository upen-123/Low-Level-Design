class Item:
    def __init__(self, id, quantity, price):
        self.__product_id = 1
        self.__quantity = quantity
        self.__price = price

    def update_quantitiy(self, quantity):
        pass


class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        pass

    def remove_item(self, item):
        pass

    def update_item_quantity(self, item, quantity):
        pass

    def get_items(self):
        return self.__items

    def checkout(self):
        pass

from utils import OrderStatus
import datetime


class OrderLog:
    def __init__(self, order_number, status=OrderStatus.PENDING):
        self.__order_number = 0
        self.__status = status
        self.__order_date = datetime.date.today()
        self.__order_log = []

    def send_shipment(self):
        pass

    def make_payment(self, payment):
        pass

    def add_order_log(self, order_log):
        pass







