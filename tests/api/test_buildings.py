import pytest

from pymerc.client import Client
from pymerc.api.models.common import BuildingType


@pytest.mark.asyncio
async def test_get(subtests, client: Client):
    player = await client.player_api.get()
    business = await client.businesses_api.get(player.household.business_ids[0])
    for building in business.buildings:
        with subtests.test(f"Testing data for building {building.type}", i=building.id):
            b = await client.buildings_api.get(building.id)
            assert b is not None
