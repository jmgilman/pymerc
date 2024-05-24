from pymerc.api.base import BaseAPI
from pymerc.api.models import common, transports
from pymerc.util import data

BASE_URL = "https://play.mercatorio.io/api/transports"


class TransportsAPI(BaseAPI):
    """A class for interacting with the transports API endpoint."""

    async def get(self, id: int) -> transports.Transport:
        """Get a transport by its ID.

        Args:
            id (int): The ID of the transport.

        Returns:
            Transport: The transport with the given ID.
        """
        response = await self.client.get(f"{BASE_URL}/{id}")
        return transports.Transport.model_validate(response.json())

    async def set_manager(
        self, id: int, item: common.Item, manager: common.InventoryManager
    ):
        """Sets the manager for the item.

        Args:
            id (int): The ID of the transport.
            item (Item): The item to set the manager for.
            manager (InventoryManager): The manager to set.
        """
        json = data.convert_floats_to_strings(manager.model_dump(exclude_unset=True))
        response = await self.client.patch(
            f"{BASE_URL}{id}/route/inventory/{item.name.lower()}", json=json
        )
        return response.status_code == 200
