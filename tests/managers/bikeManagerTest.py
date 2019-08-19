import pytest
import logging
from app.utils.enums import BikeType
from app.utils.enums import BikeBrand
from app.models.bike import Bike
from app.managers.bikeManager import BikeManager


def test_available():
    """Tests if bike available status is correctly changed to true"""

    bikemanager = BikeManager()
    bike = Bike('AAA', BikeType.BMX, BikeBrand.GIANT, False)
    logging.warning('Created bike: ' + str(bike))
    bikemanager.available(bike)
    logging.warning('Bike available property changed to True')
    assert bike.available == True

def test_unavailable():
    """Tests if bike available status is correctly changed to False"""

    bikemanager = BikeManager()
    bike = Bike('AAA', BikeType.BMX, BikeBrand.GIANT, True)
    bikemanager.unavailable(bike)
    assert bike.available == False

def test_get_bike_ok():
    """Tests if a bike available can be rented"""

    bikemanager = BikeManager()
    bike = Bike('AAA', BikeType.BMX, BikeBrand.GIANT, True)
    bikemanager.add_bike(bike)
    rentedbike = bikemanager.get_bike(BikeType.BMX)
    assert isinstance(rentedbike, Bike) == True

def test_get_bike_notok1():
    """Tests if a bike not available can be rented"""

    bikemanager = BikeManager()
    bike = Bike('AAA', BikeType.BMX, BikeBrand.GIANT, False)
    bikemanager.add_bike(bike)
    rentedbike = bikemanager.get_bike(BikeType.BMX)
    assert isinstance(rentedbike, Bike) == False

def test_get_bike_notok2():
    """Tests if a bike that does not exist can be rented"""

    bikemanager = BikeManager()
    bike = Bike('AAA', BikeType.BMX, BikeBrand.GIANT, True)
    bikemanager.add_bike(bike)
    rentedbike = bikemanager.get_bike(BikeType.COMMUTING)
    assert isinstance(rentedbike, Bike) == False

def test_get_bike_notok3():
    """Tests if a bike can be rented when there are no bikes"""

    bikemanager = BikeManager()
    rentedbike = bikemanager.get_bike(BikeType.COMMUTING)
    assert isinstance(rentedbike, Bike) == False

def test_add_bike_ok():
    """Tests if a bike is added correctly to the manager"""

    bikemanager = BikeManager()
    bike = Bike('AAA', BikeType.BMX, BikeBrand.GIANT, True)

    size = len(bikemanager.bikes)
    bikemanager.add_bike(bike)
    newsize = len(bikemanager.bikes)

    assert (newsize < size) == False
