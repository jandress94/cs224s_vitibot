import sys
from wit import Wit
import requests
import random

wit_access_token = 'VOZBU6UDWIKBSKSZKCZCLACZPOYCECZK'
wine_access_token = '81fbbbb3dc3337a13df4fec1230eb5e7'

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def send(request, response):
    print(response['text'])

def get_wine(request):
    context = request['context']
    entities = request['entities']

    context.clear()

    color = first_entity_value(entities, 'color')

    if color == 'red':
        category_code = 124
    elif color == 'white':
        category_code = 125
    else:
        return context

    payload = {
        'filter': 'categories(490+%d)' % (category_code),
        'offset': random.randint(1, 1000),
        'size': 1,
        'apikey': wine_access_token
    }
    r = requests.get('http://services.wine.com/api/beta2/service.svc/json/catalog', params = payload)

    if r.status_code != 200:
        context['error_message'] = 'GET request had status %d' % (r.status_code)
        return context

    json = r.json()

    context['wine_info'] = json['Products']['List'][0]['Name']
    return context


actions = {
    'getWine': get_wine,
    'send': send
}

print " __      ___ _   _ ____        _   "
print " \ \    / (_) | (_)  _ \      | |  "
print "  \ \  / / _| |_ _| |_) | ___ | |_ "
print "   \ \/ / | | __| |  _ < / _ \| __|"
print "    \  /  | | |_| | |_) | (_) | |_ "
print "     \/   |_|\__|_|____/ \___/ \__|"
print ""
print "Ask me for a recommended bottle of either red or white wine."

client = Wit(access_token=wit_access_token, actions=actions)
client.interactive()