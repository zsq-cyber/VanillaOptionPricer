import datetime as dt
from core.constants import *


class DateTimeUtils:
    @staticmethod
    def string2date(dtStr):
        """Convert date string with specific format (e.g. 01-Feb-18) to date object"""
        return dt.datetime.strptime(dtStr, DT_FMT).date()
