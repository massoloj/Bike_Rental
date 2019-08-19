import datetime
from app.utils.enums import RentType
from app.models.customer import Customer
from app.models.bike import Bike


class Rent:
    """Rent class, stores the information of a Rent"""

    def __init__(self,
                 rentid: int,
                 startdate: str,
                 enddate: str,
                 renttype: RentType,
                 customer: Customer,
                 bike: Bike):

        self.__rentid = rentid
        self.__startdate = startdate
        self.__enddate = enddate
        self.__renttype = renttype
        self.__customer = customer
        self.__bike = bike

    @property
    def rentid(self):
        return self.__rentid

    @rentid.setter
    def rentid(self, rentid: int):
        self.__rentid = rentid
        
    @property
    def startdate(self):
        return self.__startdate

    @startdate.setter
    def startdate(self, startdate: str):
        self.__startdate = startdate

    @property
    def enddate(self):
        return self.__enddate

    @enddate.setter
    def enddate(self, enddate: str):
        self.__enddate = enddate

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer: Customer):
        self.__customer = customer

    @property
    def bike(self):
        return self.__bike

    @bike.setter
    def bike(self, bike: Bike):
        self.__bike = bike
