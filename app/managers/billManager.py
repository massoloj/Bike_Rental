import datetime
import logging
from app.utils.constants import FAMILY_DISCOUNT
from app.models.bill import Bill
from app.models.customer import Customer
from app.managers.rentManager import RentManager


class BillManager:
    """This class is used to interact and manipulate Bill objects"""

    logging.basicConfig(level=logging.INFO)

    def __init__(self):
        self.__idcounter = 0
        self.__bills = []
        self.__rentManager = RentManager()

    @property
    def idcounter(self):
        return self.__idcounter

    @property
    def bills(self):
        return self.__bills

    def increase_idcounter(self):
        """Increases the id counter by 1"""

        self.idcounter += 1

    def apply_discount(self, amount: float):
        """Applies a discount of 30% to an amount"""

        logging.info('Applying discount')
        amount = format((amount * FAMILY_DISCOUNT) / 100, '.2f')
        return amount

    def calculate_amount(self, rents: list):
        """Calculates the total amount of a bill"""

        logging.info('Calculating amount of the bill')
        amount = 0
        for rent in rents:
            amount += rent.rentType

        logging.info('Checking if a discount must be applied')
        if len(rents) >= 3:
            amount = self.apply_discount(amount)

        return amount

    def create_bill(self, paydate: datetime, customer: Customer, rents: list):
        """Creates a bill object"""

        amount = self.calculate_amount(rents)
        bill = Bill(self.idcounter, paydate, customer, rents, amount)
        logging.info('Bill object created')
        return bill
