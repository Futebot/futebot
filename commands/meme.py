import logging as puts
import random

import discord

from annotation.futebot import command
from util.helpers import RANDOM_EXCEPTION_COMEBACKS as rec
import requests

from exception.exceptions import FutebotException, TooManyCharsException
from service.img_card_service import generate_card, generate_card_img, generate_card_img_title_description, \
    generate_card_twit, generate_card_multiple_texts
from util.helpers import generate_image_search_url


@command(name="soniko", desc="Generates a Soniko image", params=["caption"])
def soniko(ctx, *args):
    try:
        string = ' '.join(args[0])
        response = generate_card(string, "templates/imgs/soniko.png", "soniko", 25, 83, 274, (0, 0, 0), 23)
        return response

    except FutebotException as e:
        puts.info(e)
        return e


@command(name="speech", desc="Generates a Speech image", params=["grade_0_to_100"])
def speech(ctx, *args):
    try:
        string = ' '.join(args[0])
        if not string.isdigit():
            return rec[random.randrange(0, len(rec) - 1)]

        return generate_card(string, "templates/imgs/speech.png", "speech",
                                          110, 670, 10, (255, 255, 255), 4)

    except FutebotException as e:
        puts.info(e)
        return e


@command(name="tano", desc="Generates a Tano facebook conversation", params=["place"])
def tano(ctx, *args):
    try:
        string = ' '.join(args[0])
        return generate_card(string, "templates/imgs/tano.png", "tano", 35, 330, 115, (0, 0, 0), 15)

    except FutebotException as e:
        puts.info(e)
        return e


@command(name="magic", desc="Generates a Magic Card with a title and description", params=["title", "description"])
def magic(ctx, *args):
    try:
        string = args[0][0]
        description = args[0][1]
        c = None
        img_index = 0
        while img is None:
            url = generate_image_search_url(string)
            res = requests.get(url)
            image_link = res.json()["items"][img_index]["link"]

            img = generate_card_img_title_description(string, "templates/imgs/magic.png", "magic", 30, 40, 33,
                                                      (0, 0, 0), 25, image_link, 40, 70, 240, 240,
                                                      description, 40, 370, 20, "magic")
            img_index += 1

            if img is not None:
                return img

    except FutebotException as e:
        puts.info(e)
        return e


@command(name="hospital", desc="Generates a whatsapp hospital conversation image", params=["reason", "person_name"])
def hospital(ctx, *args):
    try:
        reason = args[0][0]
        name = args[0][1]
        return generate_card_multiple_texts("templates/imgs/hospital.png", "hospital",
                                                         (reason, 35, 400, 927, (0, 0, 0), 30, "helveticamedium"),
                                                         (name, 35, 590, 188, (0, 0, 0), 30, "helveticamedium"))
    except FutebotException as e:
        puts.info(e)
        return e


@command(name="antagonista", desc="Generates an Antagonista headline image", params=["headline", "text"])
def antagonista(ctx, *args):
    try:
        headline = args[0][0]
        text = args[0][1]
        headline = "\"" + headline + "\""
        return generate_card_multiple_texts("templates/imgs/anta.png", "anta",
                                                         (headline, 50, 40, 250, (0, 0, 0), 30, "times-new-roman"),
                                                         (text, 30, 50, 580, (0, 0, 0), 60, "times-new-roman"))
    except FutebotException as e:
        puts.info(e)
        return e


@command(name="buemo", desc="Generates a Buemo Tweet", params=["tweet"])
def buemo(ctx, *args):
    try:
        string = ' '.join(args[0])
        return generate_card(string, "templates/imgs/buemo.png", "buemo", 35, 20, 100, (0, 0, 0), 40,
                                          "helvetica")
    except FutebotException as e:
        puts.info(e)
        return e


@command(name="twit", desc="Generates a @User tweet", params=["user", "tweet"])
def twit(ctx, user, string):
    try:
        img_url = user.avatar_url._url
        user_display_name = '@'+user.display_name
        user_name = user.name

        return generate_card_twit(user_name, user_display_name,
                                               "templates/imgs/twit.png", "twit",
                                               img_url, string)
    except FutebotException as e:
        puts.info(e)
        return e


@command(name="feijoada", desc="Generates a Feijoada image", params=["name"])
def feijoada(ctx, *args):
    try:
        string = ' '.join(args[0])
        url = generate_image_search_url(string)
        res = requests.get(url)
        image_link = res.json()["items"][0]["link"]

        return generate_card_img(string, "templates/imgs/nada.png", "nada", 15, 205, 70, (0, 0, 0), 30,
                       image_link, 16, 55, 150, 150)

    except FutebotException as e:
        puts.info(e)
        return e


@command(name="book", desc="Generates an Oreilly book cover", params=["book_name"])
def book(ctx, *args):
    string = ' '.join(args[0])
    try:
        if len(string.split(' ')) > 3:
            raise TooManyCharsException("Diminue esse textão, pfv")

        font_size = 120 - (25*len(string.split(' ')))

        string = '\n'.join(string.split(' '))
        img = None
        img_index = 0
        while img is None:
            url = generate_image_search_url(string.split(' '))
            res = requests.get(url)
            image_link = res.json()["items"][img_index]["link"]

            img = generate_card_img(string, "templates/imgs/oreilly.png", "book", font_size, 50, 150, (255, 255, 255),
                                    30, image_link, 30, 285, 300, 300, "garamond")
            img_index += 1

            if img is not None:
                return img

    except FutebotException as e:
        puts.info(e)
        return e


@command(name="tomacu", desc="Generates a Tomacu image", params=["name"])
def tomacu(ctx, *args):
    try:
        string = ' '.join(args[0])
        return generate_card(string, "templates/imgs/tomacu.png", "tomacu", 40, 560, 110, (0, 0, 0), 15)

    except FutebotException as e:
        puts.info(e)
        return e


@command(name="gordo", desc="Generates a Sou Gordo shirt image", params=["adjective"])
def gordo(ctx, *args):
    try:
        string = ' '.join(args[0])
        return generate_card(string, "templates/imgs/gordo.png", "gordo", 40, 200, 525, (255, 0, 0), 10)

    except FutebotException as e:
        puts.info(e)
        return e
