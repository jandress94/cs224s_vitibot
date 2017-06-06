import sys
from VitibotWitLink import *
from VitibotState import *

print " __      ___ _   _ ____        _   "
print " \ \    / (_) | (_)  _ \      | |  "
print "  \ \  / / _| |_ _| |_) | ___ | |_ "
print "   \ \/ / | | __| |  _ < / _ \| __|"
print "    \  /  | | |_| | |_) | (_) | |_ "
print "     \/   |_|\__|_|____/ \___/ \__|"
print ""

flags = set(sys.argv[1:])
if '-h' in flags or '--help' in flags:
    print("-t: typed input to vitibot rather than spoken")
    print("-v: verbose")
    print("-b: use baseline implementation")
    sys.exit(0)

verbose = '-v' in flags

inputMethod = 'typed' if '-t' in flags else 'spoken'
useBaseline = '-b' in flags

vitibotState = VitibotState(verbose = verbose, useBaseline = useBaseline)
witLink = VitibotWitLink(verbose = verbose)

print "Hello there!  I am your personal wine expert.  Let me know if there is anything I can search for you.\n"

while True:
    parsedInput = witLink.getParsedInput(inputMethod = inputMethod)
    vitibotResponse = vitibotState.respondToDialog(parsedInput)
    print(vitibotResponse)