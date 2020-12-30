class Summoner(object):
    def __init__(self, summonerName: str):
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
    def name(self, name: str):
        self.__name = name
    
    @level.setter
    def level(self, level: str):
        self.__level = level

    # soloRankInfo and subRankInfo: a dictionary of keys ["Tier", "LP", "WinLose", "WinRate"]
    @soloRankInfo.setter
    def soloRankInfo(self, info: dict):
        self.__soloRankInfo = info

    @subRankInfo.setter
    def subRankInfo(self, info: dict):
        self.__subRankInfo = info

    # mostChampions: a list of class "Champion"
    @mostChampions.setter
    def mostChampions(self, champs: list):
        self.__mostChampions = champs

    # recentGames: player's recent game win / lose
    @recentGames.setter
    def recentGames(self, recent: str):
        self.__recentGames = recent
    
    @medal.setter
    def medal(self, medal: str):
        self.__medal = medal