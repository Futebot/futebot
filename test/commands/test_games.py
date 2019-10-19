import pytest
from asyncmock import AsyncMock

from commands.games import roll


@pytest.fixture
def ctx():
    ctx = AsyncMock()
    return ctx


@pytest.mark.asyncio
async def test_roll(ctx):
    await roll(ctx, "1d1")
    ctx.send.assert_called_with("Rolled 1 = 1")


@pytest.mark.asyncio
async def test_roll_invalid(ctx):
    await roll(ctx, "sdds")
    ctx.send.assert_called_with("Are you dumb?")
