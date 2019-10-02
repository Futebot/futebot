from discord.ext import commands

from annotation.futebot import command
from util.helpers import (
    get_json_field_from_url,
)
from .config import (
    COACH_ENDPOINT,
    HOROSCOPO_ENDPOINT,
)


@command
@commands.command()
async def coach(ctx):
    await ctx.send(
        get_json_field_from_url(
            COACH_ENDPOINT,
            "quoteText",
        )
    )


@command
@commands.command()
async def horoscopo(ctx, arg):
    await ctx.send(
        get_json_field_from_url(
            HOROSCOPO_ENDPOINT.format(arg), "texto"
        )
    )


@command
@commands.command()
async def decide(ctx, arg):
    await ctx.send(
        get_json_field_from_url(
            "https://yesno.wtf/api", "image"
        )
    )
