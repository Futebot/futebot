from discord import Embed

from annotation.futebot import command
from util.commands import Commands
from util.helpers import format_params, split_dict
from .config import DISCORD_EMBED_LIMIT


@command(desc="List all commands")
async def listall(ctx):
    commands = split_dict(Commands.get_instance().dictionary, DISCORD_EMBED_LIMIT)

    for page in commands:
        embed = Embed(title="Commands list", color=0x00ff75)

        for line in page:
            command = page[line]
            embed.add_field(name=".{} {}".format(line, format_params(command['params'])),
                            value=command['description'],
                            inline=False)

        await ctx.author.send(embed=embed)
