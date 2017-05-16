from __future__ import unicode_literals
import sys
from wit import Wit
import requests
import random
from prompt_toolkit import prompt

wit_access_token = 'VOZBU6UDWIKBSKSZKCZCLACZPOYCECZK'
wine_access_token = '81fbbbb3dc3337a13df4fec1230eb5e7'
INTERACTIVE_PROMPT = '> '

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def send(request, response):
    print(response['text'])

def get_wine(context, entities):
    context.clear()

    color = first_entity_value(entities, 'color')

    if color is None:
        return 'no color'
    if color == 'red':
        category_code = 124
    elif color == 'white':
        category_code = 125
    else:
        return 'unknown color: %s' % (color)

    payload = {
        'filter': 'categories(490+%d)' % (category_code),
        'offset': random.randint(1, 1000),
        'size': 1,
        'apikey': wine_access_token
    }
    r = requests.get('http://services.wine.com/api/beta2/service.svc/json/catalog', params = payload)

    if r.status_code != 200:
        return 'GET request had status %d' % (r.status_code)

    json = r.json()

    return 'Here is the wine I chose: %s' % (json['Products']['List'][0]['Name'])


actions = {
    'getWine': get_wine,
    'send': send
}

def process_message_results(json_result):
    if not 'entities' in json_result:
        print('Did not get any entities from that message, sorry.')
        print(json_result)
        return

    entities = json_result['entities']

    if 'intent' not in entities:
        print('Did not get an intent from that message, sorry.')
        print(json_result)
        return

    intent = first_entity_value(entities, 'intent')

    if intent in actions:
        result = actions[intent]({}, entities)
        if result is not None:
            print(result)
    else:
        print('No action defined for intent "%s"' % (intent))

if __name__ == '__main__':

    print " __      ___ _   _ ____        _   "
    print " \ \    / (_) | (_)  _ \      | |  "
    print "  \ \  / / _| |_ _| |_) | ___ | |_ "
    print "   \ \/ / | | __| |  _ < / _ \| __|"
    print "    \  /  | | |_| | |_) | (_) | |_ "
    print "     \/   |_|\__|_|____/ \___/ \__|"
    print ""
    print "Ask me for a recommended bottle of either red or white wine."


    client = Wit(access_token=wit_access_token, actions=actions)

    if len(sys.argv) != 2 or not sys.argv[1].endswith('.wav'):
        print('You did not provide a .wav file, running interactive text mode.  Please enter your query')
        message = prompt(INTERACTIVE_PROMPT, mouse_support=True).rstrip()
        json_result = client.message(message)
    else:
        f = open(sys.argv[1])
        json_result = client.speech(f, None, {'Content-Type': 'audio/wav'})
        f.close()

    process_message_results(json_result)