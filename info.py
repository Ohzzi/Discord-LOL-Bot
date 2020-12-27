class Summoner(object):
    def __init__(self, summonerName):
        self.__name = summonerName
    
    @property
    def name(self):
        return self.__name

    @property
    def level(self):
        return self.__level

    @property
    def soloRankInfo(self):
        return self.__soloRankInfo
    
    @property
    def subRankInfo(self):
        return self.__subRankInfo
    
    @property
    def mostChampions(self):
        return self.__mostChampions

    @property
    def recentGames(self):
        return self.__recentGames

    @property
    def medal(self):
        return self.__medal

    @name.setter
    def name(self, inputString):
        self.__name = inputString
    
    @level.setter
    def level(self, level):
        self.__level = level

    # soloRankInfo and subRankInfo: a dictionary of keys ["Tier", "LP", "WinLose", "WinRate"]
    @soloRankInfo.setter
    def soloRankInfo(self, info):
        self.__soloRankInfo = info

    @subRankInfo.setter
    def subRankInfo(self, info):
        self.__subRankInfo = info

    # mostChampions: a list of class "Champion"
    @mostChampions.setter
    def mostChampions(self, champs):
        self.__mostChampions = champs

    # recentGames: player's recent game win / lose
    @recentGames.setter
    def recentGames(self, recent):
        self.__recentGames = recent
    
    @medal.setter
    def medal(self, medal):
        self.__medal = medal

    # method for testing
    def printInfo(self):
        print(f'소환사명: {self.name}')
        print(f'솔로 랭크: {self.soloRankInfo["Tier"]} {self.soloRankInfo["LP"]} {self.soloRankInfo["WinLose"]} 승률 {self.soloRankInfo["WinRate"]}')
        print(f'자유 랭크: {self.subRankInfo["Tier"]} {self.subRankInfo["LP"]} {self.subRankInfo["WinLose"]} 승률 {self.subRankInfo["WinRate"]}')
        print('모스트 챔피언:', end=" ")
        for champ in self.mostChampions:
            print(champ.name, champ.playedNum, champ.KDA, champ.WinRate, end=" ")
        print('\n최근 전적:', self.recentGames)
        print(f'메달 주소: https:{self.medal}')