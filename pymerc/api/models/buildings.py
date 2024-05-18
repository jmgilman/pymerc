from __future__ import annotations

from pydantic import BaseModel

from pymerc.api.models import common

class Building(BaseModel):
    """Represents a building."""
    capacity: int
    construction: BuildingConstruction
    delivery_cost: BuildingDeliveryCost
    id: int
    land: list[common.Location]
    name: str
    owner_id: int
    size: int
    storage: BuildingStorage
    sublocation: common.Location
    town_id: int
    type: common.BuildingType

class BuildingConstruction(BaseModel):
    """Represents a construction on a building."""
    inventory: common.Inventory
    progress: int
    reference: str
    stage: str
    time: int
    upgrade_type: str

class BuildingDeliveryCost(BaseModel):
    """Represents the delivery cost of a building."""
    land_distance: int

class BuildingStorage(BaseModel):
    """Represents the storage of a building."""
    inventory: common.Inventory
    operations: list[str]
    reference: str