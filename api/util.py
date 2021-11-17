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

def add_url_params(url, params):
    if params.get('SYMBOL'):
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