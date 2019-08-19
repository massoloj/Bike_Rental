from app.utils.enums import BikeType
from app.models.bike import Bike
import logging

class BikeManager:
    """This class is used to interact and manipulate Bike objects"""

    logging.basicConfig(level=logging.INFO)

    def __init__(self):
        self.__bikes = []

    @property
    def bikes(self):
        return self.__bikes

    def add_bike(self, bike: Bike):
        self.bikes.append(bike)

    def available(self, bike: Bike):
        """Sets a bike's available property to True"""

        logging.info('Changing bike availability to true')
        bike.available = True

    def unavailable(self, bike: Bike):
        """Sets a bike's available property to False"""

        logging.info('Changing bike availability to false')
        bike.available = False

    def get_bike(self, biketype: BikeType):
        """Searchs a bike in a list of available bikes. Returns a Bike object if a bike is found, otherwise
        it returns None"""

        result = None
        logging.info('Searching for a bike')
        for bike in self.bikes:
            if bike.available and bike.biketype == biketype:
                logging.info('Bike found')
                self.available(bike)
                result = bike
                break

        logging.info('There are no available bikes for the desired type')
        return result
