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
    def items(self) -> Optional[dict[str, common.InventoryAccountAsset]]:
        """Returns the items in the building's storage."""
        if self.data.storage:
            return self.data.storage.inventory.account.assets
        else:
            return None

    @property
    def production(self) -> Optional[common.Producer]:
        """Returns the production of the building."""
        return self.data.producer

    @property
    def production_flows(self) -> Optional[dict[common.Item, common.InventoryFlow]]:
        """Returns the production flows of the building."""
        if self.data.producer:
            return self.data.producer.inventory.previous_flows
        else:
            return None

    @property
    def size(self) -> Optional[int]:
        """Returns the size of the building."""
        return self.data.size

    @property
    def type(self) -> common.BuildingType:
        """Returns the type of the building."""
        return self.data.type

    @property
    def under_construction(self) -> bool:
        """Returns whether the building is under construction."""
        return self.data.construction is not None

    @property
    def upgrades(self) -> Optional[list[common.BuildingUpgradeType]]:
        """Returns the upgrades installed for the building."""
        return self.data.upgrades