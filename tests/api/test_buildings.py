import pytest

from pymerc.client import Client
from pymerc.api.models.common import BuildingType


@pytest.mark.asyncio
async def test_get(client: Client):
    player = await client.player.get()
    business = await client.businesses.get(player.household.business_ids[0])
    storehouse_id = [
        building.id
        for building in business.buildings
        if building.type == BuildingType.Storehouse
    ][0]
    storehouse = await client.buildings.get(storehouse_id)
    assert storehouse is not None
