import unittest

from models.option import VanillaOption
from core.pricing_models import BlackScholesModel


class PricingModelTestCase(unittest.TestCase):
    def testBlackScholesModelCall(self):
        optionDesc = {
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
        self.option = VanillaOption()
        self.option.parseFromDesc(optionDesc)
        blackScholesModel = BlackScholesModel(self.option)
        result = blackScholesModel.getPriceAndGreeks()
        self.assertEqual(result['price'], 0.09934)
        self.assertEqual(result['greeks']['delta'], 0.54967)
        self.assertEqual(result['greeks']['gamma'], 1.58556)
        self.assertEqual(result['greeks']['vega'], 0.00395)
        self.assertEqual(result['greeks']['theta'], -0.00014)
        self.assertEqual(result['greeks']['rho'], 0.00449)

    def testBlackScholesModelPut(self):
        optionDesc = {
            "ProductName": "Put",
            "ProductParams":
                {
                    "Underlying": "UnderlyingB",
                    "Spot": 100,
                    "Strike": 50,
                    "Rate": 0,
                    "Vol": 0.25,
                    "StrikeDate": "23-Feb-18",
                    "MaturityDate": "23-Feb-19"
                }
        }
        self.option = VanillaOption()
        self.option.parseFromDesc(optionDesc)
        blackScholesModel = BlackScholesModel(self.option)
        result = blackScholesModel.getPriceAndGreeks()
        self.assertEqual(result['price'], 0.01465)
        self.assertEqual(result['greeks']['delta'], -0.00188)
        self.assertEqual(result['greeks']['gamma'], 0.00024)
        self.assertEqual(result['greeks']['vega'], 0.00599)
        self.assertEqual(result['greeks']['theta'], -0.00021)
        self.assertEqual(result['greeks']['rho'], -0.00203)


if __name__ == '__main__':
    unittest.main()
