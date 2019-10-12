from commands.misc import ping, banner

import pytest
from asyncmock import AsyncMock


@pytest.fixture
def ctx():
    ctx = AsyncMock()
    return ctx


@pytest.mark.asyncio
async def test_ping(ctx):
    await ping(ctx)
    ctx.send.assert_called_with("pong")


@pytest.mark.asyncio
async def test_ping_with_mention(ctx):
    await ping(ctx, arg="ab")
    ctx.send.assert_called_with("Pinging Don't be evil. 🏓")


@pytest.mark.asyncio
async def test_banner(ctx):
    expected_art_string = "```    _    \r\n   / \\   \r\n  / _ \\  \r\n / ___ \\ \r\n/_/   \\_\\\r\n         \r\n```"  # text2art("A")
    await banner(ctx, "A")
    ctx.send.assert_called_with(expected_art_string)


@pytest.mark.asyncio
async def test_banner_with_more_than_20_chars(ctx):
    long_string = "A" * 21
    await banner(ctx, long_string)
    ctx.send.assert_called_with("Diminue esse textão aí, pfv.")
