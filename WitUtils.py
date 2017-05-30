def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def getEntitiesFromResponse(jsonResponse):
    return jsonResponse['entities'] if 'entities' in jsonResponse else None