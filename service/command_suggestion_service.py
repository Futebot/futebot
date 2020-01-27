import os

import yaml
from fuzzywuzzy import process

from util.commands import Commands


def get_suggested_command(command):
    prefix = command

    if is_custom_command(command):
        return command
    else:
        command_tuple = get_command(command)
        command = command_tuple[1]
        return command


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
