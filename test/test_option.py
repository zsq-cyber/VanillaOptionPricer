import unittest

from models.option import VanillaOption, OptionType


class OptionTestCase(unittest.TestCase):
    def setUp(self):
        desc = {
            "ProductName": "Put",
            "ProductParams":
                {
                    "Underlying": "UnderlyingB",
                    "Spot": 100,
                    "Strike": 100,
                    "Rate": 0,
                    "Vol": 0.25,
                    "StrikeDate": "23-Feb-18",
                    "MaturityDate": "23-Feb-19"
                }
        }
        self.option = VanillaOption(desc)

    def test_init(self):
        self.assertEqual(self.option.type, OptionType.PUT)
        self.assertEqual(self.option.underlying, "UnderlyingB")
        self.assertEqual(self.option.spot, 100)
        self.assertEqual(self.option.strike, 100)
        self.assertEqual(self.option.rate, 0)
        self.assertEqual(self.option.vol, 0.25)
        self.assertEqual(self.option.strike_date, "23-Feb-18")
        self.assertEqual(self.option.maturity_date, "23-Feb-19")

    def test_describe_option(self):
        self.assertEqual(self.option.describe_option(), '[OptionType.PUT] - [UnderlyingB] - [23-Feb-18, 23-Feb-19]')

    def test_get_time_to_exercise(self):
        self.assertEqual(self.option.get_time_to_exercise(), 365 / 365.0)


if __name__ == '__main__':
    unittest.main()
