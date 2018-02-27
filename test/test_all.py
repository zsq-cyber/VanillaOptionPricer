import unittest

from test.test_datetime_utils import DateTimeUtilsTestCase
from test.test_option import OptionTestCase
from test.test_pricer import OptionPricerTestCase
from test.test_pricing_models import PricingModelTestCase


def create_suite():
    test_classes_to_run = [OptionTestCase,
                           PricingModelTestCase,
                           OptionPricerTestCase,
                           DateTimeUtilsTestCase]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    return unittest.TestSuite(suites_list)


if __name__ == '__main__':
    test_suite = create_suite()
    runner = unittest.TextTestRunner()
    results = runner.run(test_suite)
