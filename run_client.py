from services.client import OptionPricerClient


if __name__ == '__main__':
    url = 'http://localhost:8080/pricer'
    product_set_file = 'resources/ProductSetA.json'
    OptionPricerClient.send_option_file(url, product_set_file)
