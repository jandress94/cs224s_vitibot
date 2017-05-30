import requests
import random
from constants import *

def getRandomWine(color_code):
    payload = {
        'filter': 'categories(490+%d)' % (color_code),
        'offset': random.randint(1, 1000),
        'size': 1,
        'apikey': wine_access_token
    }
    r = requests.get('http://services.wine.com/api/beta2/service.svc/json/catalog', params = payload)

    if r.status_code != 200:
        return None

    return r.json()['Products']['List'][0]