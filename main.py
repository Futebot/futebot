import logging as puts
import os
from commands.utils import bot

puts.basicConfig(format="%(asctime)s - %(message)s", level=puts.INFO)

bot.run(os.environ["DISCORD_APP_TOKEN"])
