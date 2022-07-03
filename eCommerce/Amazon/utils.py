import Enum


class Address:
    def __init__(self, street, city, zip_code, country):
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.country = country


class OrderStatus(Enum):
    unshipped = 0
    pending = 1
    shipped = 2
    completed = 3
    canceled = 4
    refund_applied = 5


class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class ShipmentStatus(Enum):
    PENDING, SHIPPED, DELIVERED, ON_HOLD = 1, 2, 3, 4


class PaymentStatus(Enum):
  UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


