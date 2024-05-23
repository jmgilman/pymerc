import pytest

from pymerc.client import Client


@pytest.mark.asyncio
async def test_get(subtests, client: Client):
    player = await client.player_api.get()
    business = await client.businesses_api.get(player.household.business_ids[0])
    for transport in business.transport_ids:
        with subtests.test(f"Testing data for transport {transport}", i=transport):
            t = await client.transports_api.get(transport)
            assert t is not None
