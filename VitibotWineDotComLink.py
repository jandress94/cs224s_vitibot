import requests
import random
from constants import *
from Wine import *

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

def addFilterWithValue(filters, key, value):
    if key not in filters:
        filters[key] = []

    filters[key].append(str(value))

def getFilters(filledSlots):
    #TODO: check what adding in 490 to the categories filter does

    filters = {}
    min_price = 0
    max_price = 1000
    changedPrice = False

    for key in filledSlots:
        value = filledSlots[key].value
        if key == 'type':
            if value == 'red':
                addFilterWithValue(filters, 'categories', 124)
            elif value == 'white':
                addFilterWithValue(filters, 'categories', 125)
            elif value == 'rose':
                addFilterWithValue(filters, 'categories', 126)
            else:
                print('I currently cannot search for that type of wine: ' + value)

        elif key == 'varietal':
            if value == 'cabernet sauvignon':
                addFilterWithValue(filters, 'categories', 139)
            elif value == 'chardonnay':
                addFilterWithValue(filters, 'categories', 140)
            elif value == 'sauvignon blanc':
                addFilterWithValue(filters, 'categories', 151)
            elif value == 'pinot noir':
                addFilterWithValue(filters, 'categories', 143)
            else:
                print('I currently cannot search for that varietal: ' + value)

        elif key == 'min_price':
            min_price = value
            changedPrice = True

        elif key == 'max_price':
            max_price = value
            changedPrice = True

        elif key == 'vintage':
            if value == 1999:
                addFilterWithValue(filters, 'categories', 364)
            elif value == 2000:
                addFilterWithValue(filters, 'categories', 365)
            elif value == 2001:
                addFilterWithValue(filters, 'categories', 366)
            else:
                print('I currently cannot search for that vintage: %d' % (value))

        elif key == 'country':
            if value == 'France':
                addFilterWithValue(filters, 'categories', 102)
            elif value == 'Italy':
                addFilterWithValue(filters, 'categories', 105)
            elif value == 'United States':
                addFilterWithValue(filters, 'categories', 101)
            else:
                print('I currently cannot search for that country: ' + value)

    if changedPrice:
        addFilterWithValue(filters, 'price', "%d|%d" % (min_price, max_price))

    return filters

def executeWineQuery(queryFrame, verbose = False):
    filledSlots = queryFrame.getFilledSlots()

    filters = getFilters(filledSlots)                                               # {'categories': [1, 2, 3], 'price': ['12|34']}
    joinedFilters = {key: '(' + '+'.join(filters[key]) + ')' for key in filters}    # {'categories': '(1+2+3)', 'price': '(12|34)'}
    filtersWithNames = [key + joinedFilters[key] for key in joinedFilters]          # ['categories(1+2+3)', 'price(12|34)']
    
    payload = {
        'filter': '+'.join(filtersWithNames),
        'size': 5,
        'apikey': wine_access_token,
        'state': 'CA',
        'sort': 'popularity|descending'
    }
    if verbose:
        print("payload for the wine query request: %s" % (str(payload)))
    r = requests.get('http://services.wine.com/api/beta2/service.svc/json/catalog', params = payload)

    if r.status_code != 200:
        return None

    if verbose:
        print("full result json from wine query: %s" % (str(r.json())))
    return [Wine(wineJson) for wineJson in r.json()['Products']['List']]