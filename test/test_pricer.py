import unittest

from core.pricer import OptionPricer
from models.option import VanillaOption
from core.pricing_models import BlackScholesModel


class OptionPricerTestCase(unittest.TestCase):
    def setUp(self):
        desc = {
            "ProductName": "Call",
            "ProductParams":
                {
                    "Underlying": "UnderlyingA",
                    "Spot": 1,
                    "Strike": 1,
                    "Rate": 0,
                    "Vol": 0.25,
                    "StrikeDate": "23-Feb-18",
                    "MaturityDate": "22-Feb-19"
                }
        }
        self.pricer = OptionPricer(BlackScholesModel(VanillaOption(desc)))

    def testGetPrice(self):
        expected = {'price': 0.09934}
        self.assertDictEqual(self.pricer.get_price(), expected)

    def testGetDelta(self):
        expected = {'delta': 0.54967}
        self.assertDictEqual(self.pricer.get_delta(), expected)

    def testGetGamma(self):
        expected = {'gamma': 1.58556}
        self.assertDictEqual(self.pricer.get_gamma(), expected)

    def testGetVega(self):
        expected = {'vega': 0.00395}
        self.assertDictEqual(self.pricer.get_vega(), expected)

    def testGetTheta(self):
        expected = {'theta': -0.00014}
        self.assertDictEqual(self.pricer.get_theta(), expected)

    def testGetRho(self):
        expected = {'rho': 0.00449}
        self.assertDictEqual(self.pricer.get_rho(), expected)

    def testGetGreeks(self):
        expected = {
            'greeks': {'delta': 0.54967,
                       'gamma': 1.58556,
                       'rho': 0.00449,
                       'theta': -0.00014,
                       'vega': 0.00395}
        }
        self.assertDictEqual(self.pricer.get_greeks(), expected)

    def testGetPriceAndGreeks(self):
        expected = {
            'greeks': {'delta': 0.54967,
                       'gamma': 1.58556,
                       'rho': 0.00449,
                       'theta': -0.00014,
                       'vega': 0.00395},
            'price': 0.09934
        }
        self.assertDictEqual(self.pricer.get_price_and_greeks(), expected)


if __name__ == '__main__':
    unittest.main()
