import requests
import random
from constants import *
from Wine import *
from category_dict import *
from FoodPairings import *

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

def getFilters(filledSlots, verbose = False):
    #TODO: check what adding in 490 to the categories filter does

    filters = {}
    min_price = 0
    max_price = 1000
    changedPrice = False

    for key in filledSlots:
        value = filledSlots[key].value

        # key will be the name of one of the slots that has been filled, e.g. 'varietal'
        # value will be the set value for that slots, e.g. 'pinot noir'

        if key in category_dict:
            value = str(value).lower()
            if value in category_dict[key]:
                addFilterWithValue(filters, 'categories', category_dict[key][value])
                if verbose: print("Set the category filter %s to be %s." % (key, value))
            else:
                print("I'm sorry, I can't filter wines based on the %s %s." % (key, value))

        elif key == 'min_price':
            min_price = value
            changedPrice = True

        elif key == 'max_price':
            max_price = value
            changedPrice = True
        elif key == 'pairing':
            # value is a list
            curr_food_dict = foodPairings

            for i in xrange(len(value)):
                if 'categories' in curr_food_dict and value[i] in curr_food_dict['categories']:
                    curr_food_dict = curr_food_dict['categories'][value[i]]
                else:
                    break
            id = curr_food_dict['id']
            if id is not None:
                addFilterWithValue(filters, 'categories', id)
            else:
                print("I'm sorry, I can't filter wines based on the %s %s." % (key, value))

    if changedPrice:
        addFilterWithValue(filters, 'price', "%d|%d" % (min_price, max_price))

    return filters

def executeWineQuery(queryFrame, verbose = False):
    filledSlots = queryFrame.getFilledSlots()

    filters = getFilters(filledSlots, verbose)                                      # {'categories': [1, 2, 3], 'price': ['12|34']}
    joinedFilters = {key: '(' + '+'.join(filters[key]) + ')' for key in filters}    # {'categories': '(1+2+3)', 'price': '(12|34)'}
    filtersWithNames = [key + joinedFilters[key] for key in joinedFilters]          # ['categories(1+2+3)', 'price(12|34)']
    
    payload = {
        'filter': '+'.join(filtersWithNames),
        'size': 20,
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

    wineList = []
    for wineJson in r.json()['Products']['List']:
        try:
            wineList.append(Wine(wineJson))
        except Exception:
            pass

    return wineList[:5]