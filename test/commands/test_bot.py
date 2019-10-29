from commands.bot import listall

import pytest
from asyncmock import AsyncMock


@pytest.fixture
def ctx():
    ctx = AsyncMock()
    return ctx


@pytest.mark.asyncio
async def test_listall(ctx):
    await listall(ctx)
    ctx.author.send.assert_called()


@pytest.mark.asyncio
async def test_listall_grep(ctx):
    await listall(ctx, "test")
    ctx.author.send.assert_called()


@pytest.mark.asyncio
async def test_listall_grep_value(ctx):
    await listall(ctx, "decide")
    assert ctx.author.send.call_args[1]['embed'].title == "Commands list"
    assert ctx.author.send.call_args[1]['embed'].fields[0].name == ".decide "
