class Summoner(object):
    def __init__(self, summonerName):
        self._name = summonerName
    
    @property
    def name(self):
        return self._name

    @property
    def soloRankInfo(self):
        return self._soloRankInfo
    
    @property
    def subRankInfo(self):
        return self._subRankInfo
    
    @property
    def mostChampions(self):
        return self._mostChampions

    @name.setter
    def name(self, inputString):
        self._name = inputString

    # soloRankInfo and subRankInfo: a dictionary of keys ["Tier", "LP", "WinLose", "WinRate"]
    @soloRankInfo.setter
    def soloRankInfo(self, info):
        self._soloRankInfo = info

    @subRankInfo.setter
    def subRankInfo(self, info):
        self._subRankInfo = info

    # mostChampions: a list of class "Champion"
    @mostChampions.setter
    def mostChampions(self, champs):
        self._mostChampions = champs

    # method for testing
    def printInfo(self):
        print(f'소환사명: {self.name}')
        print(f'솔로 랭크: {self.soloRankInfo["Tier"]} {self.soloRankInfo["LP"]} {self.soloRankInfo["WinLose"]} 승률 {self.soloRankInfo["WinRate"]}')
        print(f'자유 랭크: {self.subRankInfo["Tier"]} {self.subRankInfo["LP"]} {self.subRankInfo["WinLose"]} 승률 {self.subRankInfo["WinRate"]}')
        print('모스트 챔피언:', end=" ")
        for champ in self.mostChampions:
            print(champ.name, champ.playedNum, champ.KDA, champ.WinRate, end=" ")