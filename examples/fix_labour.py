"""
This example demonstrates how to adjust the amount of labour being automatically
purchased in a storehouse to match the amount of labour being used.
"""

import asyncio
import math
import os

from dotenv import load_dotenv

from pymerc.api.models.common import Item
from pymerc.client import Client

# Load the API_USER and API_TOKEN from the environment
load_dotenv()


async def main():
    client = Client(os.environ["API_USER"], os.environ["API_TOKEN"])
    player = await client.player()

    manager = player.storehouse.inventory.managers.get(Item.Labour)
    flow = player.storehouse.total_flow.get(Item.Labour)

    consumed = flow.consumption - flow.production

    print(f"Currently consuming {consumed} labour")
    print(f"Currently buying {manager.buy_volume} labour")

    if consumed < manager.buy_volume:
        print(f"Wasting {manager.buy_volume - consumed} labour")
    elif consumed > manager.buy_volume:
        print(f"Missing {consumed - manager.buy_volume} labour")
    else:
        print("Labour consumption is balanced")
        return

    print(f"Adjusting labour purchase amount to {math.ceil(consumed)}")
    manager.buy_volume = math.ceil(consumed)

    result = await player.storehouse.set_manager(Item.Labour, manager)
    if result:
        print("Labour purchase amount adjusted successfully")
    else:
        print("Failed to adjust labour purchase amount")


if __name__ == "__main__":
    asyncio.run(main())
