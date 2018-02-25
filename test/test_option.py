import unittest

from models.option import VanillaOption, OptionType


class OptionTestCase(unittest.TestCase):
    def setUp(self):
        optionDesc = {
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
        self.option = VanillaOption()
        self.option.parseFromDesc(optionDesc)

    def testParseFromDesc(self):
        self.assertEqual(self.option.type, OptionType.PUT)
        self.assertEqual(self.option.underlying, "UnderlyingB")
        self.assertEqual(self.option.spot, 100)
        self.assertEqual(self.option.strike, 100)
        self.assertEqual(self.option.rate, 0)
        self.assertEqual(self.option.vol, 0.25)
        self.assertEqual(self.option.strikeDate, "23-Feb-18")
        self.assertEqual(self.option.maturityDate, "23-Feb-19")

    def testDescribeOption(self):
        self.assertEqual(self.option.describeOption(), '[OptionType.PUT] - [UnderlyingB] - [23-Feb-18, 23-Feb-19]')

    def testGetTimeToExercise(self):
        self.assertEqual(self.option.getTimeToExercise(), 365/365.0)


if __name__ == '__main__':
    unittest.main()
