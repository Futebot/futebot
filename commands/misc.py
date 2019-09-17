from util.helpers import mention
from .utils import bot


@bot.command()
async def ping(ctx, arg=""):
    if arg == "":
        await ctx.send("pong")
    else:
        await ctx.send("Pinging " + mention(ctx, arg) + " 🏓")
