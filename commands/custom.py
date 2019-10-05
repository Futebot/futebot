import os
import yaml
from annotation.futebot import command


@command(desc="Adds a new custom command", params=["command_name", "command_content"])
async def add(ctx, *args):

    command_name = args[0]
    command_url = args[1]
    try:
        with open(os.environ["COMMANDS_DATA_FILE"]) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError as e:
        print("creating file")
        data = dict()

    data[command_name] = command_url

    with open(os.environ["COMMANDS_DATA_FILE"], 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


@command(desc="List Custom Commands")
async def listcustom(ctx):
    list = '```'
    with open(os.environ["COMMANDS_DATA_FILE"]) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        for cmd in data:
            list += ".c " + cmd + " -> " + data[cmd] + "\n"

        list += "```"
        await ctx.send(list)


@command(desc="Returns a command", params=["command_name"])
async def c(ctx, arg):
    with open(os.environ["COMMANDS_DATA_FILE"]) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        await ctx.message.delete()
        await ctx.send(data[arg])
