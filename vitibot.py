from VitibotWitLink import *
from VitibotState import *

print " __      ___ _   _ ____        _   "
print " \ \    / (_) | (_)  _ \      | |  "
print "  \ \  / / _| |_ _| |_) | ___ | |_ "
print "   \ \/ / | | __| |  _ < / _ \| __|"
print "    \  /  | | |_| | |_) | (_) | |_ "
print "     \/   |_|\__|_|____/ \___/ \__|"
print ""

vitibotState = VitibotState()
witLink = VitibotWitLink()

while True:
    parsedInput = witLink.getParsedInput(inputMethod = 'spoken')
    vitibotResponse = vitibotState.respondToDialog(parsedInput)
    print(vitibotResponse)