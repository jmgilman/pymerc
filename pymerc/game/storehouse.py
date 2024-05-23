from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from pymerc.api.models import common
from pymerc.game.building import Building
from pymerc.game.exports import ExportsList
from pymerc.game.imports import ImportsList

if TYPE_CHECKING:
    from pymerc.client import Client
    from pymerc.game.player import Player


class Storehouse:
    """A higher level representation of a storehouse in the game."""

    data: Building
    items: dict[common.Item, StorehouseItem]

    def __init__(self, client: Client, player: Player):
        self._client = client
        self.player = player
        self.items = {}

    async def load(self):
        """Loads the data for the storehouse."""
        storehouses = self.player.buildings.by_type(
            common.BuildingType.Storehouse
        ) + self.player.buildings.by_type(common.BuildingType.Warehouse)
        if not storehouses:
            raise ValueError("No storehouses found.")

        self.data = storehouses[0]
        for item, data in self.data.items.items():
            self.items[item] = StorehouseItem(
                asset=data,
                exports=self.player.exports.get(item, ExportsList()),
                imports=self.player.imports.get(item, ImportsList()),
                manager=self.data.inventory.managers.get(item, None),
                flow=self.data.inventory.previous_flows.get(item, None),
            )


@dataclass
class StorehouseItem:
    """A higher level representation of an item in a storehouse."""

    asset: common.InventoryAccountAsset
    exports: ExportsList
    imports: ImportsList
    manager: common.InventoryManager
    flow: common.InventoryFlow

    @property
    def average_cost(self) -> float:
        """The average cost of the item across production, imports, and purchases."""
        costs = []
        if self.produced:
            costs.append(self.production_cost / self.produced)
        if self.imported:
            costs.append(self.import_cost_flowed / self.imported)
        if self.purchased:
            costs.append(self.purchased_cost / self.purchased)

        if costs:
            return sum(costs) / len(costs)
        else:
            return 0

    @property
    def consumed(self) -> float:
        """The amount of the item consumed."""
        if self.flow:
            return self.flow.consumption
        else:
            return 0.0

    @property
    def consumption_cost(self) -> float:
        """The cost of consuming the item."""
        return (self.consumed * self.average_cost) if self.consumed else 0

    @property
    def exported(self) -> int:
        """The amount of the item exported."""
        if self.flow:
            return self.flow.export or 0
        else:
            return 0

    @property
    def export_value(self) -> float:
        """The value of the item exported if all items were sold at max price."""
        return self.exports.value

    @property
    def export_value_flowed(self) -> float:
        """The value of the item exported based on the actual volume sold and prices received."""
        return self.exports.value_flowed

    @property
    def imported(self) -> int:
        """The amount of the item imported."""
        if self.flow:
            return self.flow.imported or 0
        else:
            return 0

    @property
    def import_cost(self) -> float:
        """The cost of importing the item if all items were bought at max price."""
        return self.imports.cost

    @property
    def import_cost_flowed(self) -> float:
        """The cost of importing the item based on the actual volume bought and prices paid."""
        return self.imports.cost_flowed

    @property
    def sold(self) -> int:
        """The amount of the item sold."""
        if self.flow:
            return self.flow.sale or 0
        else:
            return 0

    @property
    def sale_value(self) -> float:
        """The value of the item sold if all items were sold at max price."""
        if self.sold:
            return self.asset.sale * self.asset.sale_price
        else:
            return 0

    @property
    def produced(self) -> float:
        """The amount of the item produced."""
        if self.flow:
            return self.flow.production
        else:
            return 0.0

    @property
    def production_cost(self) -> float:
        """The cost of producing the item."""
        if self.flow:
            return self.flow.production_cost or 0
        else:
            return 0.0

    @property
    def purchased(self) -> int:
        """The amount of the item purchased."""
        if self.flow:
            return self.flow.purchase or 0
        else:
            return 0

    @property
    def purchased_cost(self) -> float:
        """The cost of purchasing the item."""
        if self.flow:
            if self.flow.purchase:
                return self.asset.purchase * self.asset.purchase_price
            else:
                return 0
        else:
            return 0
