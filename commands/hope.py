from annotation.futebot import command
from util.helpers import (
    get_json_field_from_url,
)
from .config import (
    COACH_ENDPOINT,
    HOROSCOPO_ENDPOINT,
)


def coach(ctx):
    return get_json_field_from_url(
            COACH_ENDPOINT,
            "quoteText",
        )


def horoscopo(arg):
    return get_json_field_from_url(
            HOROSCOPO_ENDPOINT.format(arg), "texto"
        )


def decide(arg):
    return get_json_field_from_url(
            "https://yesno.wtf/api", "image"
        )

