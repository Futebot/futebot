import os

from service.command_suggestion_service import get_custom_dict, get_command, is_custom_command


def test_get_custom_dict():
    os.environ["COMMANDS_DATA_FILE"] = os.path.dirname(os.path.abspath(__file__))+"/data_test.yml"
    data = get_custom_dict()
    assert data['test'] == "hi"


def test_is_custom_command():
    os.environ["COMMANDS_DATA_FILE"] = os.path.dirname(os.path.abspath(__file__))+"/data_test.yml"
    assert is_custom_command("another") is True
    assert is_custom_command("nothere") is False


def test_get_custom_dict():
    os.environ["COMMANDS_DATA_FILE"] = os.path.dirname(os.path.abspath(__file__))+"/data_test.yml"
    command = get_command("anther")
    assert command[1] == "another"
