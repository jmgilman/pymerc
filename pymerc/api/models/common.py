from __future__ import annotations
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Asset(Enum):
    """Represents an asset."""

    Cog = "cog"
    Handcart = "handcart"
    Money = "money"
    Snekkja = "snekkja"
    Tumbrel = "tumbrel"


class BuildingType(Enum):
    """Represents the type of a building."""

    Apothecary = "apothecary"
    Bakery = "bakery"
    Bloomery = "bloomery"
    Brewery = "brewery"
    Brickworks = "brickworks"
    Butchery = "butchery"
    Carpentry = "carpentry"
    Cartshed = "cartshed"
    Cathedral = "cathedral"
    Center = "center"
    CeramicKiln = "ceramic kiln"
    Chandlery = "chandlery"
    Chapel = "chapel"
    CharcoalHut = "charcoal hut"
    CharcoalKiln = "charcoal kiln"
    Church = "church"
    ClayPit = "clay pit"
    CopperMine = "copper mine"
    Coppersmith = "coppersmith"
    Cottage = "cottage"
    Dairy = "dairy"
    DyeBoiler = "dye boiler"
    Dyeworks = "dyeworks"
    Farmstead = "farmstead"
    Fisher = "fisher"
    FlaxFarm = "flax farm"
    Foundry = "foundry"
    GlassBlower = "glass blower"
    GlassHouse = "glass house"
    GoldMine = "gold mine"
    GrainFarm = "grain farm"
    Guardhouse = "guardhouse"
    HerbGarden = "herb garden"
    Hjell = "hjell"
    Household = "household"
    HuntingLodge = "hunting lodge"
    IronMine = "iron mine"
    Jeweller = "jeweller"
    LeadMine = "lead mine"
    Leatherworks = "leatherworks"
    LoggingCamp = "logging camp"
    Markethall = "markethall"
    Malthouse = "malthouse"
    Mansion = "mansion"
    Mint = "mint"
    NetMaker = "net maker"
    Outpost = "outpost"
    Park = "park"
    Pasture = "pasture"
    Quarry = "quarry"
    RettingPit = "retting pit"
    Ropewalk = "ropewalk"
    Saltery = "saltery"
    SaltMine = "salt mine"
    Sawmill = "sawmill"
    SewingShop = "sewing shop"
    Shipyard = "shipyard"
    Smithy = "smithy"
    Smokery = "smokery"
    Spinnery = "spinnery"
    Stable = "stable"
    Storehouse = "storehouse"
    Square = "square"
    Tannery = "tannery"
    TarKiln = "tar kiln"
    Toolworks = "toolworks"
    Townhall = "townhall"
    Townhouse = "townhouse"
    Townroad = "townroad"
    Vignoble = "vignoble"
    Warehouse = "warehouse"
    Weavery = "weavery"
    Windmill = "windmill"


class BuildingUpgradeType(Enum):
    """Represents the type of a building upgrade."""

    Armsrack = "armsrack"
    Beehives = "beehives"
    Bellows = "bellows"
    ButtonCast = "button cast"
    Cowshed = "cowshed"
    Crane = "crane"
    CraneLift = "crane lift"
    CuringChamber = "curing chamber"
    CuttingTable = "cutting table"
    Fermentory = "fermentory"
    Grindstone = "grindstone"
    GroovedBedstone = "grooved bedstone"
    GuardBooth = "guard booth"
    HoppingVessels = "hopping vessels"
    LimeKiln = "lime kiln"
    LimingPots = "liming pots"
    MaltMill = "malt mill"
    MaltSieve = "malt sieve"
    ManurePit = "manure pit"
    PloughHouse = "plough house"
    SkinningTable = "skinning table"
    SpinningWheel = "spinning wheel"
    SteelAnvil = "steel anvil"
    StoneOven = "stone oven"
    StonecuttersHut = "stonecutter's hut"
    TileMoulds = "tile moulds"
    Toolshed = "toolshed"
    Transmission = "transmission"
    TreadleLoom = "treadle loom"
    UpholstryBench = "upholstry bench"
    Warehouse = "warehouse"
    Weaponsrack = "weaponsrack"


class Climate(Enum):
    """Represents a climate."""

    Cold = "cold"
    Warm = "warm"


class Item(Enum):
    """Represents an item."""

    Alembics = "alembics"
    Arms = "arms"
    Axes = "axes"
    Beer = "beer"
    Belts = "belts"
    Blades = "blades"
    Bread = "bread"
    Bricks = "bricks"
    Butter = "butter"
    Candles = "candles"
    Carting = "carting"
    Casks = "casks"
    Cattle = "cattle"
    Charcoal = "charcoal"
    Cheese = "cheese"
    Clay = "clay"
    Cloth = "cloth"
    Coats = "coats"
    Cog = "cog"
    Cookware = "cookware"
    CopperIngots = "copper ingots"
    CopperOre = "copper ore"
    CuredFish = "cured fish"
    CuredMeat = "cured meat"
    Donations = "donations"
    Dye = "dye"
    DyedCloth = "dyed cloth"
    Firewood = "firewood"
    Fish = "fish"
    FlaxFibres = "flax fibres"
    FlaxPlants = "flax plants"
    Flour = "flour"
    Furniture = "furniture"
    Garments = "garments"
    Glass = "glass"
    Glassware = "glassware"
    GoldBars = "gold bars"
    GoldOre = "gold ore"
    Grain = "grain"
    Grindstones = "grindstones"
    Ham = "ham"
    Handcart = "handcart"
    Harnesses = "harnesses"
    Herbs = "herbs"
    Hides = "hides"
    Honey = "honey"
    HopBeer = "hop beer"
    IronOre = "iron ore"
    Jewellery = "jewellery"
    Labour = "labour"
    LeadBars = "lead bars"
    LeadOre = "lead ore"
    Leather = "leather"
    LightArmor = "light armor"
    Limestone = "limestone"
    Lodging = "lodging"
    Lumber = "lumber"
    Malt = "malt"
    Manure = "manure"
    Meat = "meat"
    Medicine = "medicine"
    Milk = "milk"
    Money = "money"
    Mouldboards = "mouldboards"
    Nails = "nails"
    Nets = "nets"
    OxPower = "ox power"
    Pasties = "pasties"
    Pickaxes = "pickaxes"
    Pies = "pies"
    Ploughs = "ploughs"
    Protection = "protection"
    Resin = "resin"
    Rope = "rope"
    Salt = "salt"
    Scythes = "scythes"
    SilverBars = "silver bars"
    SlackedLime = "slacked lime"
    Snekkja = "snekkja"
    Spirits = "spirits"
    SteelIngots = "steel ingots"
    Stockfish = "stockfish"
    Swords = "swords"
    Tar = "tar"
    Thread = "thread"
    Tiles = "tiles"
    Timber = "timber"
    Tools = "tools"
    Tumbrel = "tumbrel"
    Wax = "wax"
    Wheels = "wheels"
    Windows = "windows"
    Wine = "wine"
    Wool = "wool"
    WroughtIron = "wrought iron"
    Yarn = "yarn"


class ItemType(Enum):
    """Represents an item type."""

    Commodity = "commodity"
    Service = "service"
    Special = "special"


class Skill(Enum):
    """Represents a worker skill."""

    Crafting = "crafting"
    Forging = "forging"
    Maritime = "maritime"
    Mercantile = "mercantile"
    Nutrition = "nutrition"
    Textile = "textile"
    Weaponry = "weaponry"


class SkillLevel(Enum):
    """Represents a worker skill level."""

    Novice = 99
    Worker = 599
    Journeyman = 2699
    Master = 9999


class Transport(Enum):
    """Represents a transport."""

    Cog = "cog"
    Handcart = "handcart"
    Snekkja = "snekkja"
    Tumbrel = "tumbrel"


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
    managers: dict[Item, InventoryManager]
    previous_flows: Optional[dict[Item, InventoryFlow]] = {}
    reserved: Optional[int] = None


class InventoryAccount(BaseModel):
    """Represents an inventory account."""

    assets: dict[Item, InventoryAccountAsset]
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
    imported: Optional[int] = Field(None, alias="import")
    production: Optional[float] = None
    production_cost: Optional[float] = None
    purchase: Optional[int] = None
    sale: Optional[int] = None
