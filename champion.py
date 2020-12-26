class Champion(object):
    def __init__(self):
        pass

    @property
    def name(self):
        return self.__name
    
    @property
    def KDA(self):
        return self.__KDA

    @property
    def playedNum(self):
        return self.__playedNum
    
    @property
    def WinRate(self):
        return self.__WinRate

    @name.setter
    def name(self, name):
        self.__name = name

    # Death / Kill + Assist
    @KDA.setter
    def KDA(self, KDA):
        self.__KDA = KDA
    
    # The number of played games
    @playedNum.setter
    def playedNum(self, played):
        self.__playedNum = played
    
    # Win rate
    @WinRate.setter
    def WinRate(self, WinRate):
        self.__WinRate = WinRate
