import json
with open('./category json.txt') as json_file:
    data = json.load(json_file)

    categories = data['Categories']
    varietals = categories[7]
    refinements = varietals['Refinements']

    for elem in refinements:
        print("        '%s': %d," % (elem['Name'], elem['Id']))