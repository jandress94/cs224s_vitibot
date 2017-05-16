import sys
from wit import Wit

access_token = 'QFQBBJPMRBQTK5A35GTK5PIKYIQZZHN3'

color_dict = {}

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def send(request, response):
    print(response['text'])

def trim_possessive_from_name(name):
    return name[:-2] if name.endswith("'s") else name

def remember_color(request):
    context = request['context']
    entities = request['entities']

    person = first_entity_value(entities, 'contact')
    person = trim_possessive_from_name(person)
    color = first_entity_value(entities, 'color')

    context.clear()

    if person and color:
        context['person'] = person
        context['color'] = color
        color_dict[person] = color
    else:
        context['missing_info'] = True

    return context

def query_color(request):
    context = request['context']
    entities = request['entities']

    person = first_entity_value(entities, 'contact')
    person = trim_possessive_from_name(person)

    context.clear()

    if person:
        if person in color_dict:
            context['person'] = person
            context['color'] = color_dict[person]
        else:
            context['person_missing_color'] = person
    else:
        context['missing_person'] = True

    return context

actions = {
    'rememberColor': remember_color,
    'queryColor': query_color,
    'send': send
}


print('This is a simple test program for Wit.ai')
print('Basically, it keeps a dictionary of people and their favorite colors.')
print("You can either ask it about someones's favorite color (e.g. \"What color does Jim like?\")")
print("or you can tell it a fact about someone's favorite color (e.g. \"Jim's favorite color is red.\").")

client = Wit(access_token=access_token, actions=actions)
client.interactive()