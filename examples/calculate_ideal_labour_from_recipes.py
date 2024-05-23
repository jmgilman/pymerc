import os
import asyncio
from dotenv import load_dotenv

from pymerc.client import Client

# Load the API_USER and API_TOKEN from the environment
load_dotenv()


async def calculate_ideal_labor_for_player_buildings():
    client = Client(os.environ["API_USER"], os.environ["API_TOKEN"])
    player = await client.player()

    total_labor = 0.0

    for building in player.buildings:
        # Ensure we're using the Building class from pymerc.game
        building = await client.building(building.id)
        if building.production:
            labor_required = await building.calculate_current_labor_need()
            print(
                f"Building ID: {building.id}, Type: {building.type}, Recipe: {building.production.recipe.value}, Labor Required: {labor_required}")
            total_labor += labor_required

    print(f"Total labor required for all buildings: {total_labor}")

    await client.close()

if __name__ == "__main__":
    asyncio.run(calculate_ideal_labor_for_player_buildings())
