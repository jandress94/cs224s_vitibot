from WitUtils import *
from VitibotWitLink import *

answers = [{'intent': 'setQuery'}, {'color': 'red', 'intent': 'setQuery'}, {'intent': 'setQuery', 'color': 'white', 'min': 20, 'max': 50}, {'type': 'seafood'}, {'type': 'meat', 'style': 'meat'}, {'intent': 'setQuery', 'color': 'rose'}, {'intent': 'setQuery', 'max': 400}, {'intent': 'setQuery', 'min': 300}, {'intent': 'setQuery', 'min': 40, 'max': 60}, {}, {'binary': 'no', 'main_ingredient': 'goat'}, {'main_ingredient': 'chocolate'}, {'style': 'pesto'}, {'intent': 'setQuery', 'color': 'rose'}, {'max': 100}, {'color': 'red'}, {'binary': 'no'}, {'binary': 'no'}, {'binary': 'yes', 'style': 'herbs'}, {'style': 'butter'}, {'main_ingredient': 'white fish', 'color': 'white'}, {'intent': 'setQuery', 'main_ingredient': 'white fish', 'color': 'white'}, {}, {'intent': 'setQuery', 'main_ingredient': 'veal'}, {'main_ingredient': 'chicken', 'main_ingredient': 'duck'}, {'style': 'roasted'}, {'type': 'dessert'}, {'intent': 'setQuery', 'min': 40, 'max': 70}, {'main_ingredient': 'duck'}, {'type': 'cheese', 'main_ingredient': 'stinky'}, {'intent': 'setQuery', 'varietal': 'pinot noir'}, {}, {'main_ingredient': 'chocolate'}, {'style': 'burgers'}, {'main_ingredient': 'stinky'}, {'intent': 'setQuery', 'color': 'red'}, {'main_ingredient': 'pizza', 'style': 'meat'}, {'main_ingredient': 'shrimp'}, {'color': 'rose'}, {'intent': 'setQuery', 'vintage': 2013}, {'intent': 'setQuery', 'color': 'white', 'vintage': '2014', 'max': 60}, {'binary': 'no'}, {}, {}, {'vintage': 2005}, {'intent': 'setQuery', 'vintage': 2007, 'max': 50, 'color': 'white'}, {'style': 'fish tacos'}, {'intent': 'setQuery', 'min': 400}, {'intent': 'setQuery'}, {}, {'main_ingredient': 'chicken'}, {'intent': 'setQuery', 'color': 'white', 'varietal': 'pinot gris'}, {'binary': 'no'}, {'binary': 'no'}, {'main_ingredient': 'chicken'}, {'intent': 'setQuery'}, {'intent': 'setQuery', 'vintage': 1979}, {'intent': 'setQuery', 'max': 27}]

correct = 0
totEnt = 0
corEnt = 0

def checkEntities(i, entities):
	global totEnt
	global corEnt
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
				c = False
			else:
				v += 1
				corEnt += 1
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
	fd = open("test/test"+str(i)+".wav", "rb")
	# send each file to wit via vitibot witlink (unstreamed)
	parsedInput = witLink.getParsedInput(inputMethod = "file", fd=fd)
	# verify returned json returned from getParsedInput(), first_entity_value(entities, 'name') if entities not None
	b = checkEntities(i, parsedInput)
	if b:
		correct += 1
print "========================="
print "Utterace Acc.: %d/%d (%f accurate)"%(correct, len(answers), float(correct)/len(answers))
print "Entity Acc. %d/%d (%f)"%(corEnt, totEnt, float(corEnt)/totEnt)