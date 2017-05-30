from QuerySlot import *

class QueryFrame:
    def __init__(self):
        self.slots = {}

        # Set up all the empty slots
        self.slots['type'] = QuerySlot('type', True)
        self.slots['varietal'] = QuerySlot('varietal')
        self.slots['min price'] = QuerySlot('min price', True)
        self.slots['max price'] = QuerySlot('max price', True)
        self.slots['vintage'] = QuerySlot('vintage')
        self.slots['rating'] = QuerySlot('rating')
        self.slots['country'] = QuerySlot('country')
        self.slots['region'] = QuerySlot('region')
        self.slots['appellation'] = QuerySlot('appellation')
        self.slots['labels'] = QuerySlot('labels')

    def getUnfilledSlotPrompts(self):
        promptSlots = []
        for key in self.slots:
            if self.slots[key].shouldPromptUser():
                promptSlots.append(key)
        return promptSlots

    def getRequestParams(self):
        pass