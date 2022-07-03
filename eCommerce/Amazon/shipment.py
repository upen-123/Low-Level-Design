from utils import ShipmentStatus
import datetime


class ShipmentLog:
    def __init__(self, shipment_number, status=ShipmentStatus.PENDING):
        self.__shipment_number = shipment_number
        self.__status = status
        self.creation_date = datetime.date.today()


class Shipment:
    def __init__(self, shipment_number, shipment_method):
        self.__shipment_number = shipment_number
        self.__shipment_date = datetime.date.today()
        self.__estimated_arrival = datetime.date.today()
        self.__shipment_method = shipment_method
        self.__shipmentLogs = []

    def add_shipment_log(self, shipment_log):
        pass


from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, id, content):
        self.__notification_id = id
        self.__created_on = datetime.date.today()
        self.__content = content

    def send_notification(self, account):
        pass
