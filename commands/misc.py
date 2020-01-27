import time
from art import *
from slackclient import client, SlackClient

from annotation.futebot import command
from util.helpers import mention


@command(name="ping", desc="Pings", params=["part_of_username"])
def ping(ctx, arg=""):
    if arg == "":
        return "pong"
    else:
        return "Pinging " + mention(arg) + " 🏓"


@command(name="banner", desc="Generates an ASCII banner", params=["word"])
def banner(ctx, *args):
    string = ' '.join(args[0])
    if len(string) > 20:
        return "Diminue esse textão aí, pfv."

    return "```" + text2art(string) + "```"


@command(name="moji", desc="Generates a one liner emoji", params=["emoji_name"])
def moji(ctx, *args):
    try:
        string = ' '.join(args[0])
        return art(string)
    except Exception as e:
        return "Tenta esses moji aqui, fera: https://github.com/sepandhaghighi/art/blob/master/art/art_dic.py"


@command(name="scroll", desc="Scrooooooooooooooooll to remove that NSFW messages")
def scroll(ctx):
    dump = ".\n" * 100
    text = "eita fdp\n" + dump + "vou chamar o marreta :hammer:"
    return text

@command(name="historia", desc="Add reactions to message, to rate a story.")
def scroll(ctx, *args):
    slack_client = SlackClient(os.getenv('SLACK_TOKEN'))

    slack_client.reactions_add(
        channel=ctx.channel,
        name="thumbsup",
        timestamp=ctx.timestamp
    )

    return None

