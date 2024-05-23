from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pymerc.api.models.buildings import Building
from pymerc.api.models import common
from pymerc.game.exports import ExportsList, ExportsSummed
from pymerc.game.imports import ImportsList, ImportsSummed
from pymerc.game.transport import Transport

if TYPE_CHECKING:
    from pymerc.client import Client


class Player:
    """A higher level representation of a player in the game."""

    business: common.Business
    data: common.Player
    exports: ExportsSummed
    imports: ImportsSummed
    transports: list[Transport]

    def __init__(self, client: Client):
        self._client = client
        self.exports = ExportsSummed()
        self.imports = ImportsSummed()

    async def load(self):
        """Loads the data for the player."""
        self.data = await self._client.player_api.get()
        self.business = await self._client.businesses_api.get(self.data.household.business_ids[0])
        self.storehouse = await self._client.building(self._get_storehouse_id())

        self.transports = []
        for id in self.business.transport_ids:
            self.transports.append(await self._client.transport(id))

        for transport in self.transports:
            for item, exp in transport.exports.items():
                if item not in self.exports:
                    self.exports[item] = ExportsList([exp])
                else:
                    self.exports[item].append(exp)

            for item, imp in transport.imports.items():
                if item not in self.imports:
                    self.imports[item] = ImportsList([imp])
                else:
                    self.imports[item].append(imp)

    @property
    def buildings(self) -> list[Building]:
        """The buildings the player owns."""
        return self.business.buildings

    @property
    def money(self) -> float:
        """The amount of money the player has."""
        return self.business.account.assets.get(common.Asset.Money).balance

    def _get_storehouse_id(self) -> Optional[int]:
        """Get the ID of the player's storehouse.

        Returns:
            Optional[int]: The ID of the storehouse, if it exists.
        """
        storehouses = [
            building.id
            for building in self.business.buildings
            if building.type == common.BuildingType.Storehouse
        ]

        if storehouses:
            return storehouses[0]
        else:
            return None