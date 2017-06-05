from QueryFrame import *
from WitUtils import *
from VitibotWineDotComLink import *
from Wine import *

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
        print(ack)

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
                    if m == "type": # TODO: if varietal specified, can skip this?
                        prompt = "Do you have a preferred type of wine? If so, what kind? Common colors are red, white, and blush."
                        self.operationsStack.append(m)
                        break
                    if m == "min_price" or m == "max_price":
                        prompt = "Are you on a budget? If so, what's your spending range?"
                        self.operationsStack.append("min_price")
                        self.operationsStack.append("max_price")
                        break

        # Everything from this point on is just for a baseline.  As long as the request is not empty, execute the query and give back the first wine
        if self.queryFrame.isEmpty():
            print "I didn't get any query information from that statement."
        else:
            self.currentState()

        if prompt != "":
            return "I need some more information.\n" + prompt + "\n"

        # if all (ask) params either filled in frame or asked in operationStack
        self.executeQuery()
        # save old queryFrame to list
        self.previousQueries.append(self.queryFrame)
        self.clearQueryFrame()
        # clear operation stack
        self.operationsStack = []

        if self.wineList is None:
            return "The wine list is still None, this probs shouldn't happen.\n"
        elif len(self.wineList) == 0:
            return "I'm sorry there were no wines which matched your description.\n"
        else:
            return "Here is the wine I chose for you:\n%s\n\nYou can now start a new search." % (str(self.wineList[0]))

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

        # first, check to see if we got a classified intent.
        intent = first_entity_value(parsedInput, 'intent')
        if intent in self.actions:
            return self.actions[intent](parsedInput)
        elif intent is not None:
            return "I'm sorry, but I don't know how to do that: " + intent


        # else if parsedInput has any extracted params, check operation stack + set specific param

        if 'color' in parsedInput and self.operationsStack[-1] == 'type':
            # set slot to color
            self.operationsStack.append("answered")
            return self.setQueryParams(parsedInput)
        elif 'binary' in parsedInput and self.operationsStack[-1] == 'type':
            ans = first_entity_value(parsedInput, 'binary')
            if ans == "yes":
                return "What is your preference between red, white, and blush wines?"
            elif ans == "no":
                print "Ok, so you don't have a preference in wine type."
                self.operationsStack.append("answered")
                return self.setQueryParams(parsedInput)

        if ('min_price' in parsedInput or 'max_price' in parsedInput) and self.operationsStack[-1] == 'max_price':
            # set price slots
            self.operationsStack.append("answered")
            return self.setQueryParams(parsedInput)
        elif 'binary' in parsedInput and self.operationsStack[-1] == 'max_price':
            ans = first_entity_value(parsedInput, 'binary')
            if ans == "yes":
                return "What is price range?"
            elif ans == "no":
                print "Ok, so you don't have a price range."
                self.operationsStack.append("answered")
                return self.setQueryParams(parsedInput)

        return ''