from discord import Embed

from annotation.futebot import command
from util.commands import Commands
from util.helpers import format_params


@command(desc="List all commands")
async def listall(ctx):

    commands = Commands.get_instance().dictionary
    embed = Embed(title="Commands list", color=0x00ff75)

    for cmd in sorted(commands.keys()):
        embed.add_field(name=".{} {}".format(cmd, format_params(commands[cmd]['params'])),
                        value=commands[cmd]['description'], inline=False)

    await ctx.send(embed=embed)
