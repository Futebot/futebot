import time
from art import *

from annotation.futebot import command
from util.helpers import mention


@command(name="ping", desc="Pings", params=["part_of_username"])
def ping(arg=""):
    if arg == "":
        return "pong"
    else:
        return "Pinging " + mention(arg) + " 🏓"


@command(name="banner", desc="Generates an ASCII banner", params=["word"])
def banner(string):
    if len(string) > 20:
        return "Diminue esse textão aí, pfv."

    return text2art(string)


@command(name="moji", desc="Generates a one liner emoji", params=["emoji_name"])
def moji(string):
    try:
        return art(string)
    except Exception as e:
        return "Tenta esses moji aqui, fera: https://github.com/sepandhaghighi/art/blob/master/art/art_dic.py"


@command(name="scroll", desc="Scrooooooooooooooooll to remove that NSFW messages")
def scroll():
    dump = ".\n" * 100
    text = "eita fdp\n" + dump + "vou chamar o marreta :hammer:"
    return text
