try:
    from urllib import urlencode, unquote
    from urlparse import urlparse, parse_qsl, ParseResult
except ImportError:
    # Python 3 fallback
    from urllib.parse import (
        urlencode, unquote, urlparse, parse_qsl, ParseResult
    )
import requests
import json
from json import dumps 
import time
# k5CqAUoCNO-nLKfNKpNZH2b1DAxLAo070
# 024d75fff9ad6a41d6302af488fce6ca

api_key = '024d75fff9ad6a41d6302af488fce6ca'
url = 'https://financialmodelingprep.com/api/v3/profile/'
def add_url_params(url, params):
    url+=params['SYMBOL']
    print(url)
    url = unquote(url)
    parsed_url = urlparse(url)
    get_args = parsed_url.query
    parsed_get_args = dict(parse_qsl(get_args))
    parsed_get_args.update(params)
    # Bool and Dict values should be converted to json-friendly values
    # you may throw this part away if you don't like it :)
    parsed_get_args.update(
        {k: dumps(v) for k, v in parsed_get_args.items()
         if isinstance(v, (bool, dict))}
    )

    # Converting URL argument to proper query string
    encoded_get_args = urlencode(parsed_get_args, doseq=True)
    # Creating new parsed result object based on provided with new
    # URL arguments. Same thing happens inside of urlparse.
    new_url = ParseResult(
        parsed_url.scheme, parsed_url.netloc, parsed_url.path,
        parsed_url.params, encoded_get_args, parsed_url.fragment
    ).geturl()

    return new_url
def get_stock_info(symbol, url):
    params = { 'apikey': api_key, 'SYMBOL': symbol }
    url = add_url_params(url, params)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def run_info_getter():
    url = 'https://financialmodelingprep.com/api/v3/profile/'
    stock_sym = input("Enter a stock symbol: ")
    while stock_sym != 'exit':
        stock_sym.upper()
        stock_info = get_stock_info(stock_sym.upper(), url)
        # print(stock_info[0])
        for key, value in stock_info[0].items():
            key = key.upper()
            print(key+": "+str(value)) 
        stock_sym = input("Enter a stock symbol: ")
# this functions uses the coingecko api to get the list of coins and their prices
def list_of_cryptos():
    url = 'https://api.coingecko.com/api/v3/coins/list'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None