from QueryFrame import *
from Wine import *

class VitibotState:
    def __init__(self, verbose = False, useBaseline = False):
        self.reset()
        self.verbose = verbose
        self.useBaseline = useBaseline

    def reset(self):
        self.queryFrame = QueryFrame()
        self.wineList = None
        self.wineListIndex = None
        self.operationsStack = []
        self.previousQueries = []
        self.numTurns = 0

    def clearQueryFrame(self, entities = None):
        self.queryFrame = QueryFrame()

    def executeQuery(self, entities = None):
        self.wineList = executeWineQuery(self.queryFrame, verbose = self.verbose)