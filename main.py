import logging as puts
import os

from commands.utils import bot

from commands.bot import *
from commands.custom import *
from commands.games import *
from commands.hope import *
from commands.meme import *
from commands.misc import *
from commands.search import *

puts.basicConfig(format="%(asctime)s - %(message)s", level=puts.INFO)

bot.run(os.environ["DISCORD_APP_TOKEN"])
