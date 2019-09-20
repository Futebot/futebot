import time
from art import *
from discord.ext.commands import CommandInvokeError

from util.helpers import mention
from discord.ext import commands


@commands.command()
async def ping(ctx, arg=""):
    if arg == "":
        await ctx.send("pong")
    else:
        await ctx.send("Pinging " + mention(ctx, arg) + " 🏓")


@commands.command()
async def banner(ctx, *args):
    string = ' '.join(args)

    if len(string) >= 12:
        await ctx.send("Diminue esse textão aí, pfv.")
        return

    art = text2art(string)
    await ctx.send("```" + art + "```")


@commands.command()
async def moji(ctx, *args):
    try:
        string = ' '.join(args)
        text = art(string)
        await ctx.send(text)
    except Exception as e:
        await ctx.send("Tenta esses moji aqui, fera: https://github.com/sepandhaghighi/art/blob/master/art/art_dic.py")

