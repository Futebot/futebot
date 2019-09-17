import os

from ...util.helpers import generate_image_search_url


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