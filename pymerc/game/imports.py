from __future__ import annotations

from collections import UserDict, UserList
from dataclasses import dataclass
from typing import TYPE_CHECKING

from pymerc.api.models import common
from pymerc.game.town import Town

if TYPE_CHECKING:
    from pymerc.game.transport import Transport

@dataclass
class Import:
    """A representation of an import in the game."""

    asset: common.InventoryAccountAsset
    flow: common.InventoryFlow
    manager: common.InventoryManager
    town: Town
    transport: Transport

    @property
    def cost(self) -> float:
        """The cost of the import if it was bought at max price."""
        return self.manager.max_buy_price

    @property
    def cost_flowed(self) -> float:
        """The cost of the import that flowed in the last turn."""
        if not self.flowed:
            return 0.0

        return self.asset.purchase * self.asset.purchase_price

    @property
    def flowed(self) -> int:
        """How much of the import flowed in the last turn."""
        return self.flow.imported or 0

    @property
    def volume(self) -> int:
        """The volume of the import if it was bought at max volume."""
        return self.manager.buy_volume

class Imports(UserDict[common.Item, Import]):
    """A collection of imports for a transport in the game."""

    @property
    def cost(self) -> float:
        """The total cost of all imports if they were bought at max price."""
        return sum([imp.cost for imp in self.data.values()])

    @property
    def cost_flowed(self) -> float:
        """The total cost of all imports that flowed in the last turn."""
        return sum([imp.cost_flowed for imp in self.data.values()])

    @property
    def flowed(self) -> Imports:
        """The imports that flowed in the last turn."""
        return Imports({item: imp for item, imp in self.data.items() if imp.flowed})

    @property
    def volume(self) -> int:
        """The total volume of all imports if they were bought at max volume."""
        return sum([imp.volume for imp in self.data.values()])

class ImportsList(UserList[Import]):
    """A collection of imports for a transport in the game."""

    @property
    def cost(self) -> float:
        """The total cost of all imports if they were bought at max price."""
        return sum([imp.cost for imp in self.data])

    @property
    def cost_flowed(self) -> float:
        """The total cost of all imports that flowed in the last turn."""
        return sum([imp.cost_flowed for imp in self.data])

    @property
    def flowed(self) -> ImportsList:
        """The imports that flowed in the last turn."""
        return ImportsList([imp for imp in self.data if imp.flowed])

    @property
    def volume(self) -> int:
        """The total volume of all imports if they were bought at max volume."""
        return sum([imp.volume for imp in self.data])

class ImportsSummed(UserDict[common.Item, ImportsList]):
    """A collection of imports for a player in the game."""

    @property
    def cost(self) -> float:
        """The total cost of all imports if they were bought at max price."""
        return sum([sum([imp.cost for imp in imps]) for imps in self.data.values()])

    @property
    def cost_flowed(self) -> float:
        """The total cost of all imports that flowed in the last turn."""
        return sum([sum([imp.cost_flowed for imp in imps]) for imps in self.data.values()])

    @property
    def flowed(self) -> ImportsSummed:
        """The imports that flowed in the last turn."""
        return ImportsSummed({item: imps for item, imps in self.data.items() if any([imp.flowed for imp in imps])})

    @property
    def volume(self) -> int:
        """The total volume of all imports if they were bought at max volume."""
        return sum([sum([imp.volume for imp in imps]) for imps in self.data.values()])

    def by_town_id(self, town_id: int) -> ImportsSummed:
        """Returns the imports for a town by id."""
        return ImportsSummed({item: imps for item, imps in self.data.items() if imps[0].town.data.id == town_id})

    def by_town_name(self, town_name: str) -> ImportsSummed:
        """Returns the imports for a town by name."""
        return ImportsSummed({item: imps for item, imps in self.data.items() if imps[0].town.data.name == town_name})