import unittest

from services.client import OptionPricerClient


class OptionPricerClientTestCase(unittest.TestCase):
    def testSendRequest(self):
        url = 'http://localhost:8080/pricer'
        productSetFile = '../resources/ProductSetB.json'
        OptionPricerClient.sendOptionFileByPOST(url, productSetFile)


if __name__ == '__main__':
    unittest.main()
