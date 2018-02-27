import unittest

from services.server import create_server


class OptionPricerServerTestCase(unittest.TestCase):
    def test_start_server(self):
        app = create_server()
        app.run(port=8080)


if __name__ == '__main__':
    unittest.main()
