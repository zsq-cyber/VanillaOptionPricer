import abc
import numpy as np
import scipy.stats as ss

from core.constants import *


class PricingModel(object):
    """Abstract Base Class for option pricing model"""

    @abc.abstractmethod
    def get_price(self, *args, **kwargs):
        """calculate theoretical price"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_delta(self, *args, **kwargs):
        """calculate delta"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_gamma(self, *args, **kwargs):
        """calculate gamma"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_vega(self, *args, **kwargs):
        """calculate vega"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_theta(self, *args, **kwargs):
        """calculate theta"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_rho(self, *args, **kwargs):
        """calculate rho"""
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
        self.t = option.get_time_to_exercise()  # Time to exercise
        self.sigma = option.vol  # Volatility
        if self.sigma == 0:
            self.d1 = 0
            self.d2 = 0
        else:
            self.d1 = (np.log(self.S / self.K) + (self.r + self.sigma ** 2 / 2) * self.t) / (
                        self.sigma * np.sqrt(self.t))
            self.d2 = self.d1 - self.sigma * np.sqrt(self.t)

    @staticmethod
    def cdf(n):
        """Cumulative distribution function"""
        return ss.norm.cdf(n)

    @staticmethod
    def pdf(n):
        """probability distribution function"""
        return ss.norm.pdf(n)

    @handle_zero_vol
    def get_delta(self):
        return self.cdf(self.d1) + min(self.flag, 0)

    @handle_zero_vol
    def get_gamma(self):
        return self.pdf(self.d1) / (self.S * self.sigma * np.sqrt(self.t))

    @handle_zero_vol
    def get_vega(self):
        return self.S * self.pdf(self.d1) * np.sqrt(self.t) * PERCENTAGE_FACTOR

    @handle_zero_vol
    def get_theta(self):
        theta = -self.S * self.pdf(self.d1) * self.sigma / (2 * np.sqrt(self.t)) - \
                self.flag * self.r * self.K * np.exp(-self.r * self.t) * self.cdf(self.flag * self.d2)
        return theta / DAYS_OF_YEAR

    @handle_zero_vol
    def get_rho(self):
        return self.flag * self.K * self.t * np.exp(-self.r * self.t) * self.cdf(self.flag * self.d2) * \
               PERCENTAGE_FACTOR

    @handle_zero_vol
    def get_price(self):
        return self.flag * (
                self.cdf(self.flag * self.d1) * self.S -
                self.cdf(self.flag * self.d2) * self.K * np.exp(-self.r * self.t))
