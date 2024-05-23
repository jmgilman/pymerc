from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pymerc.api.models import common
from pymerc.game.exports import Export, Exports
from pymerc.game.imports import Import, Imports

if TYPE_CHECKING:
    from pymerc.client import Client


class Transport:
    """A higher level representation of a transport in the game."""

    exports: Exports
    id: int
    imports: Imports

    def __init__(self, client: Client, id: int):
        self._client = client
        self.id = id
        self.exports = Exports()
        self.imports = Imports()

    async def load(self):
        """Loads the data for the transport."""
        self.data = await self._client.transports_api.get(self.id)
        await self._load_imports_exports()

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
        if self.data.route:
            town = await self._client.town(self.data.route.remote_town)
            for item, manager in self.route.managers.items():
                asset = self.route.account.assets[item]
                flow = self.data.route.current_flows[item]
                if manager.buy_volume:
                    self.imports[item] = Import(asset, flow, manager, town, self)
                if manager.sell_volume:
                    self.exports[item] = Export(asset, flow, manager, town, self)
