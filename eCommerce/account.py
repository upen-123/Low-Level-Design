from utils import AccountStatus


class Account:
    def __init__(self, username, name, email, phone_number, password, shipping_address, status=AccountStatus):
        self.username = username
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.status = status.ACTIVE
        self.password = password
        self.shipping_address = shipping_address

    def add_product(self, product):
        pass

    def add_product_review(self, review):
        pass

    def reset_password(self, password):
        pass


from abc import ABC, abstractmethod


class Customer(ABC):
    def __init__(self, cart, order):
        self.__cart = cart
        self.__order = order

    def get_shopping_cart(self):
        return self.__cart

    def add_item_to_cart(self, item):
        pass

    def remove_item_from_cart(self, item):
        pass


class Guest(Customer):
    def register_account(self):
        pass


class Member(Customer):
    def __init__(self, account):
        self.__account = account

    def place_order(self, order):
        pass


    