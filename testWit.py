from WitUtils import *
from VitibotWitLink import *

answers = [{'intent': 'setQuery'}, {'color': 'red', 'intent': 'setQuery'}, {'intent': 'setQuery', 'color': 'white', 'min': 20, 'max': 50}, {'type': 'seafood'}, {'type': 'meat', 'style': 'meat'}, {'intent': 'setQuery', 'color': 'rose'}, {'intent': 'setQuery', 'max': 400}, {'intent': 'setQuery', 'min': 300}, {'intent': 'setQuery', 'min': 40, 'max': 60}, {}, {'binary': 'no', 'main_ingredient': 'goat'}, {'main_ingredient': 'chocolate'}, {'style': 'pesto'}, {'intent': 'setQuery', 'color': 'rose'}, {'max': 100}, {'color': 'red'}, {'binary': 'no'}, {'binary': 'no'}, {'binary': 'yes', 'style': 'herbs'}, {'style': 'butter'}, {'main_ingredient': 'white fish', 'color': 'white'}, {'intent': 'setQuery', 'main_ingredient': 'white fish', 'color': 'white'}, {}, {'intent': 'setQuery', 'main_ingredient': 'veal'}, {'main_ingredient': 'chicken', 'main_ingredient': 'duck'}, {'style': 'roasted'}, {'type': 'dessert'}, {'intent': 'setQuery', 'min': 40, 'max': 70}, {'main_ingredient': 'duck'}, {'type': 'cheese', 'main_ingredient': 'stinky'}, {'intent': 'setQuery', 'varietal': 'pinot noir'}, {}, {'main_ingredient': 'chocolate'}, {'style': 'burgers'}, {'main_ingredient': 'stinky'}, {'intent': 'setQuery', 'color': 'red'}, {'main_ingredient': 'pizza', 'style': 'meat'}, {'main_ingredient': 'shrimp'}, {'color': 'rose'}, {'intent': 'setQuery', 'vintage': 2013}, {'intent': 'setQuery', 'color': 'white', 'vintage': '2014', 'max': 60}, {'binary': 'no'}, {}, {}, {'vintage': 2005}, {'intent': 'setQuery', 'vintage': 2007, 'max': 50, 'color': 'white'}, {'style': 'fish tacos'}, {'intent': 'setQuery', 'min': 400}, {'intent': 'setQuery'}, {}, {'main_ingredient': 'chicken'}, {'intent': 'setQuery', 'color': 'white', 'varietal': 'pinot gris'}, {'binary': 'no'}, {'binary': 'no'}, {'main_ingredient': 'chicken'}, {'intent': 'setQuery'}, {'intent': 'setQuery', 'vintage': 1979}, {'intent': 'setQuery', 'max': 27}]
textInput = ["I'm looking for a wine.", "I like red wine.", "recommend me a white wine that costs between 20 dollars and 50 dollars", "i'll be eating seafood", "meat", "a blush sounds good", "i'm interested in a wine costing no more than 400 dollars.", "i want to spend at least 300 dollars", "something between 40 and 60 dollars", "moose", "none goat", "it has a lot of chocolate in it", "pesto", "i want a pink wine recommendation", "it shouldn't be above 100 dollars", "something red", "no", "i don't have a budget", "yes it has herbs", "butter", "white fish", "i want a white wine that pairs well with a white fish", "something cheap", "can you recommend me something that goes well with veal", "my friend ate chicken yesterday, but i'm having duck today", "it's roasted", "i want a dessert wine", "my budget is between 40 and 70 dollars", "i had duck yesterday", "stinky cheese", "i want a pinot noir wine", "i like cheesecake", "i'm in the mood for chocolate", "i will be having burgers", "you're stinky", "what about a full bodied red", "i'll be eating pizza with meat", "I'm a fan of shrimp.", "Maybe a rose.", "I want a wine from 2013.", "Recommend me a good white wine from 2014 costing under 60 dollars.", "Nope.", "Yeah, but cats are better.", "I don't know.", "2005.", "I want a 2007 white under 50 dollars.", "We're having fish tacos.", "I plan on spending at least 400 dollars.", "I'm desiring a dessert wine.", "What do you recommend?","I had burgers last week, but this time I'm eating chicken.", "I'm in the mood for a white wine, maybe a pinot gris.", "None of these.", "I'm indifferent.", "Either chicken or duck.", "We're having cow.", "Give me a wine from 1979.", "I'm spending at most 27 dollars."]

correct = 0
totEnt = 0
corEnt = 0
missingEnt = 0
wrongVal = 0

def checkEntities(i, entities):
	global totEnt
	global corEnt
	global missingEnt
	global wrongVal
	answer = answers[i]
	c = True
	e = 0 # num entities present
	v = 0 # num entity values correct
	t = len(answer.keys()) # total expected entities
	for k in answer:
		totEnt += 1
		val = answer[k]
		if k in entities:
			e += 1
			if val != first_entity_value(entities, k):
				wrongVal += 1
				c = False
			else:
				v += 1
				corEnt += 1
		else:
			missingEnt += 1
			c = False
	if c:
		print "Test %d correct."%(i)
	else:
		print "Test %d does not match. %d/%d entities present. %d/%d entity values correct."%(i,e,t,v,t)
		print answer
		print entities
	return c

# 20 spoken wav files
witLink = VitibotWitLink()

for i in xrange(0, 58):
	#fd = open("test/test"+str(i)+".wav", "rb")
	#parsedInput = witLink.getParsedInput(inputMethod = "file", fd=fd)
	parsedInput = witLink.getParsedInput(inputMethod = "str", mstr=textInput[i])
	# verify returned json returned from getParsedInput(), first_entity_value(entities, 'name') if entities not None
	b = checkEntities(i, parsedInput)
	if b:
		correct += 1
print "========================="
print "Utterance Acc. (All entities present + correct): %d/%d (%f accurate)"%(correct, len(answers), float(correct)/len(answers))
print "Entity (Present + Correct) Acc. %d/%d (%f)"%(corEnt, totEnt, float(corEnt)/totEnt)
print "Entity Error (Present + Incorrect): %d/%d (%f)"%(wrongVal, totEnt, float(wrongVal)/totEnt)
print "Missing Entities (Not Present): %d/%d (%f)"%(missingEnt, totEnt, float(missingEnt)/totEnt)