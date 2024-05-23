"""
This example demonstrates how to generate a report of the financial status of a storehouse in a table format.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import os
import asyncio
from dotenv import load_dotenv
from pymerc.api.models.common import Item, Transport
from pymerc.client import Client
from pymerc.game.player import Player
from tabulate import tabulate

# Load the API_USER and API_TOKEN from the environment
load_dotenv()

@dataclass
class ItemReport:
    balance: float = 0
    item: Item = None
    imported: float = 0
    production: float = 0
    purchase: float = 0
    consumption: float = 0
    export: float = 0
    sale: float = 0

async def main():
    client = Client(os.environ["API_USER"], os.environ["API_TOKEN"])
    player = await client.player()

    table = []
    headers = ["Item", "Imported", "Production", "Purchase", "Consumption", "Export", "Sale", "Balance"]

    for item in player.storehouse.items:
        if item.value in Transport:
            continue

        report = generate_report(player, item)
        table.append([
            item.name,
            report.imported,
            report.production,
            report.purchase,
            report.consumption,
            report.export,
            report.sale,
            report.balance
        ])

    print(tabulate(table, headers, floatfmt=".2f"))

def generate_report(player: Player, target_item: Item) -> ItemReport:
    report = ItemReport(target_item)
    report.item = target_item
    item = player.storehouse.items[target_item]

    input = 0
    output = 0

    if item.imported:
        input += item.import_cost_flowed
        report.imported = -item.import_cost_flowed
    if item.produced:
        input += item.production_cost
        report.production = -item.production_cost
    if item.purchased:
        input += item.purchased_cost
        report.purchase = -item.purchased_cost
    if item.consumed:
        consumption = 0
        if target_item in player.sustenance_items:
            consumed = item.consumed - player.sustenance_item_consumption(target_item)
            consumption = consumed * item.average_cost
        else:
            consumption = item.consumption_cost

        input -= consumption
        report.consumption = consumption

    if item.exported:
        output += item.export_value_flowed
        report.export = item.export_value_flowed
    if item.sold:
        output += item.sale_value
        report.sale = item.sale_value

    report.balance = round(output - input, 2)
    return report

if __name__ == "__main__":
    asyncio.run(main())
