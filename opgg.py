import requests
from bs4 import BeautifulSoup
from info import Summoner
from champion import Champion

def getSummonerInfo(name: str) -> Summoner:
    # name = input("소환사명을 입력하세요: ")
    summoner = Summoner(name) # create a new Summoner instatnce
    url='https://www.op.gg/summoner/userName=' + name
    header = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': ('Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
    req = requests.get(url, header)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser') # crawling

    # exception: If user dosen't exist
    if len(soup.select('div.l-container > div.SummonerNotFoundLayout')) > 0:
        return None

    # get summoner's info frop the object "soup", and then set summoner's property
    summoner.level = getSummonerLevel(soup)
    summoner.soloRankInfo = getSummonerSoloRank(soup)
    summoner.subRankInfo = getSummonerSubRank(soup)
    summoner.mostChampions = getSummonerMost(soup)
    summoner.recentGames = getRecent(soup)
    summoner.medal = getMedal(soup)

    return summoner

def getSummonerLevel(soup) -> str:
    return soup.select("span.Level")[0].text.strip()

def getSummonerSoloRank(soup) -> dict:
    # make a dictionary of solorank info
    info = {}
    if soup.select("div.TierRankInfo > div.unranked"):
        info["Tier"] = "Unranked"
        return info
    info['Tier'] = soup.select('div.TierRank')[0].text.strip()
    info['LP'] = f'{soup.select("div.TierInfo > span.LeaguePoints")[0].text.split("L")[0].strip()}LP'
    info['WinLose'] = f'{soup.select("span.wins")[0].text.strip()} {soup.select("span.losses")[0].text.strip()}'
    info['WinRate'] = soup.select("span.winratio")[0].text.strip().split(" ")[2]
    return info

def getSummonerSubRank(soup) -> dict:
    # make a dictionary of flexrank info
    info = {}
    # if the summoner is unranked, set status "Unranked"
    if soup.select("div.sub-tier > div.unranked"):
        info["Tier"] = "Unranked"
        info["LP"] = "Unranked"
        info["WinLose"] = "Unranked"
        info["WinRate"] = "Unranked"
        return info
    info['Tier'] = soup.select('div.sub-tier__rank-tier')[0].text.strip()
    info['LP'] = f'{soup.select("div.sub-tier__league-point")[0].text.strip().split("/")[0]}'
    info['WinLose'] = soup.select('div.sub-tier__league-point > span.sub-tier__gray-text')[0].text.split('/')[1].strip()
    info['WinRate'] = soup.select('div.sub-tier__gray-text')[0].text.strip().split(" ")[2]
    return info

def getSummonerMost(soup) -> list:
    # make a list of champions
    champions = []
    for idx, value in enumerate(soup.select('div.MostChampionContent > div.ChampionBox > div.ChampionInfo > div.ChampionName > a')):
        champ = Champion()
        champ.name = value.text.strip()
        champ.KDA = soup.select('div.MostChampionContent > div.ChampionBox > div.PersonalKDA > div.KDA > span.KDA')[idx].text.strip()
        champ.WinRate = soup.select('div.MostChampionContent > div.ChampionBox > div.Played > div.WinRatio')[idx].text.strip()
        champ.playedNum = soup.select('div.MostChampionContent > div.ChampionBox > div.Played > div.Title')[idx].text.split(' ')[0].strip() + 'G'
        champions.append(champ)
        # return most 3 champions
        if len(champions) == 3:
            return champions
    return champions

def getRecent(soup) -> str:
    # get summoner's recent games win, lose, kda
    total = soup.select('div.WinRatioTitle > span.total')[0].text.strip()
    win = soup.select('div.WinRatioTitle > span.win')[0].text.strip()
    lose = soup.select('div.WinRatioTitle > span.lose')[0].text.strip()
    KDA = soup.select('div.KDARatio > span.KDARatio')[0].text.strip()
    return f'{total}전 {win}승 {lose}패 {KDA}'

def getMedal(soup) -> str:
    # get a tier medal
    soloMedal = soup.select('div.Medal > img')[0].get('src')
    # return url of the medal
    return soloMedal