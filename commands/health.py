import logging as puts
import random

from annotation.futebot import command
from service import roll_service
from util.helpers import (
    get_json_fields_from_url,
    RANDOM_EXCEPTION_COMEBACKS as rec,
)

from .config import CHARADA_ENDPOINT, COVID_ENDPOINT


@command(name="covid", desc="Sends COVID info", params=["country"])
def covid(ctx, *args):
    country = ' '.join(args[0]).capitalize()

    fields = get_json_fields_from_url(
        COVID_ENDPOINT.format(country),
        "cases",
        "todayCases",
        "deaths",
        "todayDeaths",
    )

    response = "*COVID-19 in {}* \n\n" \
               ":covid: *Cases:* {} - :arrow_up_small: {} today.\n\n" \
               ":skull: *Deaths:* {} - :arrow_up_small: {} today.".format(country, fields[0], fields[1], fields[2], fields[3])

    return response


