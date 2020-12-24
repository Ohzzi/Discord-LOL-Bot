import discord
import json
from discord.ext import commands

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

bot.run(token)