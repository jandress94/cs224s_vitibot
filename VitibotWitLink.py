from __future__ import unicode_literals
import sys
from wit import Wit
from prompt_toolkit import prompt
from constants import *
from WitUtils import *
from AudioInput import *

class VitibotWitLink:
    def __init__(self, verbose = False):
        self.witClient = Wit(access_token=wit_access_token)
        self.verbose = verbose

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
                jsonResponse = self.witClient.speech(getAudioInput(), headers = {'Content-Type': 'audio/raw;encoding=signed-integer;bits=16;rate=88200;endian=little'})
                if verbose:
                    print jsonResponse

            entities = getEntitiesFromResponse(jsonResponse)
            if entities is not None:
                return entities

            print("I couldn't understand that, sorry.")
