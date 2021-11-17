# list of S&P 500 companies

from apiConstants import *
from util import *
import requests
url = API_URL + "sp500_constituent"

def get_sp500_constituents(url):
    """
    Returns a list of S&P 500 companies
    """
    params = {'apikey' : API_KEY}
    new_url = add_url_params(url, params)
    print(new_url)
    temp = url+"?apikey="+API_KEY
    response = requests.get(temp)
    if response.status_code == 200:
        return response.json()
    else: 
        return response
sp_info = get_sp500_constituents(url)
print(sp_info)
