import os
import shlex
import slack
from commands.context import Context
from commands.custom import c
from commands.utils import prefix
from service.command_suggestion_service import get_suggested_command
from util.commands import Commands

slack_client = slack.WebClient(token=os.getenv('SLACK_TOKEN'))


def find_command(context, command):
    command_prefix = command
    command_params = None
    try:
        command_prefix = command.split(' ')[0].split('\n')[0]
        command_params = command.split(' ', 1)[1]
        command_params = shlex.split(command_params)
    except:
        command_params = None

    # Validating and correting command
    command_prefix = get_suggested_command(command_prefix)
    try:
        func = Commands.get_instance().dictionary[command_prefix]['func']
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


def handle_command(command, channel, user, timestamp):
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
            slack_client.chat_postMessage(
                channel=channel,
                text=response
            )
    except Exception as e:
        error_response = "Ouch! It hurts, but I will recover."
        slack_client.chat_postMessage(
            channel=channel,
            text=error_response
        )
        print(e)


@slack.RTMClient.run_on(event='message')
def on_message(**payload):
    data = payload['data']
    if data['text'].startswith(prefix):
        handle_command(data['text'].replace(prefix, ''), data['channel'], data['user'], data['ts'])


rtm_client = slack.RTMClient(token=os.getenv('SLACK_TOKEN'))
rtm_client.start()
