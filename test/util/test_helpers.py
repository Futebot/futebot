import os
from discord import File

from util.helpers import (
    create_discord_file_object,
    generate_image_search_url,
)


def test_generate_image_search_url():
    """Test url generator for google image queries"""
    query = generate_image_search_url(("this", "is", "a", "test"))

    google_image_query_url = (
        f"https://www.googleapis.com/customsearch/v1?"
        f"key={os.getenv('GOOGLE_CUSTOM_SEARCH_API_TOKEN')}&"
        f"cx={os.getenv('GOOGLE_CUSTOM_SEARCH_API_ID')}&"
        f"q={'this is a test'}&"
        f"searchType=image"
    )
    if not query == google_image_query_url:
        raise AssertionError()


def test_generate_image_search_url_gif():
    """Test url generator for google gif queries"""
    query = generate_image_search_url(("this", "is", "a", "test"), gif=True)

    google_image_query_url = (
        f"https://www.googleapis.com/customsearch/v1?"
        f"key={os.getenv('GOOGLE_CUSTOM_SEARCH_API_TOKEN')}&"
        f"cx={os.getenv('GOOGLE_CUSTOM_SEARCH_API_ID')}&"
        f"q={'this is a test'}&"
        f"searchType=image&"
        f"fileType=gif"
    )
    if not query == google_image_query_url:
        raise AssertionError()


def test_create_discord_file_object():
    """Test create discord file object"""
    img_link = 'https://media.discordapp.net/attachments/615527031148642334/627764848821796864/tano.png'
    discord_file = create_discord_file_object(img_link)

    assert type(discord_file) is File
    assert 'SPOILER_' not in discord_file.filename


def test_create_discord_file_object_as_spoiler():
    """Test create discord file object"""
    img_link = 'https://media.discordapp.net/attachments/615527031148642334/627764848821796864/tano.png'
    discord_file = create_discord_file_object(img_link, '--spoiler')

    assert type(discord_file) is File
    assert 'SPOILER_' in discord_file.filename
