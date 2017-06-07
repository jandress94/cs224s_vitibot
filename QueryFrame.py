from QuerySlot import *
import random

class QueryFrame:
    def __init__(self):
        self.slots = {}

        # Set up all the empty slots
        self.slots['type'] = QuerySlot('type', True)
        self.slots['varietal'] = QuerySlot('varietal')
        self.slots['min_price'] = QuerySlot('min_price', True)
        self.slots['max_price'] = QuerySlot('max_price', True)
        self.slots['vintage'] = QuerySlot('vintage')
        self.slots['rating'] = QuerySlot('rating')
        self.slots['wineLoc'] = QuerySlot('wineLoc')
        self.slots['pairing'] = QuerySlot('pairing', True)

    def setSlotValue(self, slot, value):
        if slot in self.slots:
            self.slots[slot].value = value

    def isEmpty(self):
        for key in self.slots:
            if self.slots[key].value is not None:
                return False
        return True

    def getUnfilledSlotPrompts(self):
        unfilled = [key for key in self.slots if self.slots[key].shouldPromptUser()]
        random.shuffle(unfilled)
        return unfilled

    def getFilledSlots(self):
        return {key: self.slots[key] for key in self.slots if self.slots[key].value is not None}

    def __str__(self):
        resultString = 'QueryFrame:'
        foundSetSlot = False

        for key in self.getFilledSlots():
            foundSetSlot = True
            resultString += '\n  %s: %s' % (key, self.slots[key].value)

        if not foundSetSlot:
            resultString += '\n  QueryFrame has no set slots'
            
        return resultString