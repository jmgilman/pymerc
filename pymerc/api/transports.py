from typing import Optional

from pydantic import TypeAdapter

from pymerc.api.base import BaseAPI
from pymerc.api.models import transports

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