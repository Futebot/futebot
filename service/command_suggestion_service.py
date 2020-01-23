import os

import yaml
from fuzzywuzzy import process

from util.commands import Commands


def execute_suggested_command(command):
    prefix = command
    suffix = ''
    try:
        prefix = command.split(' ')[0]
        suffix = command.split(' ', 1)[1]
    except:
        suffix = ''

    from commands.custom import c
    if is_custom_command(command):
        return c(command)
    else:
        command_tuple = get_command(command)
        command = command_tuple[1]
        if is_default_command(command):
            command_module = Commands.get_instance().dictionary[command]['module']

            module = getattr(__import__('commands'), command_module)
            method = getattr(module, command)

            return method(command)
        else:
            return c(command)


def is_custom_command(command):
    if command in get_custom_dict():
        return True
    return False


def is_default_command(command):
    if "module" in Commands.get_instance().dictionary[command]:
        return True
    return False


def get_custom_dict():
    with open(os.environ["COMMANDS_DATA_FILE"]) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def get_command(cmd):

    cmd_dict = list(Commands.get_instance().dictionary.keys())
    data = get_custom_dict()
    cmd_dict += list(data.keys())
    ratios = process.extract(cmd, cmd_dict)
    return cmd_dict, ratios[0][0]
