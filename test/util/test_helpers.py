import os
from unittest.mock import MagicMock

import pytest
from discord import File

from util.helpers import (
    create_discord_file_object,
    generate_image_search_url,
    get_json_field_from_url,
    get_json_fields_from_url,
    mention,
    validate_image,
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
    assert query == google_image_query_url


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
    assert query == google_image_query_url


def test_create_discord_file_object():
    """Test create discord file object"""
    img_link = "https://media.discordapp.net/attachments/615527031148642334/627764848821796864/tano.png"
    image_is_valid, file_bytes = validate_image(img_link)
    discord_file = create_discord_file_object(file_bytes, ".jpg")

    assert type(discord_file) is File
    assert "SPOILER_" not in discord_file.filename


def test_create_discord_file_object_as_spoiler():
    """Test create discord file object"""
    img_link = "https://media.discordapp.net/attachments/615527031148642334/627764848821796864/tano.png"
    spoiler = True
    image_is_valid, file_bytes = validate_image(img_link)
    discord_file = create_discord_file_object(file_bytes, ".jpg",  "--spoiler")

    assert type(discord_file) is File
    assert "SPOILER_" in discord_file.filename


def test_get_json_fields_from_url():
    """Test get json fields from url"""
    expected_json_data = [
        {
            "id": 1,
            "name": "cerulean",
            "year": 2000,
            "color": "#98B2D1",
            "pantone_value": "15-4020",
        }
    ]

    json_data = get_json_fields_from_url("https://reqres.in/api/products/1", "data")
    assert expected_json_data == json_data


def test_get_json_field_from_url():
    """Test get json field from url"""
    expected_json_data = {
        "id": 1,
        "name": "cerulean",
        "year": 2000,
        "color": "#98B2D1",
        "pantone_value": "15-4020",
    }

    assert expected_json_data == get_json_field_from_url(
        "https://reqres.in/api/products/1", "data"
    )


def test_get_json_fields_from_url_failing():
    """Test failling get json fields from url"""
    with pytest.raises(Exception) as e:
        assert get_json_fields_from_url()


@pytest.fixture
def ctx_object():
    """Fixture to mock discord context objects"""
    ctx = MagicMock()
    member_1 = MagicMock()
    member_2 = MagicMock()
    member_1.name = "abc"
    member_2.name = "def"
    member_1.mention = "@abc"
    member_2.mention = "@def"
    ctx.message.channel.members = [member_1, member_2]
    return ctx


def test_mention_less_than_3_chars(ctx_object):
    """Test mention with less than 3 chars"""
    expected_result = "Don't be evil."
    criteria = "ab"
    assert mention(ctx_object, criteria) == expected_result


def test_mention(ctx_object):
    """Test mention using magic mock object"""
    assert mention(ctx_object, "def") == "@def "
