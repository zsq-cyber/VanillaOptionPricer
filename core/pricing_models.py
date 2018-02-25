import abc
import numpy as np
import scipy.stats as ss

from core.constants import *


class PricingModel(object):
    """Abstract Base Class for option pricing model"""
    @abc.abstractmethod
    def doPricing(self, *args, **kwargs):
        raise NotImplementedError


def handle_zero_vol(func):
    """Decorator to handle zero volatility"""
    def zero_vol():
        return 0

    def handled(self, *args, **kwargs):
        # if volatility is zero, skip pricing and return 0
        if self.sigma != 0:
            return func(self, *args, **kwargs)
        else:
            return zero_vol()

    return handled


class BlackScholesModel(PricingModel):
    """Black-Scholes Pricing Model Implementation"""
    def __init__(self, option):
        # flags to allow single analytical equation for both calls and puts
        # Call: 1
        # Put: -1
        self.flag = int(option.type)
        self.S = option.spot  # Underlying asset price
        self.K = option.strike  # Option strike K
        self.r = option.rate  # Risk fee rate
        self.T = option.getTimeToExercise()  # Time to exercise
        self.sigma = option.vol  # Volatility
        if self.sigma == 0:
            self.d1 = 0
            self.d2 = 0
        else:
            self.d1 = (np.log(self.S / self.K) + (self.r + self.sigma ** 2 / 2) * self.T) / (self.sigma * np.sqrt(self.T))
            self.d2 = self.d1 - self.sigma * np.sqrt(self.T)

    @staticmethod
    def cdf(n):
        """Cumulative distribution function"""
        return ss.norm.cdf(n)

    @staticmethod
    def pdf(n):
        """probability distribution function"""
        return ss.norm.pdf(n)

    @handle_zero_vol
    def getDelta(self):
        return self.cdf(self.d1) + min(self.flag, 0)

    @handle_zero_vol
    def getGamma(self):
        return self.pdf(self.d1) / (self.S * self.sigma * np.sqrt(self.T))

    @handle_zero_vol
    def getVega(self):
        return self.S * self.pdf(self.d1) * np.sqrt(self.T) * PERCENTAGE_FACTOR

    @handle_zero_vol
    def getTheta(self):
        theta = -self.S * self.pdf(self.d1) * self.sigma / (2 * np.sqrt(self.T)) - \
                self.flag * self.r * self.K * np.exp(-self.r * self.T) * self.cdf(self.flag * self.d2)
        return theta / DAYS_OF_YEAR

    @handle_zero_vol
    def getRho(self):
        return self.flag * self.K * self.T * np.exp(-self.r * self.T) * self.cdf(self.flag * self.d2) * \
               PERCENTAGE_FACTOR

    @handle_zero_vol
    def getPrice(self):
        return self.flag * (
                self.cdf(self.flag * self.d1) * self.S -
                self.cdf(self.flag * self.d2) * self.K * np.exp(-self.r * self.T))

    def getPriceAndGreeks(self):
        """Rounding price and greeks, and format with a dictionary"""
        return {
            'price': round(self.getPrice(), ROUND_NUM),
            'greeks': {
                'delta': round(self.getDelta(), ROUND_NUM),
                'gamma': round(self.getGamma(), ROUND_NUM),
                'vega': round(self.getVega(), ROUND_NUM),
                'theta': round(self.getTheta(), ROUND_NUM),
                'rho': round(self.getRho(), ROUND_NUM)
            }
        }

    def doPricing(self):
        """The method to do the pricing"""
        return self.getPriceAndGreeks()
