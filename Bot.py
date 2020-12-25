import discord
import json
from discord.ext import commands
from opgg import getSummonerInfo

with open('token.json') as jsonFile:
    jsonData = json.load(jsonFile)
    token = jsonData["token"]

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Test bot'))
    print("Bot status::online")

@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(round(bot.latency, 4)*1000)}ms')

@bot.command(name="검색")
async def getInfo(ctx, args):
    summoner = getSummonerInfo(args)
    if not summoner:
        await ctx.send("유저 정보 없음")
        return
    # summoner.printInfo()
    await ctx.send(embed = createEmbed(summoner))

def createEmbed(summoner):
    embed = discord.Embed(title = f'{summoner.name}', color = 0xEEEEEE)
    if summoner.soloRankInfo["Tier"] == "Unranked":
        embed.add_field(name = "솔로 랭크", value = "Unranked", inline=True)
    else:
        embed.add_field(name = "솔로 랭크", value = f'{summoner.soloRankInfo["Tier"]} {summoner.soloRankInfo["LP"]}\
        \n{summoner.soloRankInfo["WinLose"]} {summoner.soloRankInfo["WinRate"]}', inline=True)
    if summoner.subRankInfo["Tier"] == "Unranked":
        embed.add_field(name = "자유 랭크", value = "Unranked", inline=True)
    else:
        embed.add_field(name = "자유 랭크", value = f'{summoner.subRankInfo["Tier"]} {summoner.subRankInfo["LP"]}\
        \n{summoner.subRankInfo["WinLose"]} {summoner.subRankInfo["WinRate"]}', inline=True)
    if len(summoner.mostChampions) != 0:
        embed.add_field(name = "모스트 챔피언", value = f'{summoner.mostChampions}', inline=False)
    return embed

bot.run(token)