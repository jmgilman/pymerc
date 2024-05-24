from __future__ import annotations

from collections import UserList
from typing import TYPE_CHECKING, Optional

from pymerc.api.models import common
from pymerc.api.models.towns import TownMarketItemDetails
from pymerc.game.exports import Export, Exports
from pymerc.game.imports import Import, Imports
from pymerc.game.town import Town

if TYPE_CHECKING:
    from pymerc.client import Client


class Transport:
    """A higher level representation of a transport in the game."""

    exports: Exports
    id: int
    imports: Imports
    town: Optional[Town]

    def __init__(self, client: Client, id: int):
        self._client = client
        self.id = id
        self.exports = Exports()
        self.imports = Imports()
        self.town = None

    async def load(self):
        """Loads the data for the transport."""
        self.data = await self._client.transports_api.get(self.id)
        if self.data.route:
            self.town = await self._client.town(self.data.route.remote_town)

        await self._load_imports_exports()

    @property
    def docked(self) -> bool:
        """Whether the transport is docked."""
        return self.town is not None

    @property
    def inventory(self) -> common.Inventory:
        """The inventory of the transport."""
        return self.data.inventory

    @property
    def route(self) -> common.Inventory:
        """The route of the transport."""
        return self.data.route

    def route_item(self, item: common.Item) -> Optional[common.InventoryAccountAsset]:
        """Returns the route data for the item, if it exists.

        Args:
            item (Item): The item to get the route data for.

        Returns:
            dict: The route data for the item, if it exists.
        """
        return self.data.route.account.assets.get(item, None)

    async def _load_imports_exports(self):
        """Loads the imports and exports for the transport."""
        if self.docked:
            for item, manager in self.route.managers.items():
                asset = self.route.account.assets[item]
                flow = self.data.route.current_flows[item]
                if manager.buy_volume:
                    self.imports[item] = Import(asset, flow, manager, self.town, self)
                if manager.sell_volume:
                    self.exports[item] = Export(asset, flow, manager, self.town, self)


class TransportList(UserList[Transport]):
    """A list of transports."""

    def search_markets(self, item: common.Item) -> list[TownItem]:
        """Searches the markets for the item.

        Args:
            item (Item): The item to search for.

        Returns:
            list: A list of the markets for the item.
        """
        items = []
        for transport in self:
            if transport.docked:
                if item in transport.town.market:
                    items.append(
                        TownItem(item, transport.town.market[item], transport.town)
                    )
        return items


class TownItem:
    """Represents an item in a town."""

    def __init__(
        self, item: common.Item, asset: common.InventoryAccountAsset, town: Town
    ):
        self.item = item
        self.asset = asset
        self.town = town

    def fetch_details(self) -> TownMarketItemDetails:
        """Fetches the details for the item from the town's market."""
        return self.town.fetch_market_item(self.item)
