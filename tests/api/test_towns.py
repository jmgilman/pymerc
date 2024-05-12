import pytest

@pytest.mark.asyncio
async def test_all(client):
    towns = await client.towns.all()
    assert len(towns) > 0

@pytest.mark.asyncio
async def test_data(subtests, client):
    towns = await client.towns.all()
    for town in towns:
        with subtests.test(f"Testing data for town {town.name}", i=town.id):
            data = await client.towns.data(town.id)
            assert data is not None

@pytest.mark.asyncio
async def test_marketdata(subtests, client):
    towns = await client.towns.all()
    for town in towns:
        with subtests.test(f"Testing data for town {town.name}", i=town.id):
            data = await client.towns.marketdata(town.id)
            assert data is not None

@pytest.mark.asyncio
async def test_get_market_item_overview(subtests, client):
    towns = await client.towns.all()
    for town in towns:
        with subtests.test(f"Testing data for town {town.name}", i=town.id):
            data = await client.towns.get_market_item_overview(town.id, "arms")
            assert data is not None