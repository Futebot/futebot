import logging as puts
import os
from discord.ext.commands import CommandNotFound
from commands.utils import bot

from service.command_suggestion_service import execute_suggested_command

puts.basicConfig(format="%(asctime)s - %(message)s", level=puts.INFO)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await execute_suggested_command(ctx)
        return
    raise error


bot.run(os.environ["DISCORD_APP_TOKEN"])
