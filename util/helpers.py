import logging as puts
import os
import requests
import uuid

from PIL import Image
from discord import File
from io import BytesIO

from commands.config import AVAILABLE_SPOILER_ACTIONS

RANDOM_EXCEPTION_COMEBACKS = ["Are you dumb?", "No, I don't think I will."]


def get_json_field_from_url(url: str, field: str):
    return get_json_fields_from_url(url, field)[0]


def get_json_fields_from_url(url: str, *fields: str):
    try:
        fields_value = []
        r = requests.get(url=url, headers={"Accept": "application/json"})
        for field in fields:
            fields_value.append(r.json()[field])

        return fields_value
    except Exception as e:
        puts.info(e)
        return ["Are you dumb?"]


def generate_image_search_url(search_terms, **kwargs):
    search_terms = " ".join(search_terms)

    google_image_query_url = (
        f"https://www.googleapis.com/customsearch/v1?"
        f"key={os.getenv('GOOGLE_CUSTOM_SEARCH_API_TOKEN')}&"
        f"cx={os.getenv('GOOGLE_CUSTOM_SEARCH_API_ID')}&"
        f"q={search_terms}&"
        f"searchType=image"
    )

    if kwargs.get("gif", None):
        return google_image_query_url + "&fileType=gif"

    return google_image_query_url


def mention(ctx, criteria):
    if len(criteria) < 3:
        return "Don't be evil."
        return
    mentioned = ""
    for member in ctx.message.channel.members:
        if criteria.lower() in member.name.lower():
            mentioned += member.mention + " "
    return mentioned


def _save_image(image_link):
    response = requests.get(image_link, stream=True)
    image = Image.open(BytesIO(response.content))
    filename = "{}.{}".format(uuid.uuid1(), image.format)
    image.save(filename)

    return filename


def create_discord_file_object(image_link, spoiler):
    filename = _save_image(image_link)
    f = File(open(filename, "rb"))
    if spoiler and spoiler in AVAILABLE_SPOILER_ACTIONS:
        setattr(f, 'filename', "{}{}".format("SPOILER_", f.filename))

    return f
