import requests
from bs4 import BeautifulSoup
from info import Summoner

def getSummonerInfo(name):
    # name = input("소환사명을 입력하세요: ")
    summoner = Summoner(name) # create a new Summoner instatnce
    url='https://www.op.gg/summoner/userName=' + name
    header = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': ('Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
    req = requests.get(url, header)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser') # crawling

    # exception: If user dosen't exist
    if len(soup.select('div.l-container > div.SummonerNotFoundLayout')) > 0:
        # print("존재하지 않는 유저입니다.")
        return None

    summoner.soloRankInfo = getSummonerSoloRank(soup)
    summoner.subRankInfo = getSummonerSubRank(soup)
    summoner.mostChampions = getSummonerMost(soup)

    return summoner
    # summoner.printInfo()

def getSummonerSoloRank(soup):
    # make dictionary with solo rank info
    info = {}
    if soup.select("div.TierRankInfo > div.unranked"):
        info["Tier"] = "Unranked"
        info["LP"] = "Unranked"
        info["WinLose"] = "Unranked"
        info["WinRate"] = "Unranked"
        return info
    info['Tier'] = soup.select('div.TierRank')[0].text.strip()
    info['LP'] = f'{soup.select("div.TierInfo > span.LeaguePoints")[0].text.split("L")[0].strip()}LP'
    info['WinLose'] = f'{soup.select("span.wins")[0].text.strip()} {soup.select("span.losses")[0].text.strip()}'
    info['WinRate'] = soup.select("span.winratio")[0].text.strip().split(" ")[2]
    return info

def getSummonerSubRank(soup):
    info = {}
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

def getSummonerMost(soup):
    champions = []
    for i in soup.select('div.MostChampionContent > div.ChampionBox > div.ChampionInfo > div.ChampionName > a'):
        champions.append(i.text.strip())
    return champions