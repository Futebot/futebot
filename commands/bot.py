from discord import Embed

from annotation.futebot import command
from util.commands import Commands
from util.helpers import embed_commands


@command(desc="List all commands")
async def listall(ctx, grep=None):

    commands = Commands.get_instance().dictionary

    if grep == None:
       embed = embed_commands(commands)
    
    else:
        filtered_commands = {key:value for key, value in commands.items() if str.lower(grep) in key.lower()}
        embed = embed_commands(filtered_commands)

    await ctx.send(embed=embed)
