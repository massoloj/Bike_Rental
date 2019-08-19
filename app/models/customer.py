import datetime

class Customer():
    """Customer class, stores the information of a customer"""
    def __init__(self, customerid: str, name: str, lastname: str, address: str, email: str, phone: str, rents: list):
        self.__customerid = customerid
        self.__name = name
        self.__lastname = lastname
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__rents = rents

    @property
    def customerid(self):
        return self.__customerid

    @customerid.setter
    def customerid(self, customerid: str):
        self.__customerid = customerid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def rents(self):
        return self.__rents

    @rents.setter
    def rents(self, rents: list):
        self.__rents = rents



    
