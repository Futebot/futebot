import os
import random
import time
import re
import urllib

import requests
from art import text2art
from slackclient import SlackClient
# instantiate Slack client
from commands.config import HOROSCOPO_ENDPOINT, COACH_ENDPOINT, WEATHER_ENDPOINT, YT_RESULTS_ENDPOINT, \
    YT_WATCH_ENDPOINT, LMGTFY_ENDPOINT
from commands.games import roll, charada
from commands.hope import coach, horoscopo, decide
from commands.meme import book, soniko, gordo, feijoada, tano, antagonista, tomacu, speech
from commands.misc import scroll, banner
from commands.search import youtube, weather, gifme, imgme, lmgtfy
from service import roll_service
from service.img_card_service import generate_card
from util.helpers import get_json_field_from_url, generate_image_search_url, validate_image, get_weather_icon, \
    format_string_to_query

slack_client = SlackClient('xoxb-890869960082-903310164100-61zcMRVqtpIjTHMPvxjCHYov')
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None
# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
rec = ["Are you dumb?", "No, I don't think I will."]


HOROSCOPO_COMMAND = "horoscopo"
COACH_COMMAND = "coach"
BANNER_COMMAND = "banner"
SCROLL_COMMAND = "scroll"
ROLL_COMMAND = 'roll'
IMG_COMMAND = 'imgme'
GIF_COMMAND = 'gifme'
YOUTUBE_COMMAND = 'youtube'
LMGTFY_COMMAND = 'lmgtfy'
WEATHER_COMMAND = 'weather'
SPEECH_COMMAND = 'speech'
BOOK_COMMAND = 'book'
SONIKO_COMMAND = 'soniko'
GORDO_COMMAND = 'gordo'
FEIJOADA_COMMAND = 'feijoada'
TANO_COMMAND = 'tano'
ANTAGONISTA_COMMAND = 'antagonista'
TOMACU_COMMAND = 'tomacu'
CHARADA_COMMAND = 'charada'
DECIDE_COMMAND = 'decide'

MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if event['text'].startswith('.'):
                handle_command(event['text'].replace('.', ''), event['channel'])

    return None, None


def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)


def find_command(command):
    command_params = ''
    try:
        command_params = command.split(' ', 1)[1]
    except:
        command_params = ''

    if command.startswith(HOROSCOPO_COMMAND):
        return horoscopo(command_params)

    if command.startswith(COACH_COMMAND):
        return coach()

    if command.startswith(BANNER_COMMAND):
        return banner(command_params)

    if command.startswith(SCROLL_COMMAND):
        return scroll()

    if command.startswith(ROLL_COMMAND):
        return roll(command_params)

    if command.startswith(IMG_COMMAND):
        return imgme(command_params)

    if command.startswith(GIF_COMMAND):
        return gifme(command_params)

    if command.startswith(WEATHER_COMMAND):
        return weather(command_params)

    if command.startswith(YOUTUBE_COMMAND):
        return youtube(command_params)

    if command.startswith(LMGTFY_COMMAND):
        return lmgtfy(command_params)

    if command.startswith(SPEECH_COMMAND):
        return speech(command_params)

    if command.startswith(BOOK_COMMAND):
        return book(command_params)

    if command.startswith(SONIKO_COMMAND):
        return soniko(command_params)

    if command.startswith(GORDO_COMMAND):
        return gordo(command_params)

    if command.startswith(FEIJOADA_COMMAND):
        return feijoada(command_params)

    if command.startswith(TANO_COMMAND):
        return tano(command_params)

    if command.startswith(ANTAGONISTA_COMMAND):
        return antagonista(command_params)

    if command.startswith(TOMACU_COMMAND):
        return tomacu(command_params)

    if command.startswith(CHARADA_COMMAND):
        return charada()

    if command.startswith(DECIDE_COMMAND):
        return decide(command_params)

    return None


def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "Not sure what you mean. Try to be smarter."
    # Finds and executes the given command, filling in response
    response = None
    response = find_command(command)

    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
