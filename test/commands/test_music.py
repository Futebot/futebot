from commands.music import musica

import pytest
from asyncmock import AsyncMock


@pytest.fixture
def ctx():
    ctx = AsyncMock()
    return ctx


@pytest.mark.asyncio
async def test_track_search(ctx):
    track_name = "Monday Morning Girl"
    expected_result = "https://open.spotify.com/track/6mtmLr1GdrTyrL9lvUKiFv"

    await musica(ctx, track_name)
    ctx.send.assert_called_with(expected_result)
