import logging as puts
import os
import re
import requests
import urllib


from annotation.futebot import command
from service.search_service import get_image
from util.helpers import (
    clean_html,
    get_weather_icon,
    format_string_to_query)

from .config import (
    DICTIONARY_PTBR_ENDPOINT,
    YT_RESULTS_ENDPOINT,
    YT_WATCH_ENDPOINT,
    WEATHER_ENDPOINT,
    LMGTFY_ENDPOINT)


@command(name="imgme", desc="Returns an image", params=["search_term"])
def imgme(ctx, search_query, spoiler=None):
    try:
        return get_image(search_query, spoiler)

    except Exception as e:
        puts.info(e)
        return e


@command(name="gifme", desc="Returns a GIF", params=["search_term"])
def gifme(ctx, search_query, spoiler=None):
    try:
        return get_image(search_query, spoiler, gif=True)

    except Exception as e:
        puts.info(e)
        return e


@command(name="youtube", desc="Returns an Youtube Video", params=["search_term"])
def youtube(ctx, string):
    try:
        query_string = urllib.parse.urlencode({"search_query": string})
        html_content = urllib.request.urlopen("{}{}".format(YT_RESULTS_ENDPOINT, query_string))
        search_results = re.findall(
            r"href=\"\/watch\?v=(.{11})", html_content.read().decode()
        )
        return "{}{}".format(YT_WATCH_ENDPOINT, search_results[0])
    except BaseException as e:
        return "Are you dumb?"


@command(name="dictionary", desc="Returns the meaning of a word", params=["word"])
def dictionary(ctx, term):
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

        return definition

    except Exception as e:
        puts.info(e)
        return e


@command(name="weather", desc="Returns the Weather", params=["city"])
def weather(ctx, location):
    try:
        print(location)
        endpoint = WEATHER_ENDPOINT.format(location, os.getenv("OPENWEATHER_KEY"))
        r = requests.get(endpoint)
        if r.status_code == 404:
            raise Exception("Place not found, coleguinha.")
        result = r.json()

        weather_conditions = "{} {}".format(get_weather_icon(result["weather"][0]["icon"]),
                                            result["weather"][0]["main"])
        temperature = ":thermometer: {}°C".format(result["main"]["temp"])
        humidity = ":droplet: {}%".format(result["main"]["humidity"])
        title = "Temperature in {} :".format(result["name"])
        response = title + "\n" + weather_conditions + "\n" + temperature + "\n" + humidity
        print(response)
        return response

    except Exception as e:
        puts.info(e)
        return e


@command(name="lmgtfy", desc="Returns search from LMGTFY", params=["word"])
def lmgtfy(ctx, string):
    query_string = format_string_to_query(string)
    endpoint = LMGTFY_ENDPOINT.format(query_string)
    return endpoint
