from enum import IntEnum
from utils.datetime_utils import DateTimeUtils
from core.constants import *


class OptionType(IntEnum):
    """Option Type Enum"""
    CALL = 1
    PUT = -1


class VanillaOption(object):
    """Serve as a Data Transfer Object to carry all information of an option"""
    def __init__(self):
        self.__type = None
        self.__underlying = ''
        self.__spot = 0
        self.__strike = 0
        self.__rate = 0
        self.__vol = 0
        self.__strikeDate = ''
        self.__maturityDate = ''

    def parseFromDesc(self, desc):
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
        self.__strikeDate = desc['ProductParams']['StrikeDate']
        self.__maturityDate = desc['ProductParams']['MaturityDate']

    def describeOption(self):
        """Return a string that uniquely represent an option"""
        return '[{}] - [{}] - [{}, {}]'.format(
            str(self.__type), self.__underlying, self.__strikeDate, self.__maturityDate)

    def getTimeToExercise(self):
        """Calculate time to exercise"""
        return (DateTimeUtils.string2date(self.maturityDate) - DateTimeUtils.string2date(self.strikeDate)).days / \
               DAYS_OF_YEAR

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
    def strikeDate(self):
        return self.__strikeDate

    @property
    def maturityDate(self):
        return self.__maturityDate
