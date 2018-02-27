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


@app.route('/pricer/price', methods=['POST'])
def get_price():
    """return price"""
    return handle_pricer_request("get_price")


@app.route('/pricer/delta', methods=['POST'])
def get_delta():
    """return delta"""
    return handle_pricer_request("get_delta")


@app.route('/pricer/gamma', methods=['POST'])
def get_gamma():
    """return gamma"""
    return handle_pricer_request("get_gamma")


@app.route('/pricer/vega', methods=['POST'])
def get_vega():
    """return vega"""
    return handle_pricer_request("get_vega")


@app.route('/pricer/theta', methods=['POST'])
def get_theta():
    """return theta"""
    return handle_pricer_request("get_theta")


@app.route('/pricer/rho', methods=['POST'])
def get_rho():
    """return rho"""
    return handle_pricer_request("get_rho")


@app.route('/pricer/greeks', methods=['POST'])
def get_greeks():
    """return all greeks"""
    return handle_pricer_request("get_greeks")


@app.route('/pricer/all', methods=['POST'])
def get_all():
    """return price and all greeks"""
    return handle_pricer_request("get_price_and_greeks")


def handle_pricer_request(pricing_method):
    """generate response with a specified pricer method (get_price, get_delta, get_greeks etc.)"""
    product_set = get_payload(request)
    if product_set is None:
        # if product set file cannot be parsed to json, send error 591
        return "Invalid product set description file", CODE_INVALID_FILE
    else:
        # Do pricing
        # if exception happened, send error 592
        # else send pricing result with response 200
        try:
            result = do_pricing(product_set, pricing_method)
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


def do_pricing(product_set, pricing_method):
    """Do pricing for each option in the product set, and return pricing result as a list"""
    result = []
    for desc in product_set['Products']:
        # create option DTO
        option = VanillaOption(desc)

        # create option pricer with Black-Scholes Model
        option_pricer = OptionPricer(BlackScholesModel(option))

        # invoke pricer with a specified method
        ret = invoke_pricer_by_method(option_pricer, pricing_method)

        # append pricing result to the final result set
        ret['description'] = option.describe_option()
        result.append(ret)
    return {'result': result}


def invoke_pricer_by_method(option_pricer, pricing_method, *args, **kwargs):
    return getattr(option_pricer, pricing_method)(*args, **kwargs)


def create_server():
    return app
