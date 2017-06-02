'''
A class representing each of the slots that must be filled when
the user is trying to query for a wine
'''

class QuerySlot:
    '''
    Constructs a new QuerySlot

    params:
        - name: the name of the slot
        - promptIfAbsent: if True, then before submitting the query 
                          vitibot will ask the user whether they want 
                          to fill this slot f they haven't done so already
    '''
    def __init__(self, name, promptIfAbsent = False):
        self.name = name
        self.promptIfAbsent = promptIfAbsent
        self.value = None

    '''
    only prompt the user if this slot should prompt and
    this slot hasn't already been filled
    '''
    def shouldPromptUser(self):
        return self.promptIfAbsent and self.value is None

    def getValue(self):
        return self.value