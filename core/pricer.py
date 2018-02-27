class OptionPricer(object):
    def __init__(self, pricing_model):
        self.__pricing_model = pricing_model

    def do_pricing(self):
        return self.__pricing_model.do_pricing()
