import requests
import json
from collections import namedtuple
import datetime

r = requests.get('https://api.coinmarketcap.com/v2/listings/') # this is blocking !!!!!!!!!!!!!
print (r.status_code)
x = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

names_list = []
sym_list = []

def crypto_list():
    for c in x.data:
        names_list.append(c.name)
        sym_list.append(c.symbol)
    return (names_list, sym_list)
