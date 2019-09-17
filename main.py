import logging as puts

from commands.utils import bot

puts.basicConfig(format="%(asctime)s - %(message)s", level=puts.INFO)

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

bot.run(os.environ["DISCORD_APP_TOKEN"])
