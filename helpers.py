import os

RANDOM_EXCEPTION_COMEBACKS = [
    "Are you dumb?",
    "No, I don't think I will."
]


def generate_image_search_url(search_terms, **kwargs):
    search_terms = ' '.join(search_terms)

    google_image_query_url = (
        f"https://www.googleapis.com/customsearch/v1?"
        f"key={os.environ['GOOGLE_CUSTOM_SEARCH_API_TOKEN']}&"
        f"cx={os.environ['GOOGLE_CUSTOM_SEARCH_API_ID']}&"
        f"q={search_terms}&"
        f"searchType=image")

    if kwargs.get('gif', None):
        return google_image_query_url + "&fileType=gif"

    return google_image_query_url
