import pytest


@pytest.mark.asyncio
async def test_get(client):
    player = await client.player_api.get()
    assert player is not None
