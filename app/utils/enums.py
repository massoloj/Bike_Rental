from enum import IntEnum

class RentType(IntEnum):
    """Enumerate that represents the types of rents"""
    HOUR = 5
    DAY = 20
    WEEK = 60

class BikeType(IntEnum):
    """Enumerate that represents the types of bikes"""
    HYBRID = 1
    ROAD = 2
    TRIATHLON = 3
    BMX = 4
    COMMUTING = 5
    CYCLOCROSS = 6

class BikeBrand(IntEnum):
    """Enumerate that represents different bike brands"""
    PINARELLO = 1
    EDDY_MERCK = 2
    BMC = 3
    TREK = 4
    SPECIALIZED = 5
    GIANT = 6
    RALEIGH = 7
