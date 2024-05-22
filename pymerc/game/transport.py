from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pymerc.api.models import common

if TYPE_CHECKING:
    from pymerc.client import Client

class Transport:
    """A higher level representation of a transport in the game."""

    def __init__(self, client: Client, id: int):
        self._client = client
        self.id = id

    async def load(self):
        """Loads the data for the transport."""
        self.data = await self._client.transports_api.get(self.id)

    @property
    def exports(self) -> list[common.Item]:
        """The exports of the transport.

        Returns:
            List[item]: The exports of the transport.
        """
        exports = []
        for item, data in self.data.route.managers.items():
            if data.sell_price:
                exports.append(item)

        return exports

    @property
    def active_exports(self) -> list[common.Item]:
        """The exports of the transport that traded in the last turn.

        Returns:
            list[Item]: The exports of the transport that traded in the last turn.
        """
        exports = []
        for item, asset in self.data.route.account.assets.items():
            if asset.sale and asset.sale_price:
                exports.append(item)

        return exports

    @property
    def imports(self) -> list[common.Item]:
        """The imports of the transport.

        Returns:
            list[Item]: The imports of the transport.
        """
        imports = []
        for item, data in self.data.route.managers.items():
            if data.buy_price:
                imports.append(item)

        return imports

    @property
    def active_imports(self) -> list[common.Item]:
        """The imports of the transport that traded in the last turn.

        Returns:
            list[Item]: The imports of the transport that traded in the last turn.
        """
        imports = []
        for item, asset in self.data.route.account.assets.items():
            if asset.purchase and asset.purchase_price:
                imports.append(item)

        return imports

    @property
    def inventory(self) -> common.Inventory:
        """The inventory of the transport."""
        return self.data.inventory

    @property
    def route(self) -> common.Inventory:
        """The route of the transport."""
        return self.data.route

    def exported(self, item: common.Item) -> bool:
        """Returns whether the transport exported the item in the last turn.

        Args:
            item (Item): The item to check.

        Returns:
            bool: Whether the transport exported the item in the last turn.
        """
        return item in self.active_exports

    def imported(self, item: common.Item) -> bool:
        """Returns whether the transport imported the item in the last turn.

        Args:
            item (Item): The item to check.

        Returns:
            bool: Whether the transport imported the item in the last turn.
        """
        return item in self.active_imports

    def route_item(self, item: common.Item) -> Optional[common.InventoryAccountAsset]:
        """Returns the route data for the item, if it exists.

        Args:
            item (Item): The item to get the route data for.

        Returns:
            dict: The route data for the item, if it exists.
        """
        return self.data.route.account.assets.get(item, None)