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
def pricing_with_file():
    product_set = get_payload(request)
    if product_set is None:
        # if product set file cannot be parsed to json, send error 591
        return "Invalid product set description file", CODE_INVALID_FILE
    else:
        # Do pricing
        # if exception happened, send error 592
        # else send pricing result with response 200
        try:
            result = get_price(product_set)
            return jsonify(result), CODE_PRICING_SUCCESSFUL
        except Exception as e:
            print(e)
            return "Pricing encountered some exception", CODE_PRICING_EXCEPTION


def get_payload(request_):
    """Read and load option info from a product set description file in the POST"""
    try:
        return json.loads(request_.files['option_desc_file'].read())
    except Exception as e:
        print(e)
        return None


def get_price(product_set):
    """Do pricing for each option in the product set, and return pricing result as a list"""
    result = []
    for desc in product_set['Products']:
        # create option DTO
        option = VanillaOption(desc)

        # create option pricer with Black-Scholes Model
        option_pricer = OptionPricer(BlackScholesModel(option))

        # calculate price and greeks
        ret = option_pricer.do_pricing()

        # append pricing result to the final result set
        ret['description'] = option.describe_option()
        result.append(ret)
    return {'result': result}


def create_server():
    return app
