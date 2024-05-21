from __future__ import annotations

from typing import TYPE_CHECKING, Optional, List
from pymerc.api.models.common import Item, InventoryAccountAsset, InventoryManager
from pymerc.api.models.static import Recipe as RecipeModel

if TYPE_CHECKING:
    from pymerc.client import Client
    from pymerc.game.building import Building


class Recipe:
    def __init__(self, client: Client, recipe_name: str, recipe: RecipeModel | None = None):
        self._client = client
        self.recipe_name = recipe_name
        self.labor: Optional[float] = 0.0
        self.data: Optional[RecipeModel] = recipe
        if recipe is not None:
            self.data = recipe

    async def load(self):
        """Loads the data for the recipe and calculates labor required."""
        if self.data is None:
            recipes = await self._client.static_api.get_recipes()
            for recipe in recipes:
                if recipe.name.value == self.recipe_name:
                    self.data = recipe
        if self.data is None:
            raise ValueError(f"Recipe {self.recipe_name} not found")
        else:
            self.labor = self._determine_labor_required()

    def _determine_labor_required(self) -> float:
        """Calculates the labor required for the recipe."""
        for input_ingredient in self.data.inputs:
            if input_ingredient.product == Item.Labour:
                return input_ingredient.amount
        return 0.0

    def get_labor(self) -> Optional[float]:
        """Returns the labor required for the recipe."""
        return self.labor

    def calculate_target_labor(
            self, target: float, inventory_assets: Optional[dict[Item, InventoryAccountAsset]] = None,
            inventory_managers: Optional[List[InventoryManager]] = None
    ) -> float:
        """Calculates the labor required for the given target multiplier.

        Args:
            target (float): The target percentage multiplier for the recipe.
            inventory_assets (Optional[List[InventoryAccountAsset]]): The list of inventory assets.
            inventory_managers (Optional[List[InventoryManager]]): The list of inventory managers.

        Returns:
            float: The labor required for the target multiplier.
        """
        inventory_assets = inventory_assets or {}
        inventory_managers = inventory_managers or []
        manager_dict = {manager.product: manager for manager in inventory_managers}
        for input_ingredient in self.data.inputs:
            if input_ingredient.product.name == "Labour":
                continue
            required_amount = input_ingredient.amount * target
            available_amount = 0

            asset = inventory_assets.get(input_ingredient.product)
            if asset:
                manager = manager_dict.get(input_ingredient.product, None)
                buy_volume = manager.buy_volume if manager and manager.buy_volume else 0
                capacity = asset.capacity or asset.balance + buy_volume
                available_amount = min(asset.balance - asset.reserved + buy_volume, capacity)

            if required_amount > available_amount:
                target = min(target, available_amount / input_ingredient.amount)

        labor_required = self.labor * target
        return labor_required

    def calculate_target_labor_for_building(self, building: Building) -> float:
        """Wrapper function to calculate target labor using a Building object.

        Args:
            building (Building): The building object to use for inventory assets and managers.

        Returns:
            float: The labor required for the target multiplier.
        """
        inventory_assets = list(building.items.values()) if building.items else []
        inventory_managers = list(
            building.inventory.managers.values()) if building.inventory and building.inventory.managers else []

        return self.calculate_target_labor(building.target, inventory_assets, inventory_managers)
