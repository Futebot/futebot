import logging as puts
import random

from annotation.futebot import command
from service import roll_service
from util.helpers import (
    get_json_fields_from_url,
    RANDOM_EXCEPTION_COMEBACKS as rec,
)

from .config import CHARADA_ENDPOINT


def charada():
    fields = get_json_fields_from_url(
        CHARADA_ENDPOINT,
        "pergunta",
        "resposta",
    )
    response = ''
    for field in fields:
        response += field + '\n'

    return response


def roll(arg):
    try:
        response = roll_service.roll(arg)
        return response
    except Exception as e:
        puts.info(e)
        return rec[random.randrange(0, len(rec) - 1)]
