import time
from art import *

from annotation.futebot import command
from util.helpers import mention


@command(desc="Pings", params=["part_of_username"])
async def ping(ctx, arg=""):
    if arg == "":
        await ctx.send("pong")
    else:
        await ctx.send("Pinging " + mention(ctx, arg) + " 🏓")


@command(desc="Generates an ASCII banner", params=["word"])
async def banner(ctx, *args):
    string = ' '.join(args)

    if len(string) > 20:
        await ctx.send("Diminue esse textão aí, pfv.")
        return

    art = text2art(string)
    await ctx.send("```" + art + "```")


@command(desc="Generates a one liner emoji", params=["emoji_name"])
async def moji(ctx, *args):
    try:
        string = ' '.join(args)
        text = art(string)
        await ctx.send(text)
    except Exception as e:
        await ctx.send("Tenta esses moji aqui, fera: https://github.com/sepandhaghighi/art/blob/master/art/art_dic.py")


@command(desc="Scrooooooooooooooooll to remove that NSFW messages")
async def scroll(ctx):
    dump = ".\n" * 100
    text = "eita fdp\n" + dump + "vou chamar o marreta :hammer:"
    await ctx.send(text)
