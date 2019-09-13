import logging as puts
import os
import random
import re
import urllib

import requests
from discord.ext import commands
from exception.exceptions import FutebotException
from service import roll_service
from service.img_card_service import generate_card
from util.helpers import (
    generate_image_search_url,
    RANDOM_EXCEPTION_COMEBACKS as rec,
    get_json_fields_from_url,
    get_json_field_from_url,
    mention,
)

bot = commands.Bot(command_prefix=".")
puts.basicConfig(format="%(asctime)s - %(message)s", level=puts.INFO)


@bot.command()
async def ping(ctx, arg=""):
    if arg == "":
        await ctx.send("pong")
    else:
        await ctx.send("Pinging " + mention(ctx, arg) + " 🏓")


@bot.command()
async def charada(ctx):
    fields = get_json_fields_from_url(
        "https://us-central1-kivson.cloudfunctions.net/charada-aleatoria",
        "pergunta",
        "resposta",
    )
    for field in fields:
        await ctx.send(field)


@bot.command()
async def listall(ctx):
    await ctx.send("```--- Commands List --- \n"
                   ".coach                     - Returns a random motivational quote\n"
                   ".gifme     {search_term}   - Search for a Gif\n"
                   ".horoscopo {horoscopo}     - Search for you daily horoscope\""
                   ".ping      {optional_name} - Check if bot is Alive with optional mention\""
                   ".youtube   {search_term}   - Search for a Youtube Video\n"
                   ".imgme     {search_term}   - Search for an image in Google\n"
                   ".soniko    {caption}       - Create a Soniko meme\n"
                   ".speech     {caption}       - Speech Meme\n"
                   "```")


@bot.command()
async def coach(ctx):
    await ctx.send(
        get_json_field_from_url(
            "http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en",
            "quoteText",
        )
    )


@bot.command()
async def roll(ctx, arg):
    try:
        response = roll_service.roll(arg)
        await ctx.send(response)
    except Exception as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@bot.command()
async def imgme(ctx, *search_query):
    try:
        url = generate_image_search_url(search_query)
        res = requests.get(url)
        image_link = res.json()["items"][0]["link"]
        await ctx.send(image_link)

    except Exception as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@bot.command()
async def gifme(ctx, *search_query):
    try:
        url = generate_image_search_url(search_query, gif=True)
        res = requests.get(url)
        image_link = res.json()["items"][0]["link"]
        await ctx.send(image_link)

    except Exception as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@bot.command()
async def youtube(ctx, *args):
    try:
        query_string = urllib.parse.urlencode({"search_query": " ".join(args)})
        html_content = urllib.request.urlopen(
            "http://www.youtube.com/results?" + query_string
        )
        search_results = re.findall(
            r"href=\"\/watch\?v=(.{11})", html_content.read().decode()
        )
        await ctx.send("http://www.youtube.com/watch?v=" + search_results[0])
    except BaseException:
        await ctx.send("Are you dumb?")


@bot.command()
async def horoscopo(ctx, arg):
    await ctx.send(
        get_json_field_from_url(
            "http://babi.hefesto.io/signo/{}/dia".format(arg), "texto"
        )
    )


@bot.command()
async def soniko(ctx, *args):
    try:
        string = ' '.join(args)
        await ctx.send(file=generate_card(string, "templates/imgs/soniko.png", "soniko", 25, 83, 274, (0, 0, 0), 23))

    except FutebotException as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])

@bot.command()
async def speech(ctx, *args):
    try:
        string = " ".join(args)
        if not string.isdigit():
            await ctx.send(rec[random.randrange(0, len(rec) - 1)])
            return

        await ctx.send(file=generate_card(string, "templates/imgs/speech.png", "speech",
                                          110, 670, 10, (255,255,255), 4))

    except FutebotException as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


bot.run(os.environ["DISCORD_APP_TOKEN"])
