import os
import yaml
from discord import Embed

from annotation.futebot import command
from service.command_suggestion_service import get_custom_dict


@command(desc="Adds a new custom command", params=["command_name", "command_content"])
async def add(ctx, *args):

    command_name = args[0]
    command_url = args[1]
    try:
        data = get_custom_dict()
    except FileNotFoundError as e:
        print("creating file")
        data = dict()

    data[command_name] = command_url

    with open(os.environ["COMMANDS_DATA_FILE"], 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


@command(desc="List Custom Commands")
async def listcustom(ctx):
    data = get_custom_dict()
    embed = Embed(title="Custom Commands list", color=0x00ff75)

    for cmd in data:
        embed.add_field(name=".{}".format(cmd),
                        value=data[cmd], inline=False)

    await ctx.send(embed=embed)


async def c(ctx, arg):
    data = get_custom_dict()
    await ctx.send(data[arg])
