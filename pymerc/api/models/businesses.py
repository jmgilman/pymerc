from __future__ import annotations
from typing import Optional

from pydantic import BaseModel

class Business(BaseModel):
    """A business in the game."""
    account: BusinessAccount
    account_id: int
    building_ids: list[int]
    buildings: list[Building]
    contract_ids: list[str]
    id: int
    name: str
    owner_id: int
    transport_ids: list[int]

class BusinessAccount(BaseModel):
    """The account of a business."""
    id: int
    name: str
    owner_id: int
    assets: dict[str, BusinessAccountAsset]

class BusinessAccountAsset(BaseModel):
    """An asset in a business account."""
    balance: float
    reserved: int
    unit_cost: Optional[float] = None

class Building(BaseModel):
    """A building belonging to a business."""
    id: int
    type: str