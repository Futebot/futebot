from discord.ext import commands

from util.helpers import (
    get_json_field_from_url,
)
from .config import (
    COACH_ENDPOINT,
    HOROSCOPO_ENDPOINT,
)


@commands.command()
async def coach(ctx):
    await ctx.send(
        get_json_field_from_url(
            COACH_ENDPOINT,
            "quoteText",
        )
    )


@commands.command()
async def horoscopo(ctx, arg):
    await ctx.send(
        get_json_field_from_url(
            HOROSCOPO_ENDPOINT.format(arg), "texto"
        )
    )


@commands.command()
async def decide(ctx, arg):
    await ctx.send(
        get_json_field_from_url(
            "https://yesno.wtf/api", "image"
        )
    )
