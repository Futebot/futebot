from annotation.futebot import command
from util.helpers import (
    get_json_field_from_url,
)
from .config import (
    COACH_ENDPOINT,
    HOROSCOPO_ENDPOINT,
)


@command(name="coach", desc="Returns a random coach message")
def coach(ctx):
    return get_json_field_from_url(
            COACH_ENDPOINT,
            "quoteText",
        )


@command(name="horoscopo", desc="Returns the horoscope of the day.", params=["horoscope"])
def horoscopo(ctx, arg):
    return get_json_field_from_url(
            HOROSCOPO_ENDPOINT.format(arg), "texto"
        )


@command(name="decide", desc="Sends a Yes or No GIF for a question.")
def decide(ctx, arg):
    return get_json_field_from_url(
            "https://yesno.wtf/api", "image"
        )

