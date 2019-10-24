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
