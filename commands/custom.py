import os
from discord.ext import commands
import yaml
from annotation.futebot import command


@command
@commands.command()
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


@command
@commands.command()
async def list(ctx):
    list = '```'
    with open(os.environ["COMMANDS_DATA_FILE"]) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        for cmd in data:
            list += ".c " + cmd + " -> " + data[cmd] + "\n"

        list += "```"
        await ctx.send(list)


@command
@commands.command()
async def c(ctx, arg):
    with open(os.environ["COMMANDS_DATA_FILE"]) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        await ctx.message.delete()
        await ctx.send(data[arg])
