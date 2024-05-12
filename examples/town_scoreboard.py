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

    # Sort towns by each criterion and select top three
    most_populated = sorted(town_data.items(), key=lambda item: item[1].commoners.count, reverse=True)[:3]
    most_gentry = sorted(town_data.items(), key=lambda item: len(item[1].household_ids), reverse=True)[:3]
    most_structures = sorted(town_data.items(), key=lambda item: len(item[1].structures), reverse=True)[:3]
    most_taxes = sorted(town_data.items(), key=lambda item: town_utils.sum_town_taxes(item[1]), reverse=True)[:3]
    most_satisfied = sorted(town_data.items(), key=lambda item: town_utils.calculate_town_satisfaction(item[1]), reverse=True)[:3]

    # Print results
    print("Scoreboard:\n")
    print("Most populated towns:")
    for name, data in most_populated:
        print(f"  {name:20} {data.commoners.count} commoners")
    print("\nMost gentry:")
    for name, data in most_gentry:
        print(f"  {name:20} {len(data.household_ids)} gentry")
    print("\nMost structures:")
    for name, data in most_structures:
        print(f"  {name:20} {len(data.structures)} structures")
    print("\nMost taxes collected:")
    for name, data in most_taxes:
        print(f"  {name:20} {town_utils.sum_town_taxes(data)}d")
    print("\nMost satisfied:")
    for name, data in most_satisfied:
        print(f"  {name:20} {town_utils.calculate_town_satisfaction(data)}% satisfaction")

if __name__ == "__main__":
    asyncio.run(main())
