from app.utils.enums import RentType
from app.utils.enums import BikeType
from app.models.customer import Customer


class Validators:
    """Class to validate parameters before object creation"""

    @classmethod
    def valid_customer(cls, customerid: str, name: str, lastname: str, address: str, phone: str, email: str, rents: list):
        """Validator for customer class, returns true if the parameters are correct. Otherwise it returns false"""

        if not isinstance(customerid, str):
            return False

        if not isinstance(name, str):
            return False

        if not isinstance(lastname, str):
            return False

        if not isinstance(address, str):
            return False

        if not isinstance(phone, str):
            return False

        if not isinstance(email, str):
            return False

        if not isinstance(rents, list):
            return False

        return True

    @classmethod
    def valid_rent(cls, startdate: str, enddate: str, renttype: RentType, customer: Customer, biketype: BikeType):
        """Validator for rent class, returns true if the parameters are correct. Otherwise it returns false"""

        if not isinstance(startdate, str):
            return False

        if not isinstance(enddate, str):
            return False

        if not isinstance(renttype, RentType):
            return False

        if not isinstance(customer, Customer):
            return False

        if not isinstance(biketype, BikeType):
            return False

        return True

