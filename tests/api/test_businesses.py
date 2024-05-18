import pytest

from pymerc.client import Client


@pytest.mark.asyncio
async def test_get(client: Client):
    player = await client.player_api.get()
    business = await client.businesses_api.get(player.household.business_ids[0])
    assert business is not None
