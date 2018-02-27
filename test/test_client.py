import unittest

from services.client import OptionPricerClient


class OptionPricerClientTestCase(unittest.TestCase):
    def test_send_request(self):
        url = 'http://localhost:8080/pricer'
        product_set_file = '../resources/ProductSetB.json'
        OptionPricerClient.send_option_file(url, product_set_file)


if __name__ == '__main__':
    unittest.main()
