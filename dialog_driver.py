from questions import *
from WitUtils import *
from FoodPairings import *
from VitibotWineDotComLink import *
import sys

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
        
    elif 'main_ingredient' in entities and len(current_pairing_state) < 2:  # They gave an ingredient
        pairing_ing = first_entity_value(entities, 'main_ingredient')
        if len(current_pairing_state) == 0:                                 # They haven't already given a pairing type yet
            for pairing_type in foodPairings['categories']:
                pair_type_dict = foodPairings['categories'][pairing_type]
                if pairing_ing in pair_type_dict['categories']:
                    current_pairing_state.append(pairing_type)
                    break

        pairing_type = current_pairing_state[0]
        if pairing_ing not in foodPairings['categories'][pairing_type]['categories']:
            pair_type_dict = foodPairings['categories'][pairing_type]
            pairing_question = Question("That's not a valid ingredient. Main ingredient for %s include: %s, or none.\nLet me know which one is the closest match for your meal, or you can start a new search as well."%(pairing_type,', '.join(pair_type_dict['categories'].keys()))) \
                                    .add_valid_entity_response('main_ingredient', pairingProgression) \
                                    .set_no_response(True, text = "That's ok, but I won't be able to make much use of a generic pairing like \"%s\"." % (pairing_type)) \
                                    .add_invalid_entity_response("That's not a valid ingredient. Main ingredient for %s include: %s, or none.\nLet me know which one is the closest match for your meal."%(pairing_type,', '.join(pair_type_dict['categories'].keys())))
            
        else:
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

            else:
                # No style to choose, so proceed.
                final_response = "Sounds delicious!  I will definitely take these foods into consideration!"
                if 'blurb' in pair_ing_dict:
                    final_response += " %s\n" % (pair_ing_dict['blurb'])
                else:
                    final_response += "\n"
                state.queryFrame.setSlotValue('pairing', current_pairing_state)
                return final_response
    elif len(current_pairing_state) == 2 and 'style' in entities:   # They gave a specific style
        pairing_style = first_entity_value(entities, 'style')
        current_pairing_state.append(pairing_style)
        final_response = "Sounds delicious!  I will definitely take these foods into consideration!"

        pair_style_dict = foodPairings['categories'][current_pairing_state[0]]['categories'][current_pairing_state[1]]['categories'][pairing_style]
        if 'blurb' in pair_style_dict:
            final_response += " %s\n" % (pair_style_dict['blurb'])
        else:
            final_response += "\n"
        state.queryFrame.setSlotValue('pairing', current_pairing_state)
        return final_response

    state.queryFrame.setSlotValue('pairing', current_pairing_state)

    if state.useBaseline:
        return ''

    if pairing_question is not None:
        state.operationsStack.append(pairing_question)
        return pairing_question.question_text
    else:
        return "I'm sorry, it looks like you already told me about what pairing you wanted.  You'll have to start a new search if you want to change the pairing.\n"


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

    if 'wineLoc' in params:
        ack = ack + " from " + params['wineLoc'].getValue()

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

    wineLoc = first_entity_value(entities, 'wineLoc')
    if wineLoc is not None:
        state.queryFrame.setSlotValue('wineLoc', wineLoc)
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


def resetQuery(entities, state):
    state.reset()
    return 'What can I help you find?\n'


def immediately_kill(entities = None, state = None):
    print("Goodbye!")
    sys.exit(0)


def askBeforeExiting(entities, state):
    exit_quest = Question('Are you sure that you want to exit?') \
                        .set_yes_response(True, func = immediately_kill) \
                        .set_no_response(True, text = "Thank goodness, I didn't want you to leave!")
    state.operationsStack.append(exit_quest)
    return exit_quest.question_text


def setWineListIndex(entities, state, manualIndex = None):
    if state.wineList is None or len(state.wineList) == 0:
        return 'You cannot choose a wine to view until you have run a search!\n'

    if manualIndex is not None:
        state.wineListIndex = manualIndex
    else:
        desired_index = first_entity_value(entities, 'wineIndex')
        if desired_index is None:
            return 'Tell which number wine you are trying to view.'
        else:
            state.wineListIndex = desired_index - 1

    response = ''

    if state.wineListIndex >= len(state.wineList) or state.wineListIndex < 0:
        state.wineListIndex = 0
        response += 'Unfortunately, that is more than the number of wines I found for you!\n\n'

    response += "Here is the information about the chosen wine:\n\n%s\n\nI hope you enjoy the recommendation!\n" % (str(state.wineList[state.wineListIndex]))
    if len(state.wineList) > 1:
        response += "This is wine number %d out of %d.  Let me know if you want to see any of the other wines or if you want to start a new search." % (state.wineListIndex+1, len(state.wineList))
    else:
        response += "Let me know if you want to start a new search."
    return response


actions = {
    'setQuery': setQueryParams,
    'resetQuery': resetQuery,
    'exit': askBeforeExiting,
    'setWineIndex': setWineListIndex
}

# Ignores what's on the operations stack, which can mess up queries if unintended.
override_actions = [
    'resetQuery',
    'exit'
]


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
            if ((m == "min_price" and "max_price" in missing) or (m == "max_price" and "min_price" in missing))and price_range_quest not in state.operationsStack:
                state.operationsStack.append(price_range_quest)
                return price_range_quest.question_text
            if m == 'pairing' and have_a_pairing_quest not in state.operationsStack:
                state.operationsStack.append(have_a_pairing_quest)
                return have_a_pairing_quest.question_text


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
    return state.numTurns > 0 and (len(state.operationsStack) == 0 or not isinstance(state.operationsStack[-1], Question) or state.operationsStack[-1].answered)


'''
This is the function that serves as the main interface between the state and the outside world.
It should be passed in the entities dictionary detected by Wit.
Based on the intent that Wit detects, it will call one of various other functions.
It returns a string that should be printed as Vitibot's part of the dialog.
'''
def respondToDialog(parsedInput, state):
    state.numTurns += 1

    if state.verbose:
        print parsedInput
        print state.operationsStack
    
    response = ''

    # Check if we got an override action.
    actionPerformed = False
    intent = first_entity_value(parsedInput, 'intent')
    if intent in override_actions:
        response += actions[intent](parsedInput, state)
        actionPerformed = True

    # first, check if the operations stack is non-empty
    if len(state.operationsStack) > 0:
        lastOp = state.operationsStack[-1]
        if isinstance(lastOp, Question) and not lastOp.answered:
            quest_response = handleQuestion(lastOp, parsedInput, state)
            if quest_response is not None:
                response += quest_response

    # Now, check to see if we got a classified intent.
    if not response and not actionPerformed:
        intent = first_entity_value(parsedInput, 'intent')
        if intent in actions:
            response += actions[intent](parsedInput, state)

    if state.useBaseline and state.numTurns > 0 and state.wineList is None:
        return response + performSearch(parsedInput, state)

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
        if state.verbose:
            return "I'm sorry, but I don't know how to do that: " + intent
        return "I'm sorry, but I don't know how to do what you are asking."

    return "I'm sorry, but I could not understand your request."