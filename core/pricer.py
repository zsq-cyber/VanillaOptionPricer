class OptionPricer(object):
    def __init__(self, pricingModel):
        self.__pricingModel = pricingModel

    def doPricing(self):
        return self.__pricingModel.doPricing()
