import datetime
import logging
from app.utils.enums import BikeType
from app.utils.enums import RentType
from app.utils.validators import Validators
from app.models.customer import Customer
from app.models.rent import Rent
from app.managers.rentManager import RentManager


class CustomerManager:
    """This class is used to interact and manipulate Customer objects"""

    logging.basicConfig(level=logging.INFO)

    def __init__(self):
        self.__customers = []
        self.__rentmanager = RentManager()

    @property
    def rentmanager(self):
        return self.__rentmanager

    @property
    def customers(self):
        return self.__customers

    def add_customer(self, customer: Customer):
        """Adds a customer to the customer list"""

        self.customers.append(customer)

    def create_customer(self, customerid: str, name: str, lastname: str, address: str, phone: str, email: str, rents: list):
        """Creates a customer object. If the parameters fail in the validation, it returns False"""

        logging.info('Validating parameters')
        is_valid = Validators.valid_customer(customerid, name, lastname, address, phone, email, rents)
        if is_valid:
            logging.info('Parameters are ok, creating customer')
            customer = Customer(customerid, name, lastname, address, phone, email, rents)
            return customer
        else:
            logging.info('There has been an error in parameters validation, returning False')
            return False

    def add_rent(self, customer: Customer, rent: Rent):
        """Adds a rent object to the customer list of rents"""

        logging.info('Adding rent')
        customer.rents.append(rent)

    def rent_bike(self, startdate: datetime,
                        enddate: datetime,
                        renttype: RentType,
                        customer: Customer, 
                        biketype: BikeType):
        """Creates a rent object for the desired biketype. Returns True if the rent is created, otherwise it returns
        false"""

        logging.info('Creating rent object')
        rent = self.rentManager.create_rent(startdate, enddate, renttype, customer, biketype)
        return True if rent else False

