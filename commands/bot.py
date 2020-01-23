from discord import Embed
from annotation.futebot import command
from util.commands import Commands
from util.helpers import format_params, split_dict
from .config import DISCORD_EMBED_LIMIT


@command(name="listall", desc="List all commands")
def listall(ctx):
    commands = split_dict(Commands.get_instance().dictionary, DISCORD_EMBED_LIMIT)

    embed = "Commands list:\n"
    for page in commands:

        for line in page:
            command = page[line]
            embed += "*.{} {}*".format(line, format_params(command['params'])) + "\n" + command['description'] + "\n\n"
    return embed
