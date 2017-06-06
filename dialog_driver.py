from questions import *
from WitUtils import *
from FoodPairings import *
from VitibotWineDotComLink import *

def pairingProgression(entities, state):
    current_pairing_state = state.queryFrame.slots['pairing'].value
    if current_pairing_state is None:
        current_pairing_state = []
    pairing_question = None

    if len(current_pairing_state) == 0 and 'type' in entities:      # They gave a general pairing type
        pairing_type = first_entity_value(entities, 'type')
        current_pairing_state.append(pairing_type)

        pair_type_dict = foodPairings['categories'][pairing_type]
        pairing_question = Question(pair_type_dict['question']) \
                                    .add_valid_entity_response('main_ingredient', pairingProgression) \
                                    .set_no_response(True, text = "That's ok, but I won't be able to make much use of a generic pairing like \"%s\"." % (pairing_type)) \
                                    .add_invalid_entity_response("That's not a valid ingredient. Main ingredient for %s include: %s, or none.\nLet me know which one is the closest match for your meal."%(pairing_type,', '.join(pair_type_dict['categories'].keys())))
        
    elif 'main_ingredient' in entities and len(current_pairing_state) < 2:
        pairing_ing = first_entity_value(entities, 'main_ingredient')
        if len(current_pairing_state) == 0:
            for pairing_type in foodPairings['categories']:
                pair_type_dict = foodPairings['categories'][pairing_type]
                if pairing_ing in pair_type_dict['categories']:
                    current_pairing_state.append(pairing_type)
                    break

        pairing_type = current_pairing_state[0]
        current_pairing_state.append(pairing_ing)

        pair_ing_dict = foodPairings['categories'][pairing_type]['categories'][pairing_ing]
        if 'question' in pair_ing_dict:
            no_response = "Ok, I'll make my wine recommendation so that it pairs well with %s: %s in general." % (pairing_type, pairing_ing)
            if 'blurb' in pair_ing_dict:
                no_response += " %s" % (pair_ing_dict['blurb'])
            pairing_question = Question(pair_ing_dict['question']) \
                                    .add_valid_entity_response('style', pairingProgression) \
                                    .set_no_response(True, text = no_response) \
                                    .add_invalid_entity_response("Styles for %s: %s include %s, or none.\nLet me know which one closest matches your meal."%(pairing_type, pairing_ing,', '.join(pair_ing_dict['categories'].keys())))

    elif len(current_pairing_state) == 2 and 'style' in entities:   # The gave a specific style
        pairing_style = first_entity_value(entities, 'style')
        current_pairing_state.append(pairing_style)
        final_response = "Sounds delicious!  I will definitely take these foods into consideration!"

        pair_style_dict = foodPairings['categories'][current_pairing_state[0]]['categories'][current_pairing_state[1]]['categories'][pairing_style]
        if 'blurb' in pair_style_dict:
            final_response += " %s\n" % (pair_style_dict['blurb'])
        else:
            final_response += "\n"
        return final_response

    state.queryFrame.setSlotValue('pairing', current_pairing_state)

    state.operationsStack.append(pairing_question)
    return pairing_question.question_text

def getQueryString(state):
    params = state.queryFrame.getFilledSlots()
    #print params
    ack = "You're looking for a"
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
        ack = ack + (" Recalling your food choices, they are: (%s).  I'll see what wine pairs well with that."%(', '.join(params['pairing'].getValue())))
    return ack

def setQueryParams(entities, state):
    made_a_change = False
    response = "Ok, I'll take that into consideration.\n"

    color = first_entity_value(entities, 'color')
    if color is not None:
        state.queryFrame.setSlotValue('type', color)
        made_a_change = True

    country = first_entity_value(entities, 'country')
    if country is not None:
        state.queryFrame.setSlotValue('country', country)
        made_a_change = True

    max_price = first_entity_value(entities, 'max')
    if max_price is not None:
        state.queryFrame.setSlotValue('max_price', max_price)
        made_a_change = True

    min_price = first_entity_value(entities, 'min')
    if min_price is not None:
        state.queryFrame.setSlotValue('min_price', min_price)
        made_a_change = True

    varietal = first_entity_value(entities, 'varietal')
    if varietal is not None:
        state.queryFrame.setSlotValue('varietal', varietal)
        made_a_change = True

    vintage = first_entity_value(entities, 'vintage')
    if vintage is not None:
        state.queryFrame.setSlotValue('vintage', vintage)
        made_a_change = True

    if made_a_change:
        response += getQueryString(state) + '\n'

    pairing_type = first_entity_value(entities, 'type')
    if pairing_type is not None:
        return response + pairingProgression(entities, state)

    pairing_ing = first_entity_value(entities, 'main_ingredient')
    if pairing_ing is not None:
        return response + pairingProgression(entities, state)

    return response if made_a_change else ''


def handleQuestion(question, parsedInput, state):
    response = None
    isAnswered = True

    if 'binary' in parsedInput:
        binary_ans = first_entity_value(parsedInput, 'binary')
        if binary_ans == 'yes' and hasattr(question, 'yes'):
            response, isAnswered = question.yes
        elif binary_ans == 'no' and hasattr(question, 'no'):
            response, isAnswered = question.no
    else:
        for entity in question.entity_to_response_dict:
            if entity in parsedInput:
                response = question.entity_to_response_dict[entity]
                break
        if response is None and hasattr(question, 'default_response'):
            response = question.default_response

    if type(response) == str:
        question.answered = isAnswered
        return response + '\n'
    elif response is not None:
        question.answered = isAnswered
        return response(parsedInput, state)
    elif hasattr(question, 'invalid_response'):
        return question.invalid_response + '\n'


actions = {
    'setQuery': setQueryParams
}

what_color_quest = Question('Do you have a preferred type of wine? If so, what kind? Common colors are red, white, and rose.') \
                        .set_yes_response(False, text = "Which color do you prefer: red, white, or rose?") \
                        .set_no_response(True, text = "Ok, I'll base my recommendation on something other than the wine type.") \
                        .add_valid_entity_response('color', setQueryParams)
price_range_quest = Question("Are you on a budget? If so, what's your spending range?") \
                        .set_yes_response(False, text = "What is your price range?") \
                        .set_no_response(True, text = "Ok, I won't take price into account when selecting a wine.  Don't be mad if I pick an expensive one though! ;-)") \
                        .add_valid_entity_response('min', setQueryParams) \
                        .add_valid_entity_response('max', setQueryParams)

have_a_pairing_quest = Question(foodPairings['question']) \
                        .set_yes_response(False, text = "I know about the following types of food: %s, or none.\nLet me know which one is the closest match for your meal."%(', '.join(foodPairings['categories'].keys()))) \
                        .set_no_response(True, text = "No problem, I'll pick a wine that stands well on its own.") \
                        .add_valid_entity_response('type', pairingProgression) \
                        .add_valid_entity_response('main_ingredient', pairingProgression) \
                        .add_invalid_entity_response("If you are planning to have a meal with the wine, let me know which of these categories it is closest to: %s.  If you aren't having a meal, just let me know." % (', '.join(foodPairings['categories'].keys())))

def prompt_for_info(state):
    missing = state.queryFrame.getUnfilledSlotPrompts()
    prompt = ""
    if len(missing) > 0 and not state.useBaseline:
        for m in missing:
            if m == 'type' and what_color_quest not in state.operationsStack and "varietal" not in state.queryFrame.getFilledSlots():
                state.operationsStack.append(what_color_quest)
                return what_color_quest.question_text
            if (m == "min_price" or m == "max_price") and price_range_quest not in state.operationsStack:
                state.operationsStack.append(price_range_quest)
                return price_range_quest.question_text
            if m == 'pairing' and have_a_pairing_quest not in state.operationsStack:
                state.operationsStack.append(have_a_pairing_quest)
                return have_a_pairing_quest.question_text

    # # Everything from this point on is just for a baseline.  As long as the request is not empty, execute the query and give back the first wine
    # if self.queryFrame.isEmpty():
    #     print "I didn't get any query information from that statement."
    # else:
    #     self.currentState()

    # if prompt != "":
    #     return "I need some more information.\n" + prompt + "\n"

    # self.executeQuery()
    # # save old queryFrame to list
    # self.previousQueries.append(self.queryFrame)
    # self.clearQueryFrame()
    # # clear operation stack
    # self.operationsStack = []

def setWineListIndex(entities, state, manualIndex = None):
    if manualIndex is not None:
        state.wineListIndex = manualIndex
    else:
        pass

    if state.wineListIndex >= len(state.wineList):
        return 'Unfortunately, that is more than the number of wines I found for you!'

    response = "Here is the information about the chosen wine:\n%s\n\nI hope you enjoy the recommendation!" % (str(state.wineList[state.wineListIndex]))
    return response

def performSearch(entities, state):
    state.wineList = executeWineQuery(state.queryFrame, verbose = state.verbose)
    if state.wineList is None:
        return "no winelist"
    elif len(state.wineList) == 0:
        return "I'm sorry, but I could not find a good wine which matches your description.  Let me know what you want to change about your query.\n"
    return setWineListIndex(entities, state, manualIndex = 0)

def askIfShouldSearch(state):
    shouldSearchQuestion = Question("Have you told me everything that you're looking for?") \
                        .set_yes_response(True, func = performSearch) \
                        .set_no_response(True, func = setQueryParams) \
                        .add_default_response(setQueryParams)
    state.operationsStack.append(shouldSearchQuestion)
    return shouldSearchQuestion.question_text

def shouldAskAnotherQuestion(state):
    return len(state.operationsStack) == 0 or not isinstance(state.operationsStack[-1], Question) or state.operationsStack[-1].answered

'''
This is the function that serves as the main interface between the state and the outside world.
It should be passed in the entities dictionary detected by Wit.
Based on the intent that Wit detects, it will call one of various other functions.
It returns a string that should be printed as Vitibot's part of the dialog.
'''
def respondToDialog(parsedInput, state):
    if state.verbose:
        print parsedInput
        print state.operationsStack

    response = ''

    # first, check if the operations stack is non-empty
    if not state.useBaseline and len(state.operationsStack) > 0:
        lastOp = state.operationsStack[-1]
        if isinstance(lastOp, Question) and not lastOp.answered:
            quest_response = handleQuestion(lastOp, parsedInput, state)
            if quest_response is not None:
                response += quest_response

    # Now, check to see if we got a classified intent.
    if not response:
        intent = first_entity_value(parsedInput, 'intent')
        if intent in actions:
            response += actions[intent](parsedInput, state)

    if shouldAskAnotherQuestion(state):
        prompt = prompt_for_info(state)
        if prompt is not None:
            return response + prompt

    if shouldAskAnotherQuestion(state):
        if state.wineList is None or len(state.wineList) == 0:
            return response + askIfShouldSearch(state)

    if response:
        return response

    if intent is not None:
        return "I'm sorry, but I don't know how to do that: " + intent

    return "I'm sorry, but I could not understand your request."