import datetime

from app.models.customer import Customer


class Bill:
    """Bill class, stores the information of a bill"""

    def __init__(self, billid: int, paydate: datetime, customer: Customer, rents: list, amount: float):
        self.__billid = billid
        self.__paydate = paydate
        self.__customer = customer
        self.__rents = rents
        self.__amount = amount

    @property
    def billid(self):
        return self.__billid

    @billid.setter
    def billid(self, billid: int):
        self.__billid = billid

    @property
    def paydate(self):
        return self.__paydate

    @paydate.setter
    def paydate(self, paydate: datetime):
        self.__paydate = paydate

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer: Customer):
        self.__customer = customer

    @property
    def rents(self):
        return self.__rents

    @rents.setter
    def rents(self, rents: list):
        self.__rents = rents
    
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    
        

    

    