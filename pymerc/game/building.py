from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pymerc.api.models import common

if TYPE_CHECKING:
    from pymerc.client import Client


class Building:
    """A higher level representation of a building in the game."""

    def __init__(self, client: Client, id: int):
        self._client = client
        self.id = id

    async def load(self):
        """Loads the data for the building."""
        self.data = await self._client.buildings_api.get(self.id)

    @property
    def flows(self) -> Optional[dict[common.Item, common.InventoryFlow]]:
        """The flows of the building."""
        if self.data.storage:
            return self.data.storage.inventory.previous_flows
        else:
            return None

    @property
    def inventory(self) -> Optional[common.Inventory]:
        """The inventory of the building."""
        return self.data.storage.inventory

    @property
    def items(self) -> Optional[dict[str, common.InventoryAccountAsset]]:
        """The items in the building's storage."""
        if self.data.storage:
            return self.data.storage.inventory.account.assets
        else:
            return None

    @property
    def managers(self) -> list[common.InventoryManager]:
        """The managers of the building."""
        return self.data.storage.inventory.managers

    @property
    def production(self) -> Optional[common.Producer]:
        """The production of the building."""
        return self.data.producer

    @property
    def production_flows(self) -> Optional[dict[common.Item, common.InventoryFlow]]:
        """The production flows of the building."""
        if self.data.producer:
            return self.data.producer.inventory.previous_flows
        else:
            return None

    @property
    def size(self) -> Optional[int]:
        """The size of the building."""
        return self.data.size

    @property
    def type(self) -> common.BuildingType:
        """The type of the building."""
        return self.data.type

    @property
    def under_construction(self) -> bool:
        """Whether the building is under construction."""
        return self.data.construction is not None

    @property
    def upgrades(self) -> Optional[list[common.BuildingUpgradeType]]:
        """The upgrades installed for the building."""
        return self.data.upgrades

    def flow(self, item: common.Item) -> Optional[common.InventoryFlow]:
        """Get the flow of an item in the building.

        Args:
            item (Item): The item.

        Returns:
            Optional[InventoryFlow]: The flow of the item, if it exists.
        """
        if self.data.storage:
            return self.data.storage.inventory.previous_flows.get(item, None)
        else:
            return None

    def item(self, item: common.Item) -> Optional[common.InventoryAccountAsset]:
        """Get an item in the building.

        Args:
            item (Item): The item.

        Returns:
            Optional[InventoryAccountAsset]: The item, if it exists.
        """
        if self.data.storage:
            return self.data.storage.inventory.account.assets.get(item, None)
        else:
            return None

    def manager(self, item: common.Item) -> Optional[common.InventoryManager]:
        """Get the manager of an item in the building.

        Args:
            item (Item): The item.

        Returns:
            Optional[InventoryManager]: The manager of the item, if it exists.
        """
        if self.data.storage:
            return self.data.storage.inventory.managers.get(item, None)
        else:
            return None

    def set_manager(self, item: common.Item, manager: common.InventoryManager) -> bool:
        """Set the manager for an item in the building.

        Args:
            item (Item): The item.
            manager (InventoryManager): The manager.

        Returns:
            bool: Whether the manager was set.
        """
        return self._client.buildings_api.set_manager(self.id, item, manager)