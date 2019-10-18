import os

import pytest
from asyncmock import AsyncMock

from commands.custom import listcustom, add, c
from commands.games import roll


@pytest.fixture
def ctx():
    ctx = AsyncMock()
    return ctx


@pytest.mark.asyncio
async def test_list_custom(ctx):
    os.environ["COMMANDS_DATA_FILE"] = os.path.dirname(os.path.abspath(__file__)) + "/../data_test.yml"

    await listcustom(ctx)
    assert ctx.send.call_args[1]['embed'].title == "Custom Commands list"
    assert ctx.send.call_args[1]['embed'].fields[0].name == ".test"
    assert ctx.send.call_args[1]['embed'].fields[1].name == ".another"


@pytest.mark.asyncio
async def test_add(ctx):
    os.environ["COMMANDS_DATA_FILE"] = os.path.dirname(os.path.abspath(__file__)) + "/../data_test_add.yml"

    await add(ctx, "a", "a")
    await c(ctx, "a")
    ctx.send.assert_called_with("a")
