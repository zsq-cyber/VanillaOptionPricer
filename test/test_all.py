import unittest

from test.test_datetime_utils import DateTimeUtilsTestCase
from test.test_option import OptionTestCase
from test.test_pricer import OptionPricerTestCase
from test.test_pricing_models import PricingModelTestCase


def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(OptionTestCase())
    test_suite.addTest(PricingModelTestCase())
    test_suite.addTest(DateTimeUtilsTestCase())
    test_suite.addTest(OptionPricerTestCase())
    return test_suite


if __name__ == '__main__':
    suite = create_suite()

    runner = unittest.TextTestRunner()
    runner.run(suite)
