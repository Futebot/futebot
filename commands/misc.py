import time

import slack
from art import *
from annotation.futebot import command
from util.helpers import mention

slack_client = slack.WebClient(token=os.getenv('SLACK_TOKEN'))


@command(name="ping", desc="Pings", params=["part_of_username"])
def ping(ctx, *args):
    # if args is None:
    return "pong 🏓"
    # arg = args[0][0]
    # if arg is None or arg == "":
    #     return "pong"
    # else:
    #     users_list = slack_client.users_list()["members"]

    #     return "Pinging " + mention(users_list, arg) + " 🏓"


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


@command(name="popcorn", desc="Add reactions to message, to rate a story.")
def popcorn(ctx, *args):

    slack_client.reactions_add(
        channel=ctx.channel,
        name="popcorn",
        timestamp=ctx.timestamp
    )
    slack_client.reactions_add(
        channel=ctx.channel,
        name="zero",
        timestamp=ctx.timestamp
    )
    slack_client.reactions_add(
        channel=ctx.channel,
        name="one",
        timestamp=ctx.timestamp
    )
    slack_client.reactions_add(
        channel=ctx.channel,
        name="two",
        timestamp=ctx.timestamp
    )
    slack_client.reactions_add(
        channel=ctx.channel,
        name="three",
        timestamp=ctx.timestamp
    )
    slack_client.reactions_add(
        channel=ctx.channel,
        name="four",
        timestamp=ctx.timestamp
    )
    slack_client.reactions_add(
        channel=ctx.channel,
        name="five",
        timestamp=ctx.timestamp
    )
    slack_client.reactions_add(
        channel=ctx.channel,
        name="six",
        timestamp=ctx.timestamp
    )
    slack_client.reactions_add(
        channel=ctx.channel,
        name="seven",
        timestamp=ctx.timestamp
    )
    slack_client.reactions_add(
        channel=ctx.channel,
        name="eight",
        timestamp=ctx.timestamp
    )
    slack_client.reactions_add(
        channel=ctx.channel,
        name="nine",
        timestamp=ctx.timestamp
    )
    slack_client.reactions_add(
        channel=ctx.channel,
        name="100",
        timestamp=ctx.timestamp
    )

    return None
