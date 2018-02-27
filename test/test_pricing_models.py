import unittest

from models.option import VanillaOption
from core.pricing_models import BlackScholesModel


class PricingModelTestCase(unittest.TestCase):
    def testBlackScholesModelCall(self):
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
        self.option = VanillaOption(desc)
        black_scholes_model = BlackScholesModel(self.option)
        self.assertEqual(black_scholes_model.get_price(), 0.09934079437910714)
        self.assertEqual(black_scholes_model.get_delta(), 0.5496703971895536)
        self.assertEqual(black_scholes_model.get_gamma(), 1.5855581254976814)
        self.assertEqual(black_scholes_model.get_vega(), 0.003953035326583261)
        self.assertEqual(black_scholes_model.get_theta(), -0.00013574983951178778)
        self.assertEqual(black_scholes_model.get_rho(), 0.0044909582307671924)

    def testBlackScholesModelPut(self):
        desc = {
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
        self.option = VanillaOption(desc)
        black_scholes_model = BlackScholesModel(self.option)
        self.assertEqual(black_scholes_model.get_price(), 0.014648530816228189)
        self.assertEqual(black_scholes_model.get_delta(), -0.0018802167965031868)
        self.assertEqual(black_scholes_model.get_gamma(), 0.0002397714069150577)
        self.assertEqual(black_scholes_model.get_vega(), 0.0059942851728764426)
        self.assertEqual(black_scholes_model.get_theta(), -0.00020528373879713844)
        self.assertEqual(black_scholes_model.get_rho(), -0.0020267021046654985)


if __name__ == '__main__':
    unittest.main()
