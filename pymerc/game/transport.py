from __future__ import annotations

from typing import TYPE_CHECKING

from pymerc.api.models.common import Item, Inventory

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
    def inventory(self) -> Inventory:
        """Returns the inventory of the transport."""
        return self.data.inventory

    @property
    def route(self) -> Inventory:
        """Returns the route of the transport."""
        return self.data.route

    def get_exports(self) -> list[Item]:
        """Get the exports of the transport.

        Returns:
            List[item]: The exports of the transport.
        """
        exports = []
        for item, data in self.data.route.managers.items():
            if data.sell_price:
                exports.append(item)

        return exports

    def get_active_exports(self) -> list[Item]:
        """Get the exports of the transport that traded in the last turn.

        Returns:
            list[Item]: The exports of the transport that traded in the last turn.
        """
        exports = []
        for item, asset in self.data.route.account.assets.items():
            if asset.sale and asset.sale_price:
                exports.append(item)

        return exports

    def get_imports(self) -> list[Item]:
        """Get the imports of the transport.

        Returns:
            list[Item]: The imports of the transport.
        """
        imports = []
        for item, data in self.data.route.managers.items():
            if data.buy_price:
                imports.append(item)

        return imports

    def get_active_imports(self) -> list[Item]:
        """Get the imports of the transport that traded in the last turn.

        Returns:
            list[Item]: The imports of the transport that traded in the last turn.
        """
        imports = []
        for item, asset in self.data.route.account.assets.items():
            if asset.purchase and asset.purchase_price:
                imports.append(item)

        return imports