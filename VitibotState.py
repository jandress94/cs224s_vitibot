from QueryFrame import *
from WitUtils import *
from VitibotWineDotComLink import *


class VitibotState:
    def __init__(self):
        self.queryFrame = QueryFrame()
        self.wineList = None
        self.wineListIndex = None
        self.operationsStack = []

        self.actions = {
            # 'getWine': self.getRandomWine
            'setQuery': self.setQueryParams
        }

    def setQueryParams(self, entities):
        # print(entities)

        color = first_entity_value(entities, 'color')
        if color is not None:
            self.queryFrame.setSlotValue('type', color)

        country = first_entity_value(entities, 'country')
        if country is not None:
            self.queryFrame.setSlotValue('country', country)

        max_price = first_entity_value(entities, 'max')
        if max_price is not None:
            self.queryFrame.setSlotValue('max_price', max_price)

        min_price = first_entity_value(entities, 'min')
        if min_price is not None:
            self.queryFrame.setSlotValue('min_price', min_price)

        varietal = first_entity_value(entities, 'varietal')
        if varietal is not None:
            self.queryFrame.setSlotValue('varietal', varietal)

        return str(self.queryFrame)

    def setQuerySlot(self, slot, value):
        pass

    def executeQuery(self, entities):
        pass

    def setWineIndex(self, entities):
        pass

    def setWineIndexBasedOnText(self, entities):
        pass

    def getRandomWine(self, entities):
        color = first_entity_value(entities, 'color')

        if color is None:
            return "I'm sorry, I didn't detect a color in your wine request."
        if color == 'red':
            category_code = 124
        elif color == 'white':
            category_code = 125
        else:
            return 'unknown color: %s' % (color)

        wine = getRandomWine(category_code)
        if wine is None:
            return "I'm sorry, I couldn't get any wines."

        return 'Here is the wine I chose: %s' % (wine['Name'])

    '''
    This is the function that serves as the main interface between the state and the outside world.
    It should be passed in the entities dictionary detected by Wit.
    Based on the intent that Wit detects, it will call one of various other functions.
    It returns a string that should be printed as Vitibot's part of the dialog.
    '''
    def respondToDialog(self, parsedInput):
        if 'intent' not in parsedInput:
            return "I'm sorry, I couldn't determine what you are trying to have me do."

        intent = first_entity_value(parsedInput, 'intent')

        if intent not in self.actions:
            return "I'm sorry, but I don't know how to do that."

        return self.actions[intent](parsedInput)