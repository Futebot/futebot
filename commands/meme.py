import logging as puts
import random
from discord.ext import commands

from exception.exceptions import FutebotException
from service.img_card_service import generate_card


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
