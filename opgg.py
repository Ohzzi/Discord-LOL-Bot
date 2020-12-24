import requests
from bs4 import BeautifulSoup

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

    @soloRankInfo.setter
    def soloRankInfo(self, info):
        self._soloRankInfo = info

    @subRankInfo.setter
    def subRankInfo(self, info):
        self._subRankInfo = info

    @mostChampions.setter
    def mostChampions(self, champs):
        self._mostChampions = champs

    def printInfo(self):
        print(f'소환사명: {self.name}')
        print(f'솔로 랭크: {self.soloRankInfo["Tier"]} {self.soloRankInfo["LP"]} {self.soloRankInfo["WinLose"]} 승률 {self.soloRankInfo["WinRate"]}')
        print(f'자유 랭크: {self.subRankInfo["Tier"]} {self.subRankInfo["LP"]} {self.subRankInfo["WinLose"]} 승률 {self.subRankInfo["WinRate"]}')
        print('모스트 챔피언:', end=" ")
        for champ in self.mostChampions:
            print(champ, end=" / ")

def getSummonerInfo():
    name = input("소환사명을 입력하세요: ")
    summoner = Summoner(name) # create a new Summoner instatnce
    url='https://www.op.gg/summoner/userName=' + name
    header = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': ('Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
    req = requests.get(url, header)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser') # crawling

    summoner.soloRankInfo = getSummonerSoloRank(soup)
    summoner.subRankInfo = getSummonerSubRank(soup)
    summoner.mostChampions = getSummonerMost(soup)

    summoner.printInfo()

def getSummonerSoloRank(soup):
    # make dictionary with solo rank info
    info = {}
    info['Tier'] = soup.select('div.TierRank')[0].text.strip()
    info['LP'] = f'{soup.select("div.TierInfo > span.LeaguePoints")[0].text.split("L")[0].strip()}LP'
    info['WinLose'] = f'{soup.select("span.wins")[0].text.strip()} {soup.select("span.losses")[0].text.strip()}'
    info['WinRate'] = soup.select("span.winratio")[0].text.strip().split(" ")[2]
    return info

def getSummonerSubRank(soup):
    info = {}
    info['Tier'] = soup.select('div.sub-tier__rank-tier')[0].text.strip()
    info['LP'] = f'{soup.select("div.sub-tier__league-point")[0].text.strip().split("/")[0]}LP'
    info['WinLose'] = soup.select('div.sub-tier__league-point > span.sub-tier__gray-text')[0].text.split('/')[1].strip()
    info['WinRate'] = soup.select('div.sub-tier__gray-text')[0].text.strip().split(" ")[2]
    return info

def getSummonerMost(soup):
    champions = []
    for i in soup.select('div.MostChampionContent > div.ChampionBox > div.ChampionInfo > div.ChampionName > a'):
        champions.append(i.text.strip())
    return champions

getSummonerInfo()