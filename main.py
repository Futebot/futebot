import logging as puts
import os
import random
import re
import urllib

import requests
from discord.ext import commands
from exception.exceptions import FutebotException
from service import roll_service
from service.img_card_service import generate_card
from util.helpers import (
    generate_image_search_url,
    RANDOM_EXCEPTION_COMEBACKS as rec,
    get_json_fields_from_url,
    get_json_field_from_url,
    mention,
)
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
