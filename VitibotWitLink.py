from __future__ import unicode_literals
import sys
from wit import Wit
from prompt_toolkit import prompt
from constants import *
from WitUtils import *

class VitibotWitLink:
    def __init__(self):
        self.witClient = Wit(access_token=wit_access_token)

    '''
    The input method can be either 'typed' or 'spoken'
    '''
    def getParsedInput(self, inputMethod = 'typed'):
        assert inputMethod == 'typed' or inputMethod == 'spoken'

        while True:
            if inputMethod == 'typed':
                message = prompt('> ', mouse_support=True).rstrip()
                jsonResponse = self.witClient.message(message)
            else:
                # f = open(sys.argv[1])
                # json_result = self.witClient.speech(f, None, {'Content-Type': 'audio/wav'})
                # f.close()
                sys.exit('Spoken input not yet implemented')

            entities = getEntitiesFromResponse(jsonResponse)
            if entities is not None:
                return entities

            print("I couldn't understand that, sorry.")
