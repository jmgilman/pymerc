from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from pymerc.api.models import common
from pymerc.api.models.buildings import Building as BuildingModel

if TYPE_CHECKING:
    from pymerc.client import Client
    from pymerc.game.recipe_manager import RecipeManager


class Building:
    """A higher level representation of a building in the game."""

    def __init__(self, client: Client, id: int):
        self._client = client
        self.id = id
        self.data: Optional[BuildingModel] = None

    async def load(self):
        """Loads the data for the building."""
        self.data = await self._client.buildings_api.get(self.id)

    @property
    def inventory(self) -> Optional[common.Inventory]:
        """Returns the inventory of the building."""
        if self.data and self.data.storage:
            return self.data.storage.inventory
        return None

    @property
    def items(self) -> Optional[dict[common.Item, common.InventoryAccountAsset]]:
        """Returns the items in the building's storage."""
        if self.data and self.data.storage:
            return self.data.storage.inventory.account.assets
        return None

    @property
    def production(self) -> Optional[common.Producer]:
        """Returns the production of the building."""
        return self.data.producer if self.data else None

    @property
    def production_flows(self) -> Optional[dict[common.Item, common.InventoryFlow]]:
        """Returns the production flows of the building."""
        if self.data and self.data.producer:
            return self.data.producer.inventory.previous_flows
        return None

    @property
    def size(self) -> Optional[int]:
        """Returns the size of the building."""
        return self.data.size if self.data else None

    @property
    def target(self) -> Optional[float]:
        """Returns the production target of the building."""
        return self.production.target if self.production and self.production.target else 0.0

    @property
    def type(self) -> common.BuildingType:
        """Returns the type of the building."""
        return self.data.type if self.data else None

    @property
    def under_construction(self) -> bool:
        """Returns whether the building is under construction."""
        return self.data.construction is not None if self.data else False

    @property
    def upgrades(self) -> Optional[list[common.BuildingUpgradeType]]:
        """Returns the upgrades installed for the building."""
        return self.data.upgrades if self.data else None

    def set_manager(self, item: common.Item, manager: common.InventoryManager) -> bool:
        """Set the manager for an item in the building.

        Args:
            item (Item): The item.
            manager (InventoryManager): The manager.

        Returns:
            bool: Whether the manager was set.
        """
        return self._client.buildings_api.set_manager(self.id, item, manager)

    async def calculate_current_labor_need(self) -> float:
        """Calculates the current labor need based on the building's production recipe.
        Returns:
            float: The labor required for the target multiplier.
        """
        from pymerc.game.recipe_manager import RecipeManager
        recipe_manager = RecipeManager.get_instance(self._client)
        await recipe_manager.load_recipes()

        if self.production:
            recipe = recipe_manager.get_recipe(self.production.recipe.value)
            if recipe:
                if self.items:
                        inventory_assets = self.items
                elif self.data and self.data.producer:
                    inventory_assets = self.data.producer.inventory.account.assets
                else:
                    inventory_assets = []
                if self.data and self.data.storage:
                    inventory_managers = self.data.storage.inventory.managers
                elif self.data and self.data.producer:
                    inventory_managers = self.data.producer.inventory.managers
                else:
                    inventory_managers = []

                return recipe.calculate_target_labor(self.target, inventory_assets, inventory_managers)

        return 0.0
