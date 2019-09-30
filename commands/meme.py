import logging as puts
import random

import discord

from util.helpers import RANDOM_EXCEPTION_COMEBACKS as rec
import requests
from discord.ext import commands

from exception.exceptions import FutebotException, TooManyCharsException
from service.img_card_service import generate_card, generate_card_img, generate_card_img_title_description, \
    generate_card_twit, generate_card_multiple_texts
from util.helpers import generate_image_search_url


@commands.command()
async def soniko(ctx, *args):
    try:
        string = ' '.join(args)
        await ctx.send(file=generate_card(string, "templates/imgs/soniko.png", "soniko", 25, 83, 274, (0, 0, 0), 23))

    except FutebotException as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@commands.command()
async def speech(ctx, *args):
    try:
        string = " ".join(args)
        if not string.isdigit():
            await ctx.send(rec[random.randrange(0, len(rec) - 1)])
            return

        await ctx.send(file=generate_card(string, "templates/imgs/speech.png", "speech",
                                          110, 670, 10, (255, 255, 255), 4))

    except FutebotException as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@commands.command()
async def tano(ctx, *args):
    try:
        string = ' '.join(args)
        await ctx.send(file=generate_card(string, "templates/imgs/tano.png", "tano", 35, 330, 115, (0, 0, 0), 15))

    except FutebotException as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@commands.command()
async def magic(ctx, *args):
    try:
        string = args[0].split()
        description = args[1]

        img = None
        img_index = 0
        while img is None:
            url = generate_image_search_url(string)
            res = requests.get(url)
            image_link = res.json()["items"][img_index]["link"]

            img = generate_card_img_title_description(args[0], "templates/imgs/magic.png", "magic", 30, 40, 33,
                                                      (0, 0, 0), 25, image_link, 40, 70, 240, 240,
                                                      description, 40, 370, 20, "magic")
            img_index += 1

            if img is not None:
                await ctx.send(file=img)

    except FutebotException as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@commands.command()
async def hospital(ctx, *args):
    try:
        name = args[0]
        reason = args[1]
        await ctx.send(file=generate_card_multiple_texts("templates/imgs/hospital.png", "hospital",
                                                         (reason, 35, 400, 927, (0, 0, 0), 30, "helveticamedium"),
                                                         (name, 35, 590, 188, (0, 0, 0), 30, "helveticamedium")))
    except FutebotException as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])



@commands.command()
async def buemo(ctx, *args):
    try:
        string = ' '.join(args)
        await ctx.send(file=generate_card(string, "templates/imgs/buemo.png", "buemo", 35, 20, 100, (0, 0, 0), 40,
                                          "helvetica"))
    except FutebotException as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@commands.command()
async def twit(ctx, user: discord.User, *args):
    try:
        img_url = user.avatar_url._url
        user_display_name = '@'+user.display_name
        user_name = user.name
        string = ' '.join(args)

        await ctx.send(file=generate_card_twit(user_name, user_display_name,
                                                "templates/imgs/twit.png", "twit",
                                                img_url, string))
    except FutebotException as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])



@commands.command()
async def feijoada(ctx, *args):
    try:
        string = ' '.join(args)

        url = generate_image_search_url(args)
        res = requests.get(url)
        image_link = res.json()["items"][0]["link"]

        await ctx.send(file=generate_card_img(string, "templates/imgs/nada.png", "nada", 15, 205, 70, (0, 0, 0), 30,
                       image_link, 16, 55, 150, 150))

    except FutebotException as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@commands.command()
async def book(ctx, *args):
    try:
        if len(args) > 3:
            raise TooManyCharsException("Diminue esse textão, pfv")

        font_size = 120 - (25*len(args))

        string = '\n'.join(args)
        img = None
        img_index = 0
        while img is None:
            url = generate_image_search_url(args)
            res = requests.get(url)
            image_link = res.json()["items"][img_index]["link"]

            img = generate_card_img(string, "templates/imgs/oreilly.png", "book", font_size, 50, 150, (255, 255, 255),
                                    30, image_link, 30, 285, 300, 300, "garamond")
            img_index += 1

            if img is not None:
                await ctx.send(file=img)

    except FutebotException as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@commands.command()
async def tomacu(ctx, *args):
    try:
        string = ' '.join(args)
        await ctx.send(file=generate_card(string, "templates/imgs/tomacu.png", "tomacu", 40, 560, 110, (0, 0, 0), 15))

    except FutebotException as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@commands.command()
async def gordo(ctx, *args):
    try:
        string = ' '.join(args)
        await ctx.send(file=generate_card(string, "templates/imgs/gordo.png", "gordo", 40, 200, 525, (255, 0, 0), 10))

    except FutebotException as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])
