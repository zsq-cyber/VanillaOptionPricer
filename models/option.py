from enum import IntEnum
from utils.datetime_utils import DateTimeUtils
from core.constants import *


class OptionType(IntEnum):
    """Option Type Enum"""
    CALL = 1
    PUT = -1


class VanillaOption(object):
    """Serve as a Data Transfer Object to carry all information of an option"""

    def __init__(self, desc):
        """Parse option info from a product description"""
        if desc['ProductName'] == 'Call':
            self.__type = OptionType.CALL
        else:
            self.__type = OptionType.PUT
        self.__underlying = desc['ProductParams']['Underlying']
        self.__spot = desc['ProductParams']['Spot']
        self.__strike = desc['ProductParams']['Strike']
        self.__rate = desc['ProductParams']['Rate']
        self.__vol = desc['ProductParams']['Vol']
        self.__strike_date = desc['ProductParams']['StrikeDate']
        self.__maturity_date = desc['ProductParams']['MaturityDate']

    def describe_option(self):
        """Return a string that uniquely represent an option"""
        return '[{}] - [{}] - [{}, {}]'.format(
            str(self.__type), self.__underlying, self.__strike_date, self.__maturity_date)

    def get_time_to_exercise(self):
        """Calculate time to exercise"""
        return (DateTimeUtils.string_to_date(self.maturity_date) - DateTimeUtils.string_to_date(
            self.strike_date)).days / DAYS_OF_YEAR

    @property
    def type(self):
        return self.__type

    @property
    def underlying(self):
        return self.__underlying

    @property
    def spot(self):
        return self.__spot

    @property
    def strike(self):
        return self.__strike

    @property
    def rate(self):
        return self.__rate

    @property
    def vol(self):
        return self.__vol

    @property
    def strike_date(self):
        return self.__strike_date

    @property
    def maturity_date(self):
        return self.__maturity_date
