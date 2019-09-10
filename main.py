import json
import urllib
import os
import re
import random

import discord
from discord import Client
from discord import client
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def roll(ctx, arg):
    try:
        rolled = random.randrange(1, int(arg))
        await ctx.send('Rolled ' + str(rolled))
    except:
        await ctx.send('Are you dumb?')


@bot.command()
async def youtube(ctx, *args):
    try:
        query_string = urllib.parse.urlencode({"search_query": " ".join(args)})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        await ctx.send("http://www.youtube.com/watch?v=" + search_results[0])
    except:
        await ctx.send('Are you dumb?')


@bot.command()
async def horoscopo(ctx, arg):
    try:
        r = requests.get(url="http://babi.hefesto.io/signo/{}/dia".format(arg))
        await ctx.send(r.json()['texto'])
    except:
        await ctx.send('Are you dumb?')


bot.run(os.environ['DISCORD_APP_TOKEN'])
