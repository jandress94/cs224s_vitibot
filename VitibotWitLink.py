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
    def getParsedInput(self, inputMethod = 'typed', fd=None, mstr=""):
        assert inputMethod == 'typed' or inputMethod == 'spoken' or inputMethod == 'file' or inputMethod == 'str'

        while True:
            if inputMethod == 'typed':
                message = prompt('> ', mouse_support=True).rstrip()
                jsonResponse = self.witClient.message(message)
            elif inputMethod == 'str':
                jsonResponse = self.witClient.message(mstr)
            elif inputMethod == 'file':
                jsonResponse = self.witClient.speech(fd, headers = {'Content-Type': 'audio/wav'})
                if self.verbose:
                    print jsonResponse
            else:
                # Wait until user hits enter before beginning the recording.
                entered = prompt('Hit enter when you are ready to speak.')
                jsonResponse = self.witClient.speech(getAudioInput(), headers = {'Content-Type': 'audio/raw;encoding=signed-integer;bits=16;rate=88200;endian=little'})
                if self.verbose:
                    print jsonResponse

            entities = getEntitiesFromResponse(jsonResponse)
            if entities is not None:
                return entities

            print("I couldn't understand that, sorry.")
