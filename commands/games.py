import logging as puts
import random

from annotation.futebot import command
from service import roll_service
from util.helpers import (
    get_json_fields_from_url,
    RANDOM_EXCEPTION_COMEBACKS as rec,
)

from .config import CHARADA_ENDPOINT


# @command(name="charada", desc="Sends a random charade")
def charada(ctx):
    fields = get_json_fields_from_url(
        CHARADA_ENDPOINT,
        "pergunta",
        "resposta",
    )
    response = ''
    for field in fields:
        response += field + '\n'

    return response


@command(name="roll", desc="Rolls the dice", params=["1d6"])
def roll(ctx, arg):
    try:
        response = roll_service.roll(arg)
        return response
    except Exception as e:
        puts.info(e)
        return rec[random.randrange(0, len(rec) - 1)]
