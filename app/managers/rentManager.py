import logging
from app.utils.enums import BikeType
from app.utils.enums import RentType
from app.utils.validators import Validators
from app.models.rent import Rent
from app.models.customer import Customer
from app.managers.bikeManager import BikeManager


class RentManager:
    """This class is used to interact and manipulate Rent objects"""

    logging.basicConfig(level=logging.INFO)

    def __init__(self):
        self.__idcounter = 0
        self.__rents = []
        self.__bikemanager = BikeManager()

    @property
    def idcounter(self):
        return self.__idcounter

    @idcounter.setter
    def idcounter(self, idcounter: int):
        self.__idcounter = idcounter

    @property
    def rents(self):
        return self.__rents

    @property
    def bikemanager(self):
        return self.__bikemanager

    def increase_idcounter(self):
        self.idcounter += 1

    def add_rent(self, rent: Rent):
        """Adds a rent object to the list of rents"""

        logging.info('Adding rent object to list')
        self.rents.append(rent)

    def create_rent(self, startdate: str, enddate: str, renttype: RentType, customer: Customer, biketype: BikeType):
        """Method to create an instance of a rental. If there is an available bike of the desired bikeType, then
        it creates the rent object"""

        logging.info('Searching for an available bike')
        bike = self.bikemanager.get_bike(biketype)
        if bike is not None:
            logging.info('A bike was found, checking new rent object parameters')
            is_valid = Validators.valid_rent(startdate, enddate, renttype, customer, biketype)
            if is_valid:
                logging.info('Data is correct, creating rent object')
                self.increase_idcounter()
                rent = Rent(self.idcounter, startdate, enddate, renttype, customer, bike)
                self.add_rent(rent)
                return rent

        logging.info('A problem occurred when creating the rent object, returning None')
        return None
    

