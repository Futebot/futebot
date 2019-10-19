from commands.hope import coach, horoscopo, decide

import pytest
from asyncmock import AsyncMock


@pytest.fixture
def ctx():
    ctx = AsyncMock()
    return ctx


@pytest.mark.asyncio
async def test_coach(ctx):
    await coach(ctx)
    ctx.send.assert_called()


@pytest.mark.asyncio
async def test_horoscopo(ctx):
    await horoscopo(ctx, "sagitário")
    ctx.send.assert_called()


@pytest.mark.asyncio
async def test_decide(ctx):
    await decide(ctx, "Yes or no?")
    ctx.send.assert_called()
