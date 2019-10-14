from commands.misc import ping, banner, moji

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
    expected_art_string = (
        "```    _    \r\n   / \\   \r\n  / _ \\  \r\n / ___ \\ \r\n/_/   \\_\\\r\n         \r\n```")
    await banner(ctx, "A")
    ctx.send.assert_called_with(expected_art_string)


@pytest.mark.asyncio
async def test_banner_with_more_than_20_chars(ctx):
    long_string = "A" * 21
    await banner(ctx, long_string)
    ctx.send.assert_called_with("Diminue esse textão aí, pfv.")


@pytest.mark.asyncio
async def test_moji(ctx):
    expected_art_string = "¯\\_(ツ)_/¯ "
    await moji(ctx, "shrug")
    ctx.send.assert_called_with(expected_art_string)


@pytest.mark.asyncio
async def test_moji_failing(ctx):
    expected_str = (
        "Tenta esses moji aqui, fera: https://github.com/sepandhaghighi/art/blob/master/art/art_dic.py")
    await moji(ctx, "HUEHUEHUE")
    ctx.send.assert_called_with(expected_str)
