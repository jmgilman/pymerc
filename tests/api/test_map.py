import pytest

from pymerc.client import Client


@pytest.mark.asyncio
async def test_all(client: Client):
    response = await client.map.get_all()
    assert len(response) > 0
