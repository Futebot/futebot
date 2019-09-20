import logging as puts
import os

from commands.utils import bot

from commands.bot import (
    listall,
)
from commands.games import (
    charada,
    roll,
)
from commands.hope import (
    coach,
    horoscopo,
)
from commands.meme import (
    soniko,
    speech,
)
from commands.misc import (
    ping,
)
from commands.search import (
    imgme,
    gifme,
    youtube,
)

puts.basicConfig(format="%(asctime)s - %(message)s", level=puts.INFO)

bot.add_command(listall)
bot.add_command(charada)
bot.add_command(roll)
bot.add_command(coach)
bot.add_command(horoscopo)
bot.add_command(soniko)
bot.add_command(speech)
bot.add_command(ping)
bot.add_command(imgme)
bot.add_command(gifme)
bot.add_command(youtube)

bot.run(os.environ["DISCORD_APP_TOKEN"])
