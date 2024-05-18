from pydantic import TypeAdapter

from pymerc.api.base import BaseAPI
from pymerc.api.models import buildings

BASE_URL = "https://play.mercatorio.io/api/buildings/"


class BuildingsAPI(BaseAPI):
    """A class for interacting with the buildings API endpoint."""

    async def get(self, id: int) -> buildings.Building:
        """Get a building by its ID.

        Args:
            id (int): The ID of the building.

        Returns:
            Building: The building.
        """
        response = await self.client.get(f"{BASE_URL}{id}")
        return buildings.Building.model_validate(response.json())
