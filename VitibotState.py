from QueryFrame import *
from WitUtils import *
from VitibotWineDotComLink import *
from Wine import *
from FoodPairings import *

class VitibotState:
    def __init__(self, verbose = False):
        self.queryFrame = QueryFrame()
        self.wineList = None
        self.wineListIndex = None
        self.operationsStack = []
        self.previousQueries = []
        self.verbose = verbose

        self.actions = {
            # 'getWine': self.getRandomWine
            'setQuery': self.setQueryParams
        }

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

    def promptPairing(self, entities):
        if entities is None:
            # prompt with dictionary layer one question
            self.operationsStack.append("pairing-type")
            return foodPairings['question']# + " Will it be %s or none of those?"%(', '.join(foodPairings['categories'].keys()))
        elif 'type' in entities and self.operationsStack[-1] == 'pairing-type':
            # set slot, ask next question
            pairing_type = first_entity_value(entities, 'type')
            if pairing_type not in foodPairings['categories']:
                return "That's not a valid type. Type of food includes: %s, or none.\nLet me know which one closest matches your meal."%(', '.join(foodPairings['categories'].keys()))
            self.queryFrame.setSlotValue('pairing', pairing_type)
            self.operationsStack.append("pairing-ingredient")
            return foodPairings['categories'][pairing_type]['question']# + " Will it be %s or none of those?"%(', '.join(foodPairings['categories'][pairing_type]['categories'].keys()))
        elif 'main_ingredient' in entities and self.operationsStack[-1] == 'pairing-ingredient':
            # set slot, ask next question
            p = self.queryFrame.slots['pairing'].getValue().split("+")
            pairing_ing = first_entity_value(entities, 'main_ingredient')
            if pairing_ing not in foodPairings['categories'][p[0]]['categories']:
                return "That's not a valid ingredient. Main ingredient for %s include: %s, or none.\nLet me know which one closest matches your meal."%(p[0],', '.join(foodPairings['categories'][p[0]].keys()))
            curr_pairing = "%s+%s"%(self.queryFrame.slots['pairing'].getValue(),pairing_ing)
            self.queryFrame.setSlotValue('pairing', curr_pairing)
            p = self.queryFrame.slots['pairing'].getValue().split("+")
            if 'question' in foodPairings['categories'][p[0]]['categories'][p[1]]:
                self.operationsStack.append("pairing-style")
                return foodPairings['categories'][p[0]]['categories'][p[1]]['question']# + " Will it be %s or none of those?"%(', '.join(foodPairings['categories'][p[0]]['categories'][p[1]]['categories'].keys()))
            else:
                self.operationsStack.append("answered")
                return self.setQueryParams(entities)
        elif 'style' in entities and self.operationsStack[-1] == 'pairing-style':
            # set slot, add answered, setQueryParams.
            pairing_style = first_entity_value(entities, 'style')
            p = self.queryFrame.slots['pairing'].getValue().split("+")
            if pairing_style not in foodPairings['categories'][p[0]]['categories'][p[1]]['categories']:
                return "Styles for %s: %s include: %s, or none.\nLet me know which one closest matches your meal."%(p[0],p[1],', '.join(foodPairings['categories'][p[0]]['categories'][p[1]].keys()))
            curr_pairing = "%s+%s"%(self.queryFrame.slots['pairing'].getValue(),pairing_style)
            self.queryFrame.setSlotValue('pairing', curr_pairing)
            p = self.queryFrame.slots['pairing'].getValue().split("+")
            self.operationsStack.append("answered")
            return self.setQueryParams(entities)
        elif 'binary' in entities:
            # finalize pairing, do no reprompt. set answered, setQueryParams
            b = first_entity_value(entities, 'binary')
            if b == "no":
                self.operationsStack.append("answered")
                return self.setQueryParams(entities)
            else:
                #reprompt
                p = self.queryFrame.slots['pairing'].getValue().split("+")
                if self.operationsStack[-1] == 'pairing-type':
                    return "Type of food includes: %s, or none.\nLet me know which one closest matches your meal."%(', '.join(foodPairings['categories'].keys()))
                elif self.operationsStack[-1] == 'pairing-ingredient':
                    return "Main ingredient for %s include: %s, or none.\nLet me know which one closest matches your meal."%(p[0],', '.join(foodPairings['categories'][p[0]]['categories'].keys()))
                elif self.operationsStack[-1] == 'pairing-style':
                    return "Styles for %s: %s include: %s, or none.\nLet me know which one closest matches your meal."%(p[0],p[1],', '.join(foodPairings['categories'][p[0]]['categories'][p[1]]['categories'].keys()))
                else:
                    self.operationsStack.append("answered")
                    return "I'm not sure what your pairing is. Let's move on."
        else:
            p = self.queryFrame.slots['pairing'].getValue()
            if p is not None:
                p = p.split("+")
            if self.operationsStack[-1] == 'pairing-type':
                return "Type of food includes: %s, or none.\nLet me know which one closest matches your meal."%(', '.join(foodPairings['categories'].keys()))
            elif self.operationsStack[-1] == 'pairing-ingredient':
                return "Main ingredient for %s include: %s, or none.\nLet me know which one closest matches your meal."%(p[0],', '.join(foodPairings['categories'][p[0]]['categories'].keys()))
            elif self.operationsStack[-1] == 'pairing-style':
                return "Styles for %s: %s include: %s, or none.\nLet me know which one closest matches your meal."%(p[0],p[1],', '.join(foodPairings['categories'][p[0]]['categories'][p[1]]['categories'].keys()))
            else:
                self.operationsStack.append("answered")
                return "I'm not sure what your pairing is. Let's move on."

    def setQueryParams(self, entities):
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

        vintage = first_entity_value(entities, 'vintage')
        if vintage is not None:
            self.queryFrame.setSlotValue('vintage', vintage)

        missing = self.queryFrame.getUnfilledSlotPrompts()
        prompt = ""
        if len(missing) > 0:
            for m in missing:
                if m not in self.operationsStack:
                    if m == "type" and "varietal" not in self.queryFrame.getFilledSlots(): # TODO: if varietal specified, can skip this?
                        prompt = "Do you have a preferred type of wine? If so, what kind? Common colors are red, white, and blush."
                        self.operationsStack.append(m)
                        break
                    if m == "min_price" or m == "max_price":
                        prompt = "Are you on a budget? If so, what's your spending range?"
                        self.operationsStack.append("min_price")
                        self.operationsStack.append("max_price")
                        break
                    if m == "pairing":
                        self.operationsStack.append("pairing")
                        print "I need some more information."
                        return self.promptPairing(None)

        # Everything from this point on is just for a baseline.  As long as the request is not empty, execute the query and give back the first wine
        if self.queryFrame.isEmpty():
            print "I didn't get any query information from that statement."
        else:
            self.currentState()

        if prompt != "":
            return "I need some more information.\n" + prompt + "\n"

        # if all (ask) params either filled in frame or asked in operationStack
        if self.queryFrame.slots['pairing'].getValue() is not None:
            p = self.queryFrame.slots['pairing'].getValue().split("+")
            if len(p) == 3:
                food_entry = foodPairings['categories'][p[0]]['categories'][p[1]]['categories'][p[2]]
            elif len(p) == 2:
                food_entry = foodPairings['categories'][p[0]]['categories'][p[1]]
            elif len(p) == 1:
                food_entry = foodPairings['categories'][p[0]]
            if 'blurb' in food_entry:
                print "About your food choice: " + food_entry['blurb']

        self.executeQuery()
        # save old queryFrame to list
        self.previousQueries.append(self.queryFrame)
        self.clearQueryFrame()
        # clear operation stack
        self.operationsStack = []

        if self.wineList is None:
            return "The wine list is still None, this probs shouldn't happen.\n"
        elif len(self.wineList) == 0:
            return "I'm sorry, but I could not find a good wine which matches your description.  You can try a different search.\n"
        else:
            return "Here is the wine I chose for you:\n%s\n\n  I hope you enjoy the recommendation!\nFeel free to start a new search." % (str(self.wineList[0]))

    def clearQueryFrame(self, entities = None):
        self.queryFrame = QueryFrame()

    def executeQuery(self, entities = None):
        self.wineList = executeWineQuery(self.queryFrame, verbose = self.verbose)

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
        if self.verbose: print parsedInput
        # first, check if the operations stack is non-empty
        lastOp = None
        if len(self.operationsStack) > 0:
            lastOp = self.operationsStack[-1]

        if lastOp is not None:
            promptedPairing = (lastOp.split("-")[0] == "pairing")
            if ('binary' in parsedInput and promptedPairing) or ('type' in parsedInput and lastOp == 'pairing-type') or ('main_ingredient' in parsedInput and lastOp == 'pairing-ingredient') or ('style' in parsedInput and lastOp == 'pairing-style'):
                #print "I need to know more about your meal."
                return self.promptPairing(parsedInput)

            if 'color' in parsedInput and lastOp == 'type':
                # set slot to color
                self.operationsStack.append("answered")
                return self.setQueryParams(parsedInput)
            elif 'binary' in parsedInput and lastOp == 'type':
                ans = first_entity_value(parsedInput, 'binary')
                if ans == "yes":
                    return "What is your preference between red, white, and blush wines?"
                elif ans == "no":
                    print "Ok, so you don't have a preference in wine type."
                    self.operationsStack.append("answered")
                    return self.setQueryParams(parsedInput)

            if ('min_price' in parsedInput or 'max_price' in parsedInput) and lastOp == 'max_price':
                # set price slots
                self.operationsStack.append("answered")
                return self.setQueryParams(parsedInput)
            elif 'binary' in parsedInput and lastOp == 'max_price':
                ans = first_entity_value(parsedInput, 'binary')
                if ans == "yes":
                    return "What is price range?"
                elif ans == "no":
                    print "Ok, so you don't have a price range."
                    self.operationsStack.append("answered")
                    return self.setQueryParams(parsedInput)

        # Now, check to see if we got a classified intent.
        intent = first_entity_value(parsedInput, 'intent')
        if intent in self.actions:
            return self.actions[intent](parsedInput)
        elif intent is not None:
            return "I'm sorry, but I don't know how to do that: " + intent

        return "I'm sorry, but I could not understand your request."