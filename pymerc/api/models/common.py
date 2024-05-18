from __future__ import annotations
from typing import Optional

from pydantic import BaseModel, Field

class Location(BaseModel):
    """Represents the location of something on the map.

    Attributes:
        x (int): The x coordinate of the location.
        y (int): The y coordinate of the location.
    """

    x: int
    y: int

class Inventory(BaseModel):
    """Represents an inventory."""
    account: InventoryAccount
    capacity: int
    managers: dict[str, InventoryManager]
    previous_flows: Optional[dict[str, InventoryFlow]] = {}
    reserved: int

class InventoryAccount(BaseModel):
    """Represents an inventory account."""
    assets: dict[str, InventoryAccountAsset]
    id: str
    name: Optional[str] = None
    owner_id: int
    sponsor_id: Optional[int] = None

class InventoryAccountAsset(BaseModel):
    """Represents an asset in an inventory account."""
    balance: float
    capacity: Optional[float] = None
    purchase: Optional[float] = None
    purchase_cost: Optional[float] = None
    reserved: float
    reserved_capacity: Optional[float] = None
    sale: Optional[float] = None
    sale_price: Optional[float] = None
    unit_cost: Optional[float] = None

class InventoryManager(BaseModel):
    """Represents an inventory manager."""
    buy_price: Optional[float] = None
    buy_volume: Optional[int] = None
    capacity: Optional[int] = None
    max_holding: Optional[int] = None
    sell_price: Optional[float] = None
    sell_volume: Optional[int] = None

class InventoryFlow(BaseModel):
    """Represents an inventory flow."""
    consumption: Optional[float] = None
    expiration: Optional[float] = None
    export: Optional[int] = None
    imported: Optional[int] = Field(None, alias='import')
    production: Optional[float] = None
    production_cost: Optional[float] = None
    purchase: Optional[int] = None
    sale: Optional[int] = None