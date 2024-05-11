from pydantic import BaseModel
from typing import Optional

from pymerc.api.models.common import Location

class ItemOrder(BaseModel):
    """Represents an order for an item in the market."""

    volume: int
    price: float


class MarketItemData(BaseModel):
    """Represents the market data for a single item in a town."""

    price: Optional[float] = 0.0
    last_price: Optional[float] = 0.0
    average_price: Optional[float] = 0.0
    moving_average: Optional[float] = 0.0
    highest_bid: Optional[float] = 0.0
    lowest_ask: Optional[float] = 0.0
    volume: int
    volume_prev_12: Optional[int] = 0
    bid_volume_10: Optional[int] = 0
    ask_volume_10: Optional[int] = 0


class MarketItemDataDetails(BaseModel):
    """Represents the market data for a single item in a town."""

    id: int
    product: str
    asset: str
    currency: str
    bids: list[ItemOrder]
    asks: list[ItemOrder]
    data: MarketItemData


class TownDomainStructure(BaseModel):
    id: str
    type: str
    tags: Optional[list[str]] = []


class TownDomain(BaseModel):
    owner_id: Optional[str] = None
    structure: Optional[TownDomainStructure] = None
    ask_price: Optional[str] = None


class TownStrucure(BaseModel):
    id: int
    type: str
    size: Optional[int] = 0
    owner_id: str
    location: Location
    land: Optional[list[Location]] = []


class TownDemand(BaseModel):
    product: str
    bonus: int
    desire: int
    request: int
    result: int


class TownCommoners(BaseModel):
    account_id: str
    count: int
    migration: float
    sustenance: list[TownDemand]


class TownGovernmentTaxes(BaseModel):
    land_tax: float
    structure_tax: float
    ferry_fees: float


class TownGovernment(BaseModel):
    account_id: str
    demands: list[TownDemand]
    taxes_collected: TownGovernmentTaxes


class TownChurch(BaseModel):
    project_ids: Optional[list[str]] = []


class TownCulture(BaseModel):
    special_market_pressure: Optional[dict[int, float]] = {}


class TownData(BaseModel):
    id: str
    name: str
    location: Location
    region: int
    center_ids: list[int]
    domain: dict[str, TownDomain]
    structures: dict[str, TownStrucure]
    household_ids: list[str]
    commoners: TownCommoners
    government: TownGovernment
    church: TownChurch
    navigation_zones: dict[int, int]
    culture: TownCulture


class Town(BaseModel):
    """Represents a town in the game."""

    id: str
    name: str
    location: Location
    region: int
    capital: bool