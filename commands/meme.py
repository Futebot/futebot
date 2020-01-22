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


def soniko(string):
    try:
        return generate_card(string, "templates/imgs/soniko.png", "soniko", 25, 83, 274, (0, 0, 0), 23)

    except FutebotException as e:
        puts.info(e)
        return e


def speech(string):
    try:
        if not string.isdigit():
            return rec[random.randrange(0, len(rec) - 1)]

        return generate_card(string, "templates/imgs/speech.png", "speech",
                                          110, 670, 10, (255, 255, 255), 4)

    except FutebotException as e:
        puts.info(e)
        return e


def tano(string):
    try:
        return generate_card(string, "templates/imgs/tano.png", "tano", 35, 330, 115, (0, 0, 0), 15)

    except FutebotException as e:
        puts.info(e)
        return e


def magic(string, description):
    try:
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


def hospital(name, reason):
    try:
        return generate_card_multiple_texts("templates/imgs/hospital.png", "hospital",
                                                         (reason, 35, 400, 927, (0, 0, 0), 30, "helveticamedium"),
                                                         (name, 35, 590, 188, (0, 0, 0), 30, "helveticamedium"))
    except FutebotException as e:
        puts.info(e)
        return e


def antagonista(headline, text):
    try:
        headline = "\"" + headline + "\""
        return generate_card_multiple_texts("templates/imgs/anta.png", "anta",
                                                         (headline, 50, 40, 250, (0, 0, 0), 30, "times-new-roman"),
                                                         (text, 30, 50, 580, (0, 0, 0), 60, "times-new-roman"))
    except FutebotException as e:
        puts.info(e)
        return e


def buemo(string):
    try:
        return generate_card(string, "templates/imgs/buemo.png", "buemo", 35, 20, 100, (0, 0, 0), 40,
                                          "helvetica")
    except FutebotException as e:
        puts.info(e)
        return e


def twit(ctx, user: discord.User, *args):
    try:
        img_url = user.avatar_url._url
        user_display_name = '@'+user.display_name
        user_name = user.name
        string = ' '.join(args)

        return generate_card_twit(user_name, user_display_name,
                                               "templates/imgs/twit.png", "twit",
                                               img_url, string)
    except FutebotException as e:
        puts.info(e)
        return e


def feijoada(string):
    try:
        url = generate_image_search_url(string)
        res = requests.get(url)
        image_link = res.json()["items"][0]["link"]

        return generate_card_img(string, "templates/imgs/nada.png", "nada", 15, 205, 70, (0, 0, 0), 30,
                       image_link, 16, 55, 150, 150)

    except FutebotException as e:
        puts.info(e)
        return e


def book(string):
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


def tomacu(string):
    try:
        return generate_card(string, "templates/imgs/tomacu.png", "tomacu", 40, 560, 110, (0, 0, 0), 15)

    except FutebotException as e:
        puts.info(e)
        return e


def gordo(string):
    try:
        return generate_card(string, "templates/imgs/gordo.png", "gordo", 40, 200, 525, (255, 0, 0), 10)

    except FutebotException as e:
        puts.info(e)
        return e
