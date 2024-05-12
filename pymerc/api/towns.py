from typing import Optional

from loguru import logger
from pydantic import TypeAdapter

from pymerc.api.base import BaseAPI
from pymerc.api.models import towns

BASE_URL = "https://play.mercatorio.io/api/towns"

class TownsAPI(BaseAPI):
    """A class for interacting with the towns API endpoint."""

    async def init_cache(self):
        pass

    async def all(self) -> list[towns.Town]:
        """Get a list of all towns in the game."""
        adapter = TypeAdapter(list[towns.Town])
        response = await self.client.get(BASE_URL)
        return adapter.validate_python(response.json())

    async def data(self, id) -> towns.TownData:
        """Get data for a town.

        Args:
            id (int): The ID of the town

        Returns:
            TownData: The data for the town
        """
        response = await self.client.get(f"{BASE_URL}/{id}")
        return towns.TownData.model_validate(response.json())

    async def marketdata(self, id) -> dict[str, towns.MarketItemData]:
        """Get market data for a town.

        Args:
            id (int): The ID of the town

        Returns:
            MarketData: The market data for the town
        """
        adapter = TypeAdapter(dict[str, towns.MarketItemData])
        response = await self.client.get(f"{BASE_URL}/{id}/marketdata")
        return adapter.validate_python(response.json())

    async def get_market_item_overview(
        self, town_id, item
    ) -> Optional[towns.MarketItemDataDetails]:
        """Get the market overview for an item in a town.

        Args:
            town_id (int): The ID of the town
            item (str): The item to get the overview for

        Returns:
            MarketItemDataDetails: The market overview for the town
        """
        response = await self.client.get(f"{BASE_URL}/{town_id}/markets/{item}")
        return towns.MarketItemDataDetails.model_validate(response.json())
