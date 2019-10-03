from discord.ext.commands import Command

from commands.utils import bot


def command(func: Command):
    bot.add_command(func)
