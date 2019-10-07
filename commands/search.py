import logging as puts
import os
import random

import re
import requests
import urllib

from discord import Embed

from annotation.futebot import command
from util.helpers import (
    clean_html,
    create_discord_file_object,
    generate_image_search_url,
    RANDOM_EXCEPTION_COMEBACKS as rec,
    validate_image,
    get_weather_icon)

from .config import (
    AVAILABLE_SPOILER_ACTIONS,
    DICTIONARY_PTBR_ENDPOINT,
    IMGUR_CLIENT_ID,
    YT_RESULTS_ENDPOINT,
    YT_WATCH_ENDPOINT,
    WEATHER_ENDPOINT)


@command(desc="Returns an image", params=["search_term"])
async def imgme(ctx, search_query, spoiler=None):
    try:
        url = generate_image_search_url(search_query)
        res = requests.get(url)
        search_result = res.json()
        if "items" not in search_result:
            raise Exception("We couldn't find any images for your search")

        image_is_valid = False

        for item in search_result["items"]:
            image_link = item["link"]
            image_is_valid, file_bytes = validate_image(image_link)
            if image_is_valid:
                f = create_discord_file_object(file_bytes, ".jpg", spoiler)
                await ctx.send(file=f)
                break

    except Exception as e:
        puts.info(e)
        await ctx.send(e)


@command(desc="Rertuns a GIF", params=["search_term"])
async def gifme(ctx, search_query, spoiler=None):
    try:
        url = generate_image_search_url(search_query, gif=True)
        res = requests.get(url)
        search_result = res.json()
        if "items" not in search_result:
            raise Exception("We couldn't find any images for your search")

        image_is_valid = False

        for item in search_result["items"]:
            image_link = item["link"]
            image_is_valid, file_bytes = validate_image(image_link)
            if image_is_valid:
                f = create_discord_file_object(file_bytes, ".gif", spoiler)
                await ctx.send(file=f)
                break

    except Exception as e:
        puts.info(e)
        await ctx.send(e)


@command(desc="Returns an Youtube Video", params=["search_term"])
async def youtube(ctx, *args):
    try:
        query_string = urllib.parse.urlencode({"search_query": " ".join(args)})
        html_content = urllib.request.urlopen("{}{}".format(YT_RESULTS_ENDPOINT, query_string))
        search_results = re.findall(
            r"href=\"\/watch\?v=(.{11})", html_content.read().decode()
        )
        await ctx.send("{}{}".format(YT_WATCH_ENDPOINT, search_results[0]))
    except BaseException as e:
        await ctx.send("Are you dumb?")


@command(desc="Returns the meaning of a word", params=["word"])
async def dictionary(ctx, term, *args):
    try:
        endpoint = DICTIONARY_PTBR_ENDPOINT.format(term)
        r = requests.get(endpoint)
        if r.status_code == 404:
            raise Exception("Word not found, coleguinha.")
        result = r.json()
        definition = "**{}**\n\n".format(term)
        first_entry = None
        if "superEntry" in result:
            first_entry = result["superEntry"][0]["entry"]
        if "entry" in result:
            first_entry = result["entry"]

        if "sense" in first_entry:
            for entry_def in first_entry["sense"]:
                definition += "{}\n".format(
                    clean_html(entry_def["def"].replace("<br/>", "\n"))
                )

        await ctx.send(definition)

    except Exception as e:
        puts.info(e)
        await ctx.send(e)


@command(desc="Returns the Weather", params=["city"])
async def weather(ctx, arg):
    try:
        endpoint = WEATHER_ENDPOINT.format(arg, os.getenv("OPENWEATHER_KEY"))
        r = requests.get(endpoint)
        if r.status_code == 404:
            raise Exception("Place not found, coleguinha.")
        result = r.json()

        weather_conditions = "{} {}".format(get_weather_icon(result["weather"][0]["icon"]),
                                            result["weather"][0]["main"])

        temperature = ":thermometer: {}°C".format(result["main"]["temp"])

        humidity = ":droplet: {}%".format(result["main"]["humidity"])

        embed = Embed(title="Temperature in {}".format(result["name"],
                      description=weather_conditions,
                      color=0x0B5394))

        embed.add_field(name="Conditions", value=weather_conditions, inline=True)
        embed.add_field(name="Temperature", value=temperature, inline=True)
        embed.add_field(name="Humidity", value=humidity, inline=True)

        await ctx.send(embed=embed)

    except Exception as e:
        puts.info(e)
        await ctx.send(e)
