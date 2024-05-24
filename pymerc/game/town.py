from __future__ import annotations

import math
from typing import TYPE_CHECKING, Optional

from pymerc.api.models import common
from pymerc.api.models import towns as models

if TYPE_CHECKING:
    from pymerc.client import Client


class Town:
    """A higher level representation of a town in the game."""

    def __init__(self, client: Client, id: int):
        self._client = client
        self.id = id

    async def load(self):
        """Loads the data for the town."""
        self.data = await self._client.towns_api.get_data(self.id)
        self._market = await self._client.towns_api.get_market_data(self.id)

    @property
    def market(self) -> dict[str, models.TownMarketItem]:
        """The market data for the town."""
        return self._market.markets

    @property
    def name(self) -> str:
        """The name of the town."""
        return self.data.name

    @property
    def structures(self) -> dict[str, models.TownDomainStructure]:
        """The structures in the town."""
        structures = {}
        for domain in self.data.domain.values():
            if domain.structure is not None:
                structures[domain.structure.type] = domain.structure

        return structures

    @property
    def total_satisfaction(self) -> int:
        """The percent satisfaction of the town across all categories."""
        demands = sum(
            [category.products for category in self.data.commoners.sustenance], []
        )
        desire_total = sum(demand.desire for demand in demands)
        result_total = sum(demand.result for demand in demands)

        return math.ceil((result_total / desire_total) * 100)

    @property
    def total_structures(self) -> int:
        """The total number of structures in the town."""
        return len(
            [
                domain
                for domain in self.data.domain.values()
                if domain.structure is not None
            ]
        )

    @property
    def total_taxes(self) -> int:
        """The total taxes collected by the town."""
        return sum(self.data.government.taxes_collected.__dict__.values())

    async def fetch_market_item(
        self, item: common.Item
    ) -> models.TownMarketItemDetails:
        """Fetches the details for a market item.

        Args:
            item (Item): The item to fetch the details for

        Returns:
            TownMarketItemDetails: The details for the item
        """
        return await self._client.towns_api.get_market_item(self.id, item)

    def item(self, item: common.Item) -> Optional[models.TownMarketItem]:
        """Get an item from the market.

        Args:
            item (Item): The item to get

        Returns:
            Optional[TownMarketItem]: The item, if found
        """
        return self._market.markets.get(item)
