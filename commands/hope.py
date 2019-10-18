from annotation.futebot import command
from util.helpers import (
    get_json_field_from_url,
)
from .config import (
    COACH_ENDPOINT,
    HOROSCOPO_ENDPOINT,
)


@command(desc="Returns a random coach message")
async def coach(ctx):
    await ctx.send(
        get_json_field_from_url(
            COACH_ENDPOINT,
            "quoteText",
        )
    )


@command(desc="Returns the horoscope of the day.", params=["horoscope"])
async def horoscopo(ctx, arg):
    await ctx.send(
        get_json_field_from_url(
            HOROSCOPO_ENDPOINT.format(arg), "texto"
        )
    )


@command(desc="Sends a Yes or No GIF for a question.")
async def decide(ctx, arg):
    await ctx.send(
        get_json_field_from_url(
            "https://yesno.wtf/api", "image"
        )
    )
