import argparse

import sys

from services.client import OptionPricerClient


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('request')
    args = parser.parse_args()
    if not args.request:
        print("Pricer request is not specified")
        sys.exit(2)

    url = 'http://localhost:8080/' + args.request
    product_set_file = 'resources/ProductSetA.json'
    OptionPricerClient.send_option_file(url, product_set_file)
