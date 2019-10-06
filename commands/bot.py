from annotation.futebot import command
from util.commands import Commands
from util.helpers import format_params


@command(desc="List all commands")
async def listall(ctx):

    commands = Commands.get_instance().dictionary
    commands_response = ":robot: \n\n Commands List:\n\n"

    for cmd in sorted(commands.keys()):
        commands_response += "**.{} {}** -> *{}*\n".format(cmd, format_params(commands[cmd]['params']),
                                                           commands[cmd]['description'])

    await ctx.send(commands_response)
