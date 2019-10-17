from commands.search import lmgtfy

import pytest
from asyncmock import AsyncMock


@pytest.fixture
def ctx():
    ctx = AsyncMock()
    return ctx


@pytest.mark.asyncio
async def test_lmgtfy(ctx):
    expected_lmgtfy_url = "http://tinyurl.com/yyxa8vpq"
    await lmgtfy(ctx, "bosta")
    ctx.send.assert_called_with("http://tinyurl.com/yyxa8vpq")
