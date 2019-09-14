import os

import pytest

from ...util.helpers import generate_image_search_url


def test_generate_image_search_url():
    """Test url generator for google image queries"""
    query = generate_image_search_url(("this", "is", "a", "test"))

    google_image_query_url = (
        f"https://www.googleapis.com/customsearch/v1?"
        f"key={os.environ['GOOGLE_CUSTOM_SEARCH_API_TOKEN']}&"
        f"cx={os.environ['GOOGLE_CUSTOM_SEARCH_API_ID']}&"
        f"q={'this is a test'}&"
        f"searchType=image"
    )
    assert query == google_image_query_url


def test_generate_image_search_url_gif():
    """Test url generator for google gif queries"""
    query = generate_image_search_url(("this", "is", "a", "test"), gif=True)

    google_image_query_url = (
        f"https://www.googleapis.com/customsearch/v1?"
        f"key={os.environ['GOOGLE_CUSTOM_SEARCH_API_TOKEN']}&"
        f"cx={os.environ['GOOGLE_CUSTOM_SEARCH_API_ID']}&"
        f"q={'this is a test'}&"
        f"searchType=image&"
        f"fileType=gif"
    )
    assert query == google_image_query_url

