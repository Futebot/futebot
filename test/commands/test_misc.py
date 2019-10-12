from commands.misc import ping

import pytest
from asyncmock import AsyncMock


@pytest.mark.asyncio
async def test_ping():
    ctx = AsyncMock()
    await ping(ctx)
    ctx.send.assert_called_with("pong")


@pytest.mark.asyncio
async def test_ping_with_mention():
    ctx = AsyncMock()
    await ping(ctx, arg="ab")
    ctx.send.assert_called_with("Pinging Don't be evil. 🏓")
