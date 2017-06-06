from QueryFrame import *
from VitibotWineDotComLink import *
from Wine import *

class VitibotState:
    def __init__(self, verbose = False, useBaseline = False):
        self.queryFrame = QueryFrame()
        self.wineList = None
        self.wineListIndex = None
        self.operationsStack = []
        self.previousQueries = []
        self.verbose = verbose
        self.useBaseline = useBaseline

    def currentState(self):
        params = self.queryFrame.getFilledSlots()
        #print params
        ack = "Ok, so you're looking for a"
        if 'vintage' in params:
            ack = ack + " " + str(params['vintage'].getValue())
        if 'varietal' in params:
            ack = ack + " " + params['varietal'].getValue()
        elif 'type' in params:
            ack = ack + " " + params['type'].getValue()
        ack += " wine"
        if 'region' in params:
            ack = ack + " from " + params['region'].getValue()
        elif 'country' in params:
            ack = ack + " from " + params['country'].getValue()
        if 'min_price' in params and 'max_price' in params:
            ack = ack + (" costing between %d and %d dollars"%(params['min_price'].getValue(),params['max_price'].getValue()))
        elif 'min_price' in params:
            ack = ack + (" costing at least %d dollars"%(params['min_price'].getValue()))
        elif 'max_price' in params:
            ack = ack + (" costing no more than %d dollars"%(params['max_price'].getValue()))
        ack += "."
        if 'pairing' in params:
            ack = ack + (" Recalling your food choices, they are: %s.  I'll see what wine pairs well with that."%(', '.join(params['pairing'].getValue().split('+'))))
        print(ack)

    # def promptPairing(self, entities):
    #     if entities is None:
    #         # prompt with dictionary layer one question
    #         self.operationsStack.append("pairing-type")
    #         return # + " Will it be %s or none of those?"%(', '.join(foodPairings['categories'].keys()))
    #     elif 'type' in entities and self.operationsStack[-1] == 'pairing-type':
    #         # set slot, ask next question
    #         pairing_type = first_entity_value(entities, 'type')
    #         if pairing_type not in foodPairings['categories']:
    #             return "That's not a valid type. Type of food includes: %s, or none.\nLet me know which one closest matches your meal."%(', '.join(foodPairings['categories'].keys()))
    #         self.queryFrame.setSlotValue('pairing', pairing_type)
    #         self.operationsStack.append("pairing-ingredient")
    #         return foodPairings['categories'][pairing_type]['question']# + " Will it be %s or none of those?"%(', '.join(foodPairings['categories'][pairing_type]['categories'].keys()))
    #     elif 'main_ingredient' in entities and self.operationsStack[-1] == 'pairing-ingredient':
    #         # set slot, ask next question
    #         p = self.queryFrame.slots['pairing'].getValue().split("+")
    #         pairing_ing = first_entity_value(entities, 'main_ingredient')
    #         if pairing_ing not in foodPairings['categories'][p[0]]['categories']:
    #             return "That's not a valid ingredient. Main ingredient for %s include: %s, or none.\nLet me know which one closest matches your meal."%(p[0],', '.join(foodPairings['categories'][p[0]].keys()))
    #         curr_pairing = "%s+%s"%(self.queryFrame.slots['pairing'].getValue(),pairing_ing)
    #         self.queryFrame.setSlotValue('pairing', curr_pairing)
    #         p = self.queryFrame.slots['pairing'].getValue().split("+")
    #         if 'question' in foodPairings['categories'][p[0]]['categories'][p[1]]:
    #             self.operationsStack.append("pairing-style")
    #             return foodPairings['categories'][p[0]]['categories'][p[1]]['question']# + " Will it be %s or none of those?"%(', '.join(foodPairings['categories'][p[0]]['categories'][p[1]]['categories'].keys()))
    #         else:
    #             self.operationsStack.append("answered")
    #             return self.setQueryParams(entities)
    #     elif 'style' in entities and self.operationsStack[-1] == 'pairing-style':
    #         # set slot, add answered, setQueryParams.
    #         pairing_style = first_entity_value(entities, 'style')
    #         p = self.queryFrame.slots['pairing'].getValue().split("+")
    #         if pairing_style not in foodPairings['categories'][p[0]]['categories'][p[1]]['categories']:
    #             return "Styles for %s: %s include: %s, or none.\nLet me know which one closest matches your meal."%(p[0],p[1],', '.join(foodPairings['categories'][p[0]]['categories'][p[1]].keys()))
    #         curr_pairing = "%s+%s"%(self.queryFrame.slots['pairing'].getValue(),pairing_style)
    #         self.queryFrame.setSlotValue('pairing', curr_pairing)
    #         p = self.queryFrame.slots['pairing'].getValue().split("+")
    #         self.operationsStack.append("answered")
    #         return self.setQueryParams(entities)
    #     elif 'binary' in entities:
    #         # finalize pairing, do no reprompt. set answered, setQueryParams
    #         b = first_entity_value(entities, 'binary')
    #         if b == "no":
    #             self.operationsStack.append("answered")
    #             return self.setQueryParams(entities)
    #         else:
    #             #reprompt
    #             p = self.queryFrame.slots['pairing'].getValue().split("+")
    #             if self.operationsStack[-1] == 'pairing-type':
    #                 return 
    #             elif self.operationsStack[-1] == 'pairing-ingredient':
    #                 return "Main ingredient for %s include: %s, or none.\nLet me know which one closest matches your meal."%(p[0],', '.join(foodPairings['categories'][p[0]]['categories'].keys()))
    #             elif self.operationsStack[-1] == 'pairing-style':
    #                 return "Styles for %s: %s include: %s, or none.\nLet me know which one closest matches your meal."%(p[0],p[1],', '.join(foodPairings['categories'][p[0]]['categories'][p[1]]['categories'].keys()))
    #             else:
    #                 self.operationsStack.append("answered")
    #                 return "I'm not sure what your pairing is. Let's move on."
    #     else:
    #         p = self.queryFrame.slots['pairing'].getValue()
    #         if p is not None:
    #             p = p.split("+")
    #         if self.operationsStack[-1] == 'pairing-type':
    #             return "Type of food includes: %s, or none.\nLet me know which one closest matches your meal."%(', '.join(foodPairings['categories'].keys()))
    #         elif self.operationsStack[-1] == 'pairing-ingredient':
    #             return "Main ingredient for %s include: %s, or none.\nLet me know which one closest matches your meal."%(p[0],', '.join(foodPairings['categories'][p[0]]['categories'].keys()))
    #         elif self.operationsStack[-1] == 'pairing-style':
    #             return "Styles for %s: %s include: %s, or none.\nLet me know which one closest matches your meal."%(p[0],p[1],', '.join(foodPairings['categories'][p[0]]['categories'][p[1]]['categories'].keys()))
    #         else:
    #             self.operationsStack.append("answered")
    #             return "I'm not sure what your pairing is. Let's move on."

    

    def clearQueryFrame(self, entities = None):
        self.queryFrame = QueryFrame()

    def executeQuery(self, entities = None):
        self.wineList = executeWineQuery(self.queryFrame, verbose = self.verbose)

    def setWineIndex(self, entities):
        pass

    def setWineIndexBasedOnText(self, entities):
        pass