from discord import Embed

from annotation.futebot import command
from util.commands import Commands
from util.helpers import format_params


@command(desc="List all commands")
async def listall(ctx, grep=None):

    commands = Commands.get_instance().dictionary
    embed = Embed(title="Commands list", color=0x00ff75)

    if grep == None:

        for cmd in sorted(commands.keys()):
            embed.add_field(name=".{} {}".format(cmd, format_params(commands[cmd]['params'])),
                            value=commands[cmd]['description'], inline=False)
    
    else:
        filtered_commands = {key:value for key, value in commands.items() if str.lower(grep) in key.lower()}

        if len(filtered_commands) < 1:
            embed.add_field(name="achei óh",
                            value="varios nadas...", inline=False)

        else:    
            for cmd in sorted(filtered_commands.keys()):
                embed.add_field(name=".{} {}".format(cmd, format_params(commands[cmd]['params'])),
                                value=commands[cmd]['description'], inline=False)

    await ctx.send(embed=embed)
