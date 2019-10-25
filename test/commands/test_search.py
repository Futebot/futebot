from commands.search import lmgtfy

import pytest
from asyncmock import AsyncMock


@pytest.fixture
def ctx():
    ctx = AsyncMock()
    return ctx


@pytest.mark.asyncio
async def test_lmgtfy(ctx):
    await lmgtfy(ctx, "League of Legends")
    ctx.send.assert_called_with("https://lmgtfy.com/?q=League+of+Legends&s=g&iie=1")
