import pytest

@pytest.mark.asyncio
async def test_get_buildings(client):
    buildings = await client.static.get_buildings()
    assert len(buildings) > 0

@pytest.mark.asyncio
async def test_get_items(client):
    items = await client.static.get_items()
    assert len(items) > 0

@pytest.mark.asyncio
async def test_get_recipes(client):
    recipes = await client.static.get_recipes()
    assert len(recipes) > 0

@pytest.mark.asyncio
async def test_get_transport(client):
    transport = await client.static.get_transport()
    assert len(transport) > 0