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
from commands.meme import (
    book,
    buemo,
    feijoada,
    gordo,
    magic,
    soniko,
    speech,
    tano,
    tomacu,
    twit

)
from commands.hope import (
    coach,
    horoscopo,
    decide
)
from commands.misc import (
    banner,
    moji,
    ping
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
bot.add_command(tano)
bot.add_command(tomacu)
bot.add_command(feijoada)
bot.add_command(banner)
bot.add_command(moji)
bot.add_command(decide)
bot.add_command(book)
bot.add_command(buemo)
bot.add_command(magic)
bot.add_command(gordo)
bot.add_command(twit)

bot.run(os.environ["DISCORD_APP_TOKEN"])
