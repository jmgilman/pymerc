import os

import asyncio
from dotenv import load_dotenv

from pymerc.api.models.towns import TownData
from pymerc.client import Client
from pymerc.util import towns as town_utils

# Load the API_USER and API_TOKEN from the environment
load_dotenv()

async def main():
    # Create a client object
    client = Client(os.environ["API_USER"], os.environ["API_TOKEN"])

    # Fetch all town data
    town_data: dict[str, TownData] = {}
    towns = await client.towns.all()
    for town in towns:
        town_data[town.name] = await client.towns.data(town.id)

    # Calculate scores
    most_populated = max(town_data, key=lambda x: town_data[x].commoners.count)
    most_gentry = max(town_data, key=lambda x: len(town_data[x].household_ids))
    most_structures = max(town_data, key=lambda x: len(town_data[x].structures))
    most_taxes = max(town_data, key=lambda x: town_utils.sum_town_taxes(town_data[x]))
    most_satisfied = max(town_data, key=lambda x: town_utils.calculate_town_satisfaction(town_data[x]))

    print("Scoreboard:")
    print(f"Most populated town: {most_populated} ({town_data[most_populated].commoners.count} commoners)")
    print(f"Most gentry: {most_gentry} ({len(town_data[most_gentry].household_ids)} gentry)")
    print(f"Most structures: {most_structures} ({len(town_data[most_structures].structures)} structures)")
    print(f"Most taxes collected: {most_taxes} ({town_utils.sum_town_taxes(town_data[most_taxes])}d)")
    print(f"Most satisfied: {most_satisfied} ({town_utils.calculate_town_satisfaction(town_data[most_satisfied])}% satisfaction)")

if __name__ == "__main__":
    asyncio.run(main())