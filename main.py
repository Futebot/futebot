import logging as puts
import os
import random

import requests
from discord.ext import commands

from helpers import generate_image_search_url, RANDOM_EXCEPTION_COMEBACKS as rec

bot = commands.Bot(command_prefix='>')
puts.basicConfig(format='%(asctime)s - %(message)s', level=puts.INFO)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def roll(ctx, arg):
    try:
        rolled = random.randrange(1, int(arg))
        await ctx.send('Rolled ' + str(rolled))
    except Exception as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@bot.command()
async def imageme(ctx, *search_query):
    try:
        url = generate_image_search_url(search_query)
        res = requests.get(url)
        image_link = res.json()['items'][0]['link']
        await ctx.send(image_link)

    except Exception as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@bot.command()
async def gifme(ctx, *search_query):
    try:
        url = generate_image_search_url(search_query, gif=True)
        res = requests.get(url)
        image_link = res.json()['items'][0]['link']
        await ctx.send(image_link)

    except Exception as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


bot.run(os.environ['DISCORD_APP_TOKEN'])
