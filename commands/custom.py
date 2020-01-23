import os
import yaml
from discord import Embed

from annotation.futebot import command
from exception.exceptions import NoArgumentException
from service.command_suggestion_service import get_custom_dict
from util.helpers import split_dict
from .config import DISCORD_EMBED_LIMIT


@command(name="add", desc="Adds a new custom command", params=["command_name", "command_content"])
def add(ctx, command_name, command_url):

    try:
        data = get_custom_dict()
    except FileNotFoundError as e:
        print("creating file")
        data = dict()

    data[command_name] = command_url

    with open(os.environ["COMMANDS_DATA_FILE"], 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


@command(name="rm", desc="Removes custom command", params=["command_name"])
def rm(ctx, command_name=""):
    try:
        if command_name == "":
            raise NoArgumentException("Are you dumb?")

        data = get_custom_dict()
        data.pop(command_name)

        with open(os.environ["COMMANDS_DATA_FILE"], 'w') as f:
            yaml.dump(data, f, default_flow_style=False)

    except FileNotFoundError as e:
        return "buguei"
    except KeyError as e:
        return "Tem esse comando ai não"
    except Exception as e:
        return e


@command(name="listcustom", desc="List Custom Commands")
def listcustom(ctx):
    custom_commands = split_dict(get_custom_dict(), DISCORD_EMBED_LIMIT)

    embed = "```Custom Commands list\n"
    for page in custom_commands:

        for line in page:
            embed += ".{}".format(line) + "\n" + page[line] + "\n\n"
    embed += "```"
    return embed


def c(ctx, arg):
    data = get_custom_dict()
    return data[arg]
