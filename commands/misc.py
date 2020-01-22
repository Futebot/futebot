import time
from art import *

from annotation.futebot import command
from util.helpers import mention


def ping(ctx, arg=""):
    if arg == "":
        return "pong"
    else:
        return "Pinging " + mention(ctx, arg) + " 🏓"


def banner(string):
    if len(string) > 20:
        return "Diminue esse textão aí, pfv."

    return text2art(string)

def moji(string):
    try:
        return art(string)
    except Exception as e:
        return "Tenta esses moji aqui, fera: https://github.com/sepandhaghighi/art/blob/master/art/art_dic.py"


def scroll():
    dump = ".\n" * 100
    text = "eita fdp\n" + dump + "vou chamar o marreta :hammer:"
    return text
