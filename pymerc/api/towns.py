from typing import Optional

from pydantic import TypeAdapter

from pymerc.api.base import BaseAPI
from pymerc.api.models import common, towns
from pymerc.util import data

BASE_URL = "https://play.mercatorio.io/api/towns"


class TownsAPI(BaseAPI):
    """A class for interacting with the towns API endpoint."""

    async def init_cache(self):
        pass

    async def get_all(self) -> list[towns.Town]:
        """Get a list of all towns in the game."""
        adapter = TypeAdapter(list[towns.Town])
        response = await self.client.get(BASE_URL)
        return adapter.validate_python(response.json())

    async def get_data(self, id: int) -> towns.TownData:
        """Get data for a town.

        Args:
            id (int): The ID of the town

        Returns:
            TownData: The data for the town
        """
        response = await self.client.get(f"{BASE_URL}/{id}")
        return towns.TownData.model_validate(response.json())

    async def get_market_data(self, id: int) -> towns.TownMarket:
        """Get market data for a town.

        Args:
            id (int): The ID of the town

        Returns:
            TownMarket: The market data for the town
        """
        response = await self.client.get(f"{BASE_URL}/{id}/marketdata")
        return towns.TownMarket.model_validate(response.json())

    async def get_market_item(
        self, town_id: int, item: common.Item
    ) -> Optional[towns.TownMarketItemDetails]:
        """Get the market overview for an item in a town.

        Args:
            town_id (int): The ID of the town
            item (str): The item to get the overview for

        Returns:
            TownMarketItemDetails: The market overview for the town
        """
        response = await self.client.get(f"{BASE_URL}/{town_id}/markets/{item.value}")
        return towns.TownMarketItemDetails.model_validate(response.json())

    async def send_sell_order(
        self,
        item: common.Item,
        id: int,
        expected_balance: int,
        operation: str,
        price: float,
        volume: int,
    ) -> common.ItemTradeResult:
        """Send a sell order to a town.

        Args:
            item (Item): The item to sell
            id (int): The ID of the town
            expected_balance (int): The expected balance after the sale
            operation (str): The operation to use for the sale
            price (float): The price of the item
            volume (int): The volume of the item to sell

        Returns:
            bool: Whether the order was successfully sent
        """
        trade = common.ItemTrade(
            direction="ask",
            expected_balance=expected_balance,
            operation=operation,
            price=price,
            volume=volume,
        )
        json = data.convert_floats_to_strings(trade.model_dump())
        response = await self.client.post(
            f"{BASE_URL}/{id}/markets/{item.value}/orders", json=json
        )

        if response.status_code == 200:
            return common.ItemTradeResult.model_validate(response.json())
        else:
            raise ValueError(f"Failed to send sell order: {response.text}")
