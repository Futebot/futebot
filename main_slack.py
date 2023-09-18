import os
import shlex
import slack
from commands.context import Context
from commands.custom import c
from commands.utils import prefix
from service.command_suggestion_service import get_suggested_command
from util.commands import Commands
from dotenv import load_dotenv


load_dotenv()

from slack_sdk.rtm import RTMClient


def find_command(context, command):
    command_prefix = command
    command_params = None
    try:
        command_prefix = command.split(" ")[0].split("\n")[0]
        command_params = command.split(" ", 1)[1]
        command_params = shlex.split(command_params)
    except:
        command_params = None

    # Validating and correting command
    command_prefix = get_suggested_command(command_prefix)
    try:
        func = Commands.get_instance().dictionary[command_prefix]["func"]
        # params = Commands.get_instance().dictionary[command_prefix]['params']
        if func is not None:
            if command_params is None:
                return func(context)
            else:
                print(command_params)
                return func(context, command_params)
    except Exception as e:
        print(e)
        try:
            return c(context, command_prefix)
        except:
            return None


def handle_command(command, channel, user, timestamp, web_client):
    """
    Executes bot command if the command is known
    """

    try:
        context = Context()
        context.channel = channel
        context.user = user
        context.timestamp = timestamp

        response = None
        response = find_command(context, command)

        if response is not None:
            web_client.chat_postMessage(channel=channel, link_names=1, text=response)
    except Exception as e:
        error_response = "Ouch! It hurts, but I will recover."
        web_client.chat_postMessage(channel=channel, text=error_response)
        print(e)


# This event runs when the connection is established and shows some connection info
@RTMClient.run_on(event="open")
def show_start(**payload):
    print(payload)


@RTMClient.run_on(event="message")
def say_hello(**payload):
    print(payload)
    data = payload["data"]
    web_client = payload["web_client"]
    if data["text"].startswith(prefix):
        channel_id = data["channel"]
        thread_ts = data["ts"]
        user = data["user"]

        handle_command(data["text"], channel_id, user, thread_ts, web_client)

        # web_client.chat_postMessage(
        #     channel=channel_id, text=f"Hi <@{user}>!", thread_ts=thread_ts
        # )


if __name__ == "__main__":
    slack_token = os.getenv("SLACK_TOKEN")
    rtm_client = RTMClient(token=slack_token)
    rtm_client.start()

# slack_client = slack.WebClient(token=os.getenv('SLACK_TOKEN'))


# @slack.RTMClient.run_on(event='message')
# def on_message(**payload):
#     data = payload['data']
#     if data['text'].startswith(prefix):
#         handle_command(data['text'].replace(prefix, '', 1), data['channel'], data['user'], data['ts'])


# rtm_client = slack.RTMClient(token=os.getenv('SLACK_TOKEN'), connect_method='rtm.connect')
# rtm_client.start()
