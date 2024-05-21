import json
import re
from typing import Any

from pydantic import TypeAdapter

from pymerc.api.base import BaseAPI
from pymerc.api.models import static

BASE_URL = "https://play.mercatorio.io/static/js/"
ROOT_URL = "https://play.mercatorio.io/"


class StaticAPI(BaseAPI):
    """A class for interacting with the static data from the game."""

    async def get_buildings(self) -> list[static.Building]:
        """Get the buildings from the game.

        Returns:
            list[static.Building]: The buildings from the game.
        """
        data = await self._get()

        type_adapter = TypeAdapter(list[static.Building])
        return type_adapter.validate_python(data["Gm"])

    async def get_items(self) -> list[static.Item]:
        """Get the items from the game.

        Returns:
            list[static.Item]: The items from the game.
        """
        data = await self._get()

        type_adapter = TypeAdapter(list[static.Item])
        return type_adapter.validate_python(data["RB"])

    async def get_recipes(self) -> list[static.Recipe]:
        """Get the recipes from the game.

        Returns:
            list[static.Recipe]: The recipes from the game.
        """
        data = await self._get()
        corrected_data = self._correct_enum_values(data["F_"])
        type_adapter = TypeAdapter(list[static.Recipe])
        return type_adapter.validate_python(corrected_data)

    async def get_transport(self) -> list[static.Transport]:
        """Get the transport from the game.

        Returns:
            list[static.Transport]: The transport from the game.
        """
        data = await self._get()

        type_adapter = TypeAdapter(list[static.Transport])
        return type_adapter.validate_python(data["g$"])

    async def _get(self) -> Any:
        """Get the static data from the game.

        Returns:
            The static data from the game.
        """
        response = await self.client.get(ROOT_URL)
        pattern = r"src=\"\/static\/js\/(.*?)\">"
        filename = re.search(pattern, response.text).group(1)

        response = await self.client.get(BASE_URL + filename)
        pattern = r"JSON\.parse\('(.*?)'\)"
        return json.loads(re.search(pattern, response.text).group(1).replace("\\", ""))

    @staticmethod
    def _correct_enum_values(data: list[dict]) -> list[dict]:
        """Corrects the enum values in the recipe data."""
        item_corrections = {
            "slaked lime": "slacked lime"
        }

        for recipe in data:
            for output in recipe.get("outputs", []):
                if output["product"] in item_corrections:
                    output["product"] = item_corrections[output["product"]]
            for input_ingredient in recipe.get("inputs", []):
                if input_ingredient["product"] in item_corrections:
                    input_ingredient["product"] = item_corrections[input_ingredient["product"]]

        return data
