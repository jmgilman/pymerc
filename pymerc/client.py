from __future__ import annotations

import httpx

from pymerc.api.buildings import BuildingsAPI
from pymerc.api.businesses import BusinessesAPI
from pymerc.api.map import MapAPI
from pymerc.api.player import PlayerAPI
from pymerc.api.static import StaticAPI
from pymerc.api.towns import TownsAPI
from pymerc.exceptions import TurnInProgressException
from pymerc.game.town import Town

class Client:
    """A simple API client for the Mercatorio API."""

    session: httpx.AsyncClient
    token: str
    user: str

    buildings: BuildingsAPI
    businesses: BusinessesAPI
    map: MapAPI
    player: PlayerAPI
    static: StaticAPI
    towns: TownsAPI

    def __init__(self, user: str, token: str):
        self.session = httpx.AsyncClient(http2=True)
        self.user = user
        self.token = token

        self.session.headers.setdefault("X-Merc-User", self.user)
        self.session.headers.setdefault("Authorization", f"Bearer {self.token}")

        self.buildings = BuildingsAPI(self)
        self.businesses = BusinessesAPI(self)
        self.map = MapAPI(self)
        self.player = PlayerAPI(self)
        self.static = StaticAPI(self)
        self.towns = TownsAPI(self)

    async def close(self):
        await self.session.aclose()

    async def get(self, url: str, **kwargs) -> httpx.Response:
        """Make a GET request to the given URL.

        Args:
            url (str): The URL to make the request to.
            **kwargs: Additional keyword arguments to pass to httpx.

        Returns:
            requests.Response: The response from the server.
        """
        return await self.session.get(url, **kwargs)

    async def town(self, town_id: int) -> Town:
        """Get a town by its ID.

        Args:
            town_id (int): The ID of the town.

        Returns:
            Town: The town with the given ID.
        """
        t = Town(self, town_id)
        await t.load()

        return t

    async def turn(client: Client) -> int:
        """Get the current turn number.

        Args:
            client (Client): The Mercatorio API client.

        Returns:
            int: The current turn number.
        """
        response = await client.get("https://play.mercatorio.io/api/clock")

        if "preparing next game-turn, try again in a few seconds" in response.text:
            raise TurnInProgressException("A turn is in progress")

        return response.json()["turn"]
