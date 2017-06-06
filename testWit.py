from WitUtils import *
from VitibotWitLink import *

answers = [{}, {}]

def checkEntities(i, entities):
	answer = answers[i]
	c = True
	e = 0 # num entities present
	v = 0 # num entity values correct
	t = len(answer.keys()) # total expected entities
	for k in answer:
		totEnt += 1
		v = answer[k]
		if k in entities:
			e += 1
			if v != first_entity_value(entities, k):
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
witLink = VitibotWitLink(verbose = verbose)

correct = 0
totEnt = 0
corEnt = 0
for i in xrange(0, 20):
	fd = open("test/test"+str(i)+".wav", "rb")
	# send each file to wit via vitibot witlink (unstreamed)
    parsedInput = witLink.getParsedInput(inputMethod = "file", fd)
	# verify returned json returned from getParsedInput(), first_entity_value(entities, 'name') if entities not None
	b = checkEntities(i, parsedInput)
	if b:
		correct += 1
print "========================="
print "Utterace Acc.: %d/%d (%f accurate)"%(correct, len(answers), float(correct/len(answers)))
print "Entity Acc. %d'%d (%f)"%(corEnt, totEnt, float(corEnt/totEnt))