from discord.ext.commands import Command

from commands.utils import bot
from util.commands import Commands


def command(*args, **kwargs):
    def inner(func):
        cls = Command(func)
        bot.add_command(cls)

        Commands.get_instance().register(cls.qualified_name, kwargs['desc'], kwargs.get('params'))

        return func
    return inner
