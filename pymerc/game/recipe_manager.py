import asyncio
from pymerc.client import Client
from pymerc.game.recipe import Recipe


class RecipeManager:
    _instance = None

    def __new__(cls, client: Client = None):
        if cls._instance is None and client is not None:
            cls._instance = super(RecipeManager, cls).__new__(cls)
            cls._instance._client = client
            cls._instance.recipes = {}
        return cls._instance

    @classmethod
    def get_instance(cls, client: Client = None):
        if cls._instance is None:
            if client is None:
                raise ValueError("Client must be provided to initialize RecipeManager")
            cls._instance = cls(client)
        return cls._instance

    async def load_recipes(self):
        """Loads all recipes and stores them in a dictionary."""
        if not self.recipes:  # Load recipes only if not already loaded
            recipe_models = await self._client.static_api.get_recipes()
            tasks = []

            for recipe_model in recipe_models:
                recipe = Recipe(self._client, recipe_model.name.value, recipe_model)
                tasks.append(recipe.load())
                self.recipes[recipe_model.name.value] = recipe

            await asyncio.gather(*tasks)

    def get_recipe(self, name: str) -> Recipe:
        """Returns the Recipe object for the given name."""
        return self.recipes.get(name)
