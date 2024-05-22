from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from pymerc.api.models.common import InventoryAccountAsset, InventoryFlow, InventoryManager, Item

if TYPE_CHECKING:
    from pymerc.client import Client

class Storehouse:
    """A higher level representation of a storehouse in the game."""

    def __init__(self, client: Client, id: int):
        self._client = client
        self.id = id

    async def load(self):
        """Loads the data for the storehouse."""
        self.data = await self._client.building(self.id)

    def get_flow(self, item: Item) -> Optional[InventoryFlow]:
        """Get the flow of an item from the player's storehouse.

        Args:
            item (Item): The item to get.

        Returns:
            Optional[InventoryFlow]: The flow of the item, if it exists.
        """
        return self.data.inventory.previous_flows.get(item, None)

    def get_flows(self) -> list[InventoryFlow]:
        """Get all flows from the player's storehouse.

        Returns:
            list[InventoryFlow]: The flows.
        """
        return self.data.inventory.previous_flows

    def get_item(self, item: Item) -> Optional[InventoryAccountAsset]:
        """Get an item from the player's storehouse.

        Args:
            item (Item): The item to get.

        Returns:
            Optional[InventoryAccountAsset]: The item, if it exists.
        """
        return self.data.inventory.account.assets.get(item, None)

    def get_items(self) -> list[Item]:
        """Get all items from the player's storehouse.

        Returns:
            list[InventoryAccountAsset]: The items.
        """
        return self.data.inventory.account.assets

    def get_manager(self, item: Item) -> Optional[InventoryManager]:
        """Get the manager of an item from the player's storehouse.

        Args:
            item (Item): The item to get.

        Returns:
            Optional[InventoryAccountAsset]: The manager of the item, if it exists.
        """
        return self.data.inventory.managers.get(item, None)

    def get_managers(self) -> list[InventoryManager]:
        """Get all managers from the player's storehouse.

        Returns:
            list[InventoryManager]: The managers.
        """
        return self.data.inventory.managers