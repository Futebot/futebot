import re
import mimetypes
from io import BytesIO
import logging as puts
import os
import requests
import uuid
from collections import OrderedDict

from discord import File
from io import BytesIO


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


def generate_image_search_url(search_terms, file_type=".jpg"):
    search_terms = " ".join(search_terms)

    google_image_query_url = (
        f"https://www.googleapis.com/customsearch/v1?"
        f"key={os.getenv('GOOGLE_CUSTOM_SEARCH_API_TOKEN')}&"
        f"cx={os.getenv('GOOGLE_CUSTOM_SEARCH_API_ID')}&"
        f"q={search_terms}&"
        f"searchType=image"
    )

    if file_type == ".gif":
        return google_image_query_url + "&fileType=gif"

    return google_image_query_url


def mention(members, criteria):
    if len(criteria) < 3:
        return "Don't be evil."
    mentioned = ""
    for member in members:
        print(member)
        if (criteria.lower() in member.name.lower()) or (criteria.lower() in member.name.lower()):
            mentioned += "@" + member.name + " "
    return mentioned


def save_image_to_imgur(image):
    from util.imgur import Imgur
    imgur = Imgur()
    imgur_link = imgur.upload(image)

    return imgur_link


def create_discord_file_object(file_bytes, file_extension=".jpg", spoiler=None):
    from commands.config import AVAILABLE_SPOILER_ACTIONS

    filename = "{}{}".format(uuid.uuid1(), file_extension)
    discord_file = File(file_bytes, filename=filename)
    if spoiler and spoiler in AVAILABLE_SPOILER_ACTIONS:
        setattr(discord_file, "filename", "{}{}".format("SPOILER_", discord_file.filename))

    return discord_file


def image_to_byte_array(image):
    imgByteArr = BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


def validate_image(image_link):
    response = requests.get(image_link)
    if "image" not in response.headers["Content-Type"]:
        return (False, None)
    file_bytes = BytesIO(response.content)

    return (True, file_bytes)


def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def get_weather_icon(code):
    if "10" in code or "09" in code:
        return ":rain_cloud:"
    if "11" in code:
        return ":lightning:"
    if "13" in code:
        return ":snowflake:"
    if "01" in code:
        return ":sunny:"
    if "02" in code:
        return ":sun_small_cloud:"
    if "03" in code or "04" in code or "50" in code:
        return ":cloud:"


def format_params(params):
    if params is None:
        return ""
    else:
        params_response = ""
        for param in params:
            params_response += "[{}] ".format(param)
        return params_response


def format_string_to_query(word: str):
    cleanword = word
    cleanword = (
        cleanword.replace('+', '%2B')
        .replace(' ', '+')
        .replace('%20', '+')
        .replace('*', '%2A')
        .replace('/', '%2F')
        .replace('@', '%40')
    )
    return cleanword


def split_dict(input_dict, size):
    return_dict = OrderedDict()

    for k, v in sorted(input_dict.items()):
        if len(return_dict) == size:
            yield return_dict
            return_dict = OrderedDict()

        return_dict[k] = v

    yield return_dict
