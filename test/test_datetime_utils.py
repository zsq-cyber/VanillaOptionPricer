import unittest
import datetime as dt
from utils.datetime_utils import DateTimeUtils


class DateTimeUtilsTestCase(unittest.TestCase):
    def testString2Date(self):
        dateString = "01-Feb-18"
        self.assertEqual(DateTimeUtils.string2date(dateString), dt.date(2018, 2, 1))


if __name__ == '__main__':
    unittest.main()
