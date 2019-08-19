import pytest
import logging
from app.utils.enums import BikeType
from app.utils.enums import RentType
from app.utils.enums import BikeBrand
from app.models.rent import Rent
from app.models.bike import Bike
from app.managers.rentManager import RentManager
from app.managers.customerManager import CustomerManager


def test_create_rent_ok():
    rent_manager = RentManager()
    customer_manager = CustomerManager()
    customer = customer_manager.create_customer('35025191', 'Julian', 'Massolo', 'Mitre 182', 'massolo.j@gmail.com',
                                                '222225', [])

    bike = Bike('AAA', BikeType.BMX, BikeBrand.GIANT, True)
    rent_manager.bikemanager.add_bike(bike)
    rent = rent_manager.create_rent('01/01/2019', '05/01/2019', RentType.DAY, customer, BikeType.BMX)
    assert isinstance(rent, Rent) == True

