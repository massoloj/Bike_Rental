from app.utils.enums import BikeType
from app.utils.enums import BikeBrand


class Bike:
    """Bike class, stores the information of a Bike"""

    def __init__(self, bikeid: str, biketype: BikeType, brand: BikeBrand, available: bool):
        self.__bikeid = bikeid
        self.__biketype = biketype
        self.__brand = brand
        self.__available = available

    @property
    def bikeid(self):
        return self.__bikeid

    @bikeid.setter
    def bikeid(self, bikeid: str):
        self.__bikeid = bikeid

    @property
    def biketype(self):
        return self.__biketype

    @biketype.setter
    def biketype(self, biketype: BikeType):
        self.__biketype = biketype

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand: BikeBrand):
        self.__brand = brand

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, available: bool):
        self.__available = available

    def __str__(self):
        return str(self.bikeid) + " " + str(self.biketype) + " " + str(self.brand) + " " + str(self.available)
