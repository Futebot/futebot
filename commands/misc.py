from util.helpers import mention
from discord.ext import commands


@commands.command()
async def ping2(ctx, arg=""):
    if arg == "":
        await ctx.send("pong")
    else:
        await ctx.send("Pinging " + mention(ctx, arg) + " 🏓")
