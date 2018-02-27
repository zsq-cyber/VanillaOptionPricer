import unittest
import datetime as dt
from utils.datetime_utils import DateTimeUtils


class DateTimeUtilsTestCase(unittest.TestCase):
    def test_string_to_date(self):
        date_string = "01-Feb-18"
        self.assertEqual(DateTimeUtils.string_to_date(date_string), dt.date(2018, 2, 1))


if __name__ == '__main__':
    unittest.main()
