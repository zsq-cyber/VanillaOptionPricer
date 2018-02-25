from services.client import OptionPricerClient


if __name__ == '__main__':
    url = 'http://localhost:8080/pricer'
    productSetFile = 'resources/ProductSetA.json'
    OptionPricerClient.sendOptionFileByPOST(url, productSetFile)
