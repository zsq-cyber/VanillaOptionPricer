import unittest

from services.server import createServer


class OptionPricerServerTestCase(unittest.TestCase):
    def testStartServer(self):
        app = createServer()
        app.run(port=8080)


if __name__ == '__main__':
    unittest.main()
