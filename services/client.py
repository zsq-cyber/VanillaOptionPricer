import pprint

import requests
from core.constants import *


class OptionPricerClient(object):
    """client to test option pricer service"""

    # send product set json file to server by post
    @staticmethod
    def send_option_file(url, product_set_file):
        files = {'option_desc_file': open(product_set_file, 'rb')}

        # Send POST request with product set description file uploaded
        print("Request: {}".format(product_set_file))
        r = requests.post(
            url=url,
            files=files
        )

        # Handle response
        if r.status_code in [CODE_INVALID_FILE, CODE_PRICING_EXCEPTION]:
            print("Response: {} - {}".format(r.status_code, r.content))
        elif r.status_code == CODE_PRICING_SUCCESSFUL:
            print("Response: {} - Pricing result received".format(r.status_code))
            result = r.json()
            for r in result['result']:
                print("\n--------------------------------------")
                pprint.pprint(r)
        else:
            print("Unknown response - {}".format(r.status_code))
