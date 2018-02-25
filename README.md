# VanillaOptionPricer
Vanilla Option Pricer REST API Service

## Swagger
https://app.swaggerhub.com/apis/zsq-cyber8/VanillaOptionPricer/1.0.0

## Design
#### Project structure
* ```core```
  * ```constants.py``` Constants such as date format, status code, rounding etc
  * ```pricer.py``` Option pricer that accepts a model and invoke pricing action
  * ```pricing_models.py``` Contains an abstract base class for models, and implementation of Black-Scholes Model
* ```models```
  * ```option.py``` Defines a Data Transfer Object to carry information of an option
* ```services```
  * ```server.py``` Implementation of option pricer server based on Flask framework
  * ```client.py``` A client to test the pricer service
* ```utils```
  * ```datetime_utils``` Datetime utils, e.g. convert date string to date object
* ```test```
  * All unit tests
* ```resources```
  * ProductSet description json files for testing purpose
* ```run_server.py``` For demo
* ```run_client.py``` For demo

#### Special case assumption
If volatility (sigma) is zero, my current handling is to return 0 for both price and all greeks.
This might need to improve with further discussion.

## Setup
This project is tested with python 2.7.14
To setup an virtual environment with all required dependencies

Download requirements.txt in the project
```
requirements.txt
```

Linux
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows
```
pip install virtualenv
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run
To start server
```
python run_server.py
```

To start client
```
python run_client.py
```

## Demo
##### *Pricing result for product set A*
![image](https://github.com/zsq-cyber/VanillaOptionPricer/blob/master/screenshots/ProductSetAPricing.png)
