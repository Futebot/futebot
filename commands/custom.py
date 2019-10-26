import os
import yaml
from discord import Embed

from annotation.futebot import command
from exception.exceptions import NoArgumentException
from service.command_suggestion_service import get_custom_dict
from util.helpers import split_dict
from .config import DISCORD_EMBED_LIMIT


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


@command(desc="Removes custom command", params=["command_name"])
async def rm(ctx, command_name=""):
    try:
        if command_name == "":
            raise NoArgumentException("Are you dumb?")

        data = get_custom_dict()
        data.pop(command_name)

        with open(os.environ["COMMANDS_DATA_FILE"], 'w') as f:
            yaml.dump(data, f, default_flow_style=False)

    except FileNotFoundError as e:
        await ctx.send("buguei")
    except KeyError as e:
        await ctx.send("Tem esse comando ai não")
    except Exception as e:
        await ctx.send(e)


@command(desc="List Custom Commands")
async def listcustom(ctx):
    custom_commands = split_dict(get_custom_dict(), DISCORD_EMBED_LIMIT)

    for page in custom_commands:
        embed = Embed(title="Custom Commands list", color=0x00ff75)

        for line in page:
            embed.add_field(name=".{}".format(line),
                            value=page[line],
                            inline=False)

        await ctx.author.send(embed=embed)


async def c(ctx, arg):
    data = get_custom_dict()
    await ctx.send(data[arg])
