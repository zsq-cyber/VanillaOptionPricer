import datetime as dt
from core.constants import *


class DateTimeUtils:
    @staticmethod
    def string_to_date(date_string):
        """Convert date string with specific format (e.g. 01-Feb-18) to date object"""
        return dt.datetime.strptime(date_string, DT_FMT).date()
