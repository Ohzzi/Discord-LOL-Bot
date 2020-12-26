class Champion(object):
    def __init__(self):
        pass

    @property
    def name(self):
        return self._name
    
    @property
    def KDA(self):
        return self._KDA

    @property
    def playedNum(self):
        return self._playedNum
    
    @property
    def WinRate(self):
        return self._WinRate

    @name.setter
    def name(self, name):
        self._name = name

    # Death / Kill + Assist
    @KDA.setter
    def KDA(self, KDA):
        self._KDA = KDA
    
    # The number of played games
    @playedNum.setter
    def playedNum(self, played):
        self._playedNum = played
    
    # Win rate
    @WinRate.setter
    def WinRate(self, WinRate):
        self._WinRate = WinRate
