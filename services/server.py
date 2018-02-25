#!/usr/bin/env python

"""
Option Pricer Rest API Server
"""
import json

from core.pricer import OptionPricer
from models.option import VanillaOption
from core.pricing_models import BlackScholesModel
from core.constants import *

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/pricer', methods=['POST'])
def pricingWithFile():
    productSet = getPayload(request)
    if productSet is None:
        # if product set file cannot be parsed to json, send error 591
        return "Invalid product set description file", CODE_INVALID_FILE
    else:
        # Do pricing
        # if exception happened, send error 592
        # else send pricing result with response 200
        try:
            result = getPrice(productSet)
            return jsonify(result), CODE_PRICING_SUCCESSFUL
        except Exception, e:
            print e
            return "Pricing encountered some exception", CODE_PRICING_EXCEPTION


def getPayload(request):
    """Read and load option info from a product set description file in the POST"""
    try:
        return json.loads(request.files['option_desc_file'].read())
    except Exception, e:
        print e
        return None


def getPrice(productSet):
    """Do pricing for each option in the product set, and return pricing result as a list"""
    result = []
    for desc in productSet['Products']:
        # create option DTO
        option = VanillaOption()
        option.parseFromDesc(desc)

        # create option pricer with Black-Scholes Model
        optionPricer = OptionPricer(BlackScholesModel(option))

        # calculate price and greeks
        ret = optionPricer.doPricing()

        # append pricing result to the final result set
        ret['description'] = option.describeOption()
        result.append(ret)
    return {'result': result}


def createServer():
    return app
