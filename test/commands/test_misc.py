import pytest
from commands.misc import ping
from asyncmock import AsyncMock


@pytest.mark.asyncio
async def test_ping():
    ctx = AsyncMock()
    await ping(ctx)
    ctx.send.assert_called_with("pong")
