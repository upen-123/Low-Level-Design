from abc import abstractmethod, ABC


class Search(ABC):
    def search_products_by_name(self, name):
        pass

    def search_product_by_category(self, category):
        pass


class Catalog(Search):
    def __init__(self):
        self.__product_names = {}
        self.__product_categories = {}

    def search_products_by_name(self, name):
        return self.__product_names.get(name)

    def search_product_by_category(self, category):
        return self.__product_categories.get(category)
