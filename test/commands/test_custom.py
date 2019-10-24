import os

import pytest
from asyncmock import AsyncMock

from commands.custom import listcustom, add, rm, c
from service.command_suggestion_service import is_custom_command


@pytest.fixture
def ctx():
    ctx = AsyncMock()
    return ctx


@pytest.mark.asyncio
async def test_list_custom(ctx):
    os.environ["COMMANDS_DATA_FILE"] = os.path.dirname(os.path.abspath(__file__)) + "/../data_test.yml"

    await listcustom(ctx)
    assert ctx.author.send.call_args[1]['embed'].title == "Custom Commands list"
    assert ctx.author.send.call_args[1]['embed'].fields[0].name == ".another"
    assert ctx.author.send.call_args[1]['embed'].fields[1].name == ".test"


@pytest.mark.asyncio
async def test_add(ctx):
    os.environ["COMMANDS_DATA_FILE"] = os.path.dirname(os.path.abspath(__file__)) + "/../data_test_add.yml"

    await add(ctx, "cmd", "value")
    assert is_custom_command("cmd") is True

    await c(ctx, "cmd")
    ctx.send.assert_called_with("value")

    os.remove(os.environ["COMMANDS_DATA_FILE"])


@pytest.mark.asyncio
async def test_rm(ctx):
    os.environ["COMMANDS_DATA_FILE"] = os.path.dirname(os.path.abspath(__file__)) + "/../data_test_rm.yml"

    await add(ctx, "cmd", "value")
    assert is_custom_command("cmd") is True

    await rm(ctx, "cmd")
    assert is_custom_command("cmd") is False

    os.remove(os.environ["COMMANDS_DATA_FILE"])


@pytest.mark.asyncio
async def test_rm_invalid_arg(ctx):
    os.environ["COMMANDS_DATA_FILE"] = os.path.dirname(os.path.abspath(__file__)) + "/../data_test_rm.yml"

    await add(ctx, "cmd", "value")
    await rm(ctx, "")
    assert str(ctx.send.call_args[0][0]) == "Are you dumb?"

    os.remove(os.environ["COMMANDS_DATA_FILE"])


@pytest.mark.asyncio
async def test_rm_invalid_data(ctx):
    os.environ["COMMANDS_DATA_FILE"] = os.path.dirname(os.path.abspath(__file__)) + "/../data_test_rm.yml"

    await rm(ctx, "cmd")
    ctx.send.assert_called_with("buguei")


@pytest.mark.asyncio
async def test_rm_invalid_cmd(ctx):
    os.environ["COMMANDS_DATA_FILE"] = os.path.dirname(os.path.abspath(__file__)) + "/../data_test_rm.yml"

    await add(ctx, "cmd", "value")
    await rm(ctx, "invalid_cmd")
    ctx.send.assert_called_with("Tem esse comando ai não")

    os.remove(os.environ["COMMANDS_DATA_FILE"])
