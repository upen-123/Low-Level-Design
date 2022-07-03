class ProductCategory:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class ProductReview:
    def __init__(self, rating, review, reviewer):
        self.rating = rating
        self.review = review
        self.reviewer = reviewer


class Product:
    def __init__(self, id, name, description, price, category,seller_account):
        self.__product_id = id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__category = category
        self.__available_item_count = 0
        self.__seller = seller_account

    def get_available_count(self):
        return self.__available_item_count

    def update_price(self, new_price):
        pass
