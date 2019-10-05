from annotation.futebot import command
from util.commands import Commands


def format_params(params):
    if params is None:
        return ""
    else:
        params_response = ""
        for param in params:
            params_response += "[{}] ".format(param)
        return params_response


@command(desc="List all commands")
async def listall(ctx):

    commands = Commands.get_instance().dictionary
    commands_response = ":robot: \n\n Commands List:\n\n"

    for cmd in sorted(commands.keys()):
        commands_response += "**.{} {}** -> *{}*\n".format(cmd, format_params(commands[cmd]['params']),
                                                           commands[cmd]['description'])

    await ctx.send(commands_response)
