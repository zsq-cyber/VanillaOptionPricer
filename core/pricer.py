from core.constants import ROUND_NUM


class OptionPricer(object):
    """Option pricer implementation that invokes pricing models' methods to get price and greeks
    with customized format and structure"""

    def __init__(self, pricing_model):
        self.__pricing_model = pricing_model

    def get_price(self):
        """return rounded price"""
        return {'price': round(self.__pricing_model.get_price(), ROUND_NUM)}

    def get_delta(self):
        """return rounded delta"""
        return {'delta': round(self.__pricing_model.get_delta(), ROUND_NUM)}

    def get_gamma(self):
        """return rounded gamma"""
        return {'gamma': round(self.__pricing_model.get_gamma(), ROUND_NUM)}

    def get_vega(self):
        """return rounded vega"""
        return {'vega': round(self.__pricing_model.get_vega(), ROUND_NUM)}

    def get_theta(self):
        """return rounded theta"""
        return {'theta': round(self.__pricing_model.get_theta(), ROUND_NUM)}

    def get_rho(self):
        """return rounded rho"""
        return {'rho': round(self.__pricing_model.get_rho(), ROUND_NUM)}

    def get_greeks(self):
        """return greeks in a dictionary"""
        ret = {}
        ret.update(self.get_delta())
        ret.update(self.get_gamma())
        ret.update(self.get_vega())
        ret.update(self.get_theta())
        ret.update(self.get_rho())
        return {'greeks': ret}

    def get_price_and_greeks(self):
        """return price and greeks in nested dictionary"""
        ret = {}
        ret.update(self.get_price())
        ret.update(self.get_greeks())
        return ret
