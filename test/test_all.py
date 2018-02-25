import unittest

from test_datetime_utils import DateTimeUtilsTestCase
from test_option import OptionTestCase
from test_pricing_models import PricingModelTestCase


def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(OptionTestCase)
    test_suite.addTest(PricingModelTestCase)
    test_suite.addTest(DateTimeUtilsTestCase)
    return test_suite


if __name__ == '__main__':
    suite = create_suite()

    runner = unittest.TextTestRunner()
    runner.run(suite)
