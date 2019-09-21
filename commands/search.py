from io import BytesIO
import logging as puts
import random
import requests
import urllib

from discord.ext import commands

from util.helpers import (
    generate_image_search_url,
    RANDOM_EXCEPTION_COMEBACKS as rec,
)

from .config import (
    AVAILABLE_SPOILER_ACTIONS,
    YT_RESULTS_ENDPOINT,
    YT_WATCH_ENDPOINT,
)


@commands.command()
async def imgme(ctx, search_query, spoiler=None):
    try:
        url = generate_image_search_url(search_query)
        res = requests.get(url)
        image_link = res.json()["items"][0]["link"]

        f = create_discord_file_object(image_link, spoiler)
        await ctx.send(file=f)

    except Exception as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@commands.command()
async def gifme(ctx, search_query, spoiler=None):
    try:
        url = generate_image_search_url(search_query, gif=True)
        res = requests.get(url)
        image_link = res.json()["items"][0]["link"]

        f = create_discord_file_object(image_link, spoiler)
        await ctx.send(file=f)

    except Exception as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])


@commands.command()
async def youtube(ctx, *args):
    try:
        query_string = urllib.parse.urlencode({"search_query": " ".join(args)})
        html_content = urllib.request.urlopen("{}{}".format(YT_RESULTS_ENDPOINT, query_string))
        search_results = re.findall(
            r"href=\"\/watch\?v=(.{11})", html_content.read().decode()
        )
        await ctx.send("{}{}".format(YT_WATCH_ENDPOINT, search_results[0]))
    except BaseException:
        await ctx.send("Are you dumb?")
