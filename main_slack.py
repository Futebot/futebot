import os
import time
import re

from art import text2art
from slackclient import SlackClient
# instantiate Slack client
from commands.config import HOROSCOPO_ENDPOINT, COACH_ENDPOINT
from service import roll_service
from util.helpers import get_json_field_from_url

slack_client = SlackClient('xoxb-890869960082-903310164100-YKEx5OuEGG9WkbEygL3tLrCh')
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None
# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM


HOROSCOPO_COMMAND = "horoscopo"
COACH_COMMAND = "coach"
BANNER_COMMAND = "banner"
SCROLL_COMMAND = "scroll"
ROLL_COMMAND = 'roll'

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


def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "Not sure what you mean. Try to be smarter."
    # Finds and executes the given command, filling in response
    response = None
    # This is where you start to implement more commands!
    if command.startswith(HOROSCOPO_COMMAND):
        response = get_json_field_from_url(
            HOROSCOPO_ENDPOINT.format(command.split()[1]), "texto"
        )

    if command.startswith(COACH_COMMAND):
        response = get_json_field_from_url(
            COACH_ENDPOINT,
            "quoteText",
        )

    if command.startswith(BANNER_COMMAND):
        response = '```' + text2art(command.split(' ', 1)[1]) + '```'

    if command.startswith(SCROLL_COMMAND):
        dump = ".\n" * 100
        response = "eita fdp\n" + dump + "vou chamar o marreta :hammer:"

    if command.startswith(ROLL_COMMAND):
        response = roll_service.roll(command.split(' ', 1)[1])

    # Sends the response back to the channel
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
