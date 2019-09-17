from util.helpers import (
    get_json_field_from_url,
)

from .utils import bot
from .config import (
    COACH_ENDPOINT,
    HOROSCOPO_ENDPOINT,
)

@bot.command()
async def coach(ctx):
    await ctx.send(
        get_json_field_from_url(
            COACH_ENDPOINT,
            "quoteText",
        )
    )


@bot.command()
async def horoscopo(ctx, arg):
    await ctx.send(
        get_json_field_from_url(
            HOROSCOPO_ENDPOINT.format(arg), "texto"
        )
    )
