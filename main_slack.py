import os
import random
import shlex
import time
import re
import urllib

import requests
from art import text2art
from slackclient import SlackClient
# instantiate Slack client
from commands.config import HOROSCOPO_ENDPOINT, COACH_ENDPOINT, WEATHER_ENDPOINT, YT_RESULTS_ENDPOINT, \
    YT_WATCH_ENDPOINT, LMGTFY_ENDPOINT
from commands.custom import c
from commands.games import roll, charada
from commands.hope import coach, horoscopo, decide
from commands.meme import book, soniko, gordo, feijoada, tano, antagonista, tomacu, speech
from commands.misc import scroll, banner
from commands.search import youtube, weather, gifme, imgme, lmgtfy
from util.commands import Commands

slack_client = SlackClient(os.getenv('SLACK_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None
# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM


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
    command = command.replace(".", "")
    print(command)

    command_prefix = command
    command_params = None
    try:
        command_prefix = command.split(' ')[0]
        command_params = command.split(' ', 1)[1]
        command_params = shlex.split(command_params)
    except:
        command_params = None

    func = Commands.get_instance().dictionary[command_prefix]['func']
    # params = Commands.get_instance().dictionary[command_prefix]['params']
    if func is not None:
        if command_params is None:
            return func()
        elif len(command_params) == 1:
            return func(command_params[0])
        elif len(command_params) == 2:
            return func(command_params[0], command_params[1])
        elif len(command_params) == 3:
            return func(command_params[0], command_params[1], command_params[2])
    else:
        return c(command_params[0])



def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """

    try:

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
    except Exception as e:
        error_response = "Ouch! It hurts, but I will recover."
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=error_response
        )
        print(e)


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
