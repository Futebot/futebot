import logging as puts
import os

from discord.ext.commands import CommandNotFound

from commands.custom import c
from commands.utils import bot

puts.basicConfig(format="%(asctime)s - %(message)s", level=puts.INFO)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await c(ctx, ctx.invoked_with)
        return
    raise error

bot.run(os.environ["DISCORD_APP_TOKEN"])
