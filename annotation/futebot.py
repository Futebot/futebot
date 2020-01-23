from discord.ext.commands import Command

from util.commands import Commands


def command(*args, **kwargs):
    def inner(func):
        Commands.get_instance().register(func, kwargs['name'], kwargs['desc'], kwargs.get('params'))
        return func
    return inner
