from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class Asset(Enum):
    """Represents an asset."""

    Cog = "cog"
    Handcart = "handcart"
    Hulk = "hulk"
    Money = "money"
    Snekkja = "snekkja"
    Tumbrel = "tumbrel"


class BuildingType(Enum):
    """Represents the type of a building."""

    Apothecary = "apothecary"
    Arena = "arena"
    Bakery = "bakery"
    Bloomery = "bloomery"
    Boardinghouse = "boardinghouse"
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
    FishingShack = "fishing shack"
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
    MachineWorkshop = "machine workshop"
    Malthouse = "malthouse"
    Mansion = "mansion"
    Masonry = "masonry"
    Mint = "mint"
    NetMaker = "net maker"
    Outpost = "outpost"
    Park = "park"
    Pasture = "pasture"
    Quarry = "quarry"
    RettingPit = "retting pit"
    Ropewalk = "ropewalk"
    Rowhouse = "rowhouse"
    SailLoft = "sail loft"
    SaltMine = "salt mine"
    Saltery = "saltery"
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
    RenderingPots = "rendering pots"
    SculptureMoulds = "sculpture moulds"
    Sculptures = "sculptures"
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

    Undefined = "undefined" # Placeholder on the API for test purposes

    Alembics = "alembics"
    Arms = "arms"
    Axes = "axes"
    Beer = "beer"
    Bellows = "bellows"
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
    Chisels = "chisels"
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
    Hulk = "hulk"
    IronOre = "iron ore"
    Jewellery = "jewellery"
    Labour = "labour"
    LeadBars = "lead bars"
    LeadOre = "lead ore"
    Leather = "leather"
    LightArmor = "light armor"
    Limestone = "limestone"
    Lodging = "lodging"
    Logs = "logs"
    Looms = "looms"
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
    Sails = "sails"
    Salt = "salt"
    Sculptures = "sculptures"
    Scythes = "scythes"
    SilverBars = "silver bars"
    SlakedLime = "slaked lime"
    Snekkja = "snekkja"
    SpinningWheels = "spinning wheels"
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


class Recipe(Enum):
    """Represents a recipe."""

    BakeBread1 = "bake bread 1"
    BakeBread2 = "bake bread 2"
    BakeBread3 = "bake bread 3"
    BakePasties1 = "bake pasties 1"
    BakePasties2 = "bake pasties 2"
    BakePasties3 = "bake pasties 3"
    BakePies1 = "bake pies 1"
    BakingDuty1 = "baking duty 1"
    BakingDuty2 = "baking duty 2"
    BindGarments1 = "bind garments 1"
    BindGarments2 = "bind garments 2"
    BlowGlassware1 = "blow glassware 1"
    BlowGlassware2 = "blow glassware 2"
    BoilDye1 = "boil dye 1"
    BoilDye2 = "boil dye 2"
    BorderPatrol1 = "border patrol 1"
    BorderPatrol2 = "border patrol 2"
    BreedCattle1 = "breed cattle 1"
    BreedCattle1Milk = "breed cattle 1 (milk)"
    BreedCattle2 = "breed cattle 2"
    BreedCattle2Milk = "breed cattle 2 (milk)"
    BreedCattle3 = "breed cattle 3"
    BrewBeer1 = "brew beer 1"
    BrewBeer2 = "brew beer 2"
    BrewBeer3 = "brew beer 3"
    BrewBeer4 = "brew beer 4"
    BrewBeer5 = "brew beer 5"
    BrewHopBeer1 = "brew hop beer 1"
    BrewHopBeer2 = "brew hop beer 2"
    BrewHopBeer3 = "brew hop beer 3"
    BuildCog1 = "build cog 1"
    BuildCog2 = "build cog 2"
    BuildHandcart1 = "build handcart 1"
    BuildHandcart2 = "build handcart 2"
    BuildHulk1 = "build hulk 1"
    BuildSnekkja1 = "build snekkja 1"
    BuildSnekkja2 = "build snekkja 2"
    BuildSnekkja3 = "build snekkja 3"
    BuildTumbrel1 = "build tumbrel 1"
    BurnBricks1 = "burn bricks 1"
    BurnCharcoal1 = "burn charcoal 1"
    BurnCharcoal2 = "burn charcoal 2"
    BurnCharcoal3 = "burn charcoal 3"
    BurnCharcoal4 = "burn charcoal 4"
    BurnCookware1 = "burn cookware 1"
    BurnCookware2 = "burn cookware 2"
    BurnCookware3 = "burn cookware 3"
    BurnCookware4 = "burn cookware 4"
    BurnGlass1 = "burn glass 1"
    BurnGlass2 = "burn glass 2"
    BurnLime1 = "burn lime 1"
    BurnTar1 = "burn tar 1"
    BurnTar2 = "burn tar 2"
    BurnTiles1 = "burn tiles 1"
    BurnTiles2 = "burn tiles 2"
    ButcherCattle1a = "butcher cattle 1a"
    ButcherCattle1b = "butcher cattle 1b"
    ButcherCattle2 = "butcher cattle 2"
    Carting1 = "carting 1"
    Carting2 = "carting 2"
    CastSculptures1 = "cast sculptures 1"
    CastSculptures2 = "cast sculptures 2"
    ChurnButter1 = "churn butter 1"
    ChurnButter2 = "churn butter 2"
    CraftArms1 = "craft arms 1"
    CraftBelts1 = "craft belts 1"
    CraftBelts2 = "craft belts 2"
    CraftBelts3 = "craft belts 3"
    CraftBelts4 = "craft belts 4"
    CraftBelts5 = "craft belts 5"
    CraftCookware1 = "craft cookware 1"
    CraftFurniture1 = "craft furniture 1"
    CraftFurniture2 = "craft furniture 2"
    CraftFurniture3 = "craft furniture 3"
    CraftFurniture4 = "craft furniture 4"
    CraftFurniture5 = "craft furniture 5"
    CraftFurniture6 = "craft furniture 6"
    CraftLooms1 = "craft looms 1"
    CraftLooms2 = "craft looms 2"
    CraftLooms3 = "craft looms 3"
    CraftPloughs1 = "craft ploughs 1"
    CraftPloughs2 = "craft ploughs 2"
    CraftPloughs3 = "craft ploughs 3"
    CraftPloughs4 = "craft ploughs 4"
    CraftScythes1 = "craft scythes 1"
    CraftScythes2 = "craft scythes 2"
    CraftScythes3 = "craft scythes 3"
    CraftSpinningWheels1 = "craft spinning wheels 1"
    CraftSpinningWheels2 = "craft spinning wheels 2"
    CraftSpinningWheels3 = "craft spinning wheels 3"
    CraftTools1 = "craft tools 1"
    CraftTools2 = "craft tools 2"
    CraftWheels1 = "craft wheels 1"
    CraftWheels2 = "craft wheels 2"
    CraftWheels3 = "craft wheels 3"
    CraftWheels5 = "craft wheels 5"
    CutBricks1 = "cut bricks 1"
    CutGrindstones1 = "cut grindstones 1"
    CutGrindstones2 = "cut grindstones 2"
    CutGrindstones3 = "cut grindstones 3"
    DeliveryDuty1 = "delivery duty 1"
    DeliveryDuty2 = "delivery duty 2"
    DeliveryDuty3 = "delivery duty 3"
    DigClay1 = "dig clay 1"
    DigClay2 = "dig clay 2"
    DistillSpirits1 = "distill spirits 1"
    DistillSpirits2 = "distill spirits 2"
    DistillSpirits3 = "distill spirits 3"
    DryFish1 = "dry fish 1"
    DryFish2 = "dry fish 2"
    DryStockfish1 = "dry stockfish 1"
    DryStockfish2 = "dry stockfish 2"
    DryStockfish3 = "dry stockfish 3"
    DyeCloth1 = "dye cloth 1"
    DyeCloth2 = "dye cloth 2"
    DyeCloth3 = "dye cloth 3"
    ExtractStone1 = "extract stone 1"
    ExtractStone2 = "extract stone 2"
    ExtractStone3 = "extract stone 3"
    Fishing1 = "fishing 1"
    Fishing2 = "fishing 2"
    Fishing3 = "fishing 3"
    Fishing4 = "fishing 4"
    Fishing5 = "fishing 5"
    ForgeArms1 = "forge arms 1"
    ForgeArms2 = "forge arms 2"
    ForgeArms3 = "forge arms 3"
    ForgeAxes1a = "forge axes 1a"
    ForgeAxes1b = "forge axes 1b"
    ForgeAxes2a = "forge axes 2a"
    ForgeAxes2b = "forge axes 2b"
    ForgeAxes3 = "forge axes 3"
    ForgeBlades1a = "forge blades 1a"
    ForgeBlades1b = "forge blades 1b"
    ForgeBlades2a = "forge blades 2a"
    ForgeBlades2b = "forge blades 2b"
    ForgeBlades3 = "forge blades 3"
    ForgeChisels1 = "forge chisels 1"
    ForgeChisels2 = "forge chisels 2"
    ForgeMouldboards1 = "forge mouldboards 1"
    ForgeMouldboards2 = "forge mouldboards 2"
    ForgePickaxes1a = "forge pickaxes 1a"
    ForgePickaxes1b = "forge pickaxes 1b"
    ForgePickaxes2a = "forge pickaxes 2a"
    ForgePickaxes2b = "forge pickaxes 2b"
    ForgePickaxes3 = "forge pickaxes 3"
    ForgeSwords1a = "forge swords 1a"
    ForgeSwords1b = "forge swords 1b"
    ForgeSwords2a = "forge swords 2a"
    ForgeSwords2b = "forge swords 2b"
    ForgeSwords3 = "forge swords 3"
    ForgeTools1 = "forge tools 1"
    ForgeTools2 = "forge tools 2"
    ForgeTools3 = "forge tools 3"
    ForgeTools4 = "forge tools 4"
    ForgeTools5 = "forge tools 5"
    FurnitureDuty1 = "furniture duty 1"
    GatherFirewood1 = "gather firewood 1"
    GatherFirewood2 = "gather firewood 2"
    GatherFirewood3 = "gather firewood 3"
    GatherResin1 = "gather resin 1"
    GatherResin2 = "gather resin 2"
    GrainPayment = "grain payment"
    GrowFlax1 = "grow flax 1"
    GrowFlax2 = "grow flax 2"
    GrowFlax3 = "grow flax 3"
    GrowFlax4 = "grow flax 4"
    GrowGrain1 = "grow grain 1"
    GrowGrain2 = "grow grain 2"
    GrowGrain3 = "grow grain 3"
    GrowGrain4 = "grow grain 4"
    GrowGrain4Manure = "grow grain 4 (manure)"
    GrowGrain5 = "grow grain 5"
    GrowGrain5Manure = "grow grain 5 (manure)"
    GrowHerbs1 = "grow herbs 1"
    GrowHerbs2 = "grow herbs 2"
    GrowHerbs3 = "grow herbs 3"
    GrowHerbs4 = "grow herbs 4"
    HammerNails1 = "hammer nails 1"
    HarnessOx1 = "harness ox 1"
    HarnessOx2 = "harness ox 2"
    HarnessOx2Manure = "harness ox 2 (manure)"
    HarnessOx3 = "harness ox 3"
    HarnessOx3Manure = "harness ox 3 (manure)"
    HarnessOx4 = "harness ox 4"
    HarnessOx4Manure = "harness ox 4 (manure)"
    HerdSheep1 = "herd sheep 1"
    HerdSheep2 = "herd sheep 2"
    HoldBanquet1a = "hold banquet 1a"
    HoldBanquet1b = "hold banquet 1b"
    HoldBanquet2a = "hold banquet 2a"
    HoldBanquet2b = "hold banquet 2b"
    HoldBanquet2c = "hold banquet 2c"
    HoldBanquet3a = "hold banquet 3a"
    HoldBanquet3b = "hold banquet 3b"
    HoldBanquet3c = "hold banquet 3c"
    HoldBanquet4a = "hold banquet 4a"
    HoldBanquet4b = "hold banquet 4b"
    HoldBanquet5 = "hold banquet 5"
    HoldFeast1 = "hold feast 1"
    HoldFeast2 = "hold feast 2"
    HoldFeast3 = "hold feast 3"
    HoldMass1 = "hold mass 1"
    HoldMass2 = "hold mass 2"
    HoldMass3 = "hold mass 3"
    HoldMass4 = "hold mass 4"
    HoldPrayer1 = "hold prayer 1"
    HoldPrayer2 = "hold prayer 2"
    HoldPrayer3 = "hold prayer 3"
    HoldPrayer4 = "hold prayer 4"
    HoldSermon1 = "hold sermon 1"
    HoldSermon2a = "hold sermon 2a"
    HoldSermon2b = "hold sermon 2b"
    HoldSermon3a = "hold sermon 3a"
    HoldSermon3b = "hold sermon 3b"
    HoldSermon4 = "hold sermon 4"
    Hunting1 = "hunting 1"
    Hunting2 = "hunting 2"
    Hunting3 = "hunting 3"
    Hunting4 = "hunting 4"
    Hunting5 = "hunting 5"
    Jousting1 = "jousting 1"
    Jousting2 = "jousting 2"
    KeepBees1 = "keep bees 1"
    KeepBees1Fallow = "keep bees 1 (fallow)"
    KeepBees1Wax = "keep bees 1 (wax)"
    KeepBees2Fallow = "keep bees 2 (fallow)"
    KnightDuty1 = "knight duty 1"
    KnightDuty2 = "knight duty 2"
    KnightDuty3 = "knight duty 3"
    KnightDuty4 = "knight duty 4"
    KnitGarments1 = "knit garments 1"
    KnitGarments2 = "knit garments 2"
    LetCottages1 = "let cottages 1"
    LetCottages2 = "let cottages 2"
    LetRowhouses1 = "let rowhouses 1"
    LetRowhouses2 = "let rowhouses 2"
    LetRowhouses3 = "let rowhouses 3"
    Logging1 = "logging 1"
    Logging2 = "logging 2"
    Logging3 = "logging 3"
    Logging4 = "logging 4"
    Maintain1 = "maintain 1"
    Maintain2 = "maintain 2"
    MakeAlembics1 = "make alembics 1"
    MakeAlembics2 = "make alembics 2"
    MakeAlembics3 = "make alembics 3"
    MakeBellows1 = "make bellows 1"
    MakeBellows2 = "make bellows 2"
    MakeBellows3 = "make bellows 3"
    MakeBricks1 = "make bricks 1"
    MakeBricks2 = "make bricks 2"
    MakeCandles1 = "make candles 1"
    MakeCandles2 = "make candles 2"
    MakeCandles3 = "make candles 3"
    MakeCandles4 = "make candles 4"
    MakeCasks1 = "make casks 1"
    MakeCasks2 = "make casks 2"
    MakeCheese1 = "make cheese 1"
    MakeCheese2 = "make cheese 2"
    MakeCheese3 = "make cheese 3"
    MakeCheese4 = "make cheese 4"
    MakeCheese5 = "make cheese 5"
    MakeCheese6 = "make cheese 6"
    MakeFlaxFibres1 = "make flax fibres 1"
    MakeFlaxFibres2 = "make flax fibres 2"
    MakeHarnesses1 = "make harnesses 1"
    MakeHarnesses2a = "make harnesses 2a"
    MakeHarnesses2b = "make harnesses 2b"
    MakeHarnesses3 = "make harnesses 3"
    MakeJewellery1 = "make jewellery 1"
    MakeJewellery2 = "make jewellery 2"
    MakeJewellery3 = "make jewellery 3"
    MakeJewellery4 = "make jewellery 4"
    MakeLeatherArmor1 = "make leather armor 1"
    MakeMedicine1 = "make medicine 1"
    MakeMedicine2 = "make medicine 2"
    MakeMedicine3 = "make medicine 3"
    MakeNets1 = "make nets 1"
    MakeNets2 = "make nets 2"
    MakeNets3 = "make nets 3"
    MakeNets4 = "make nets 4"
    MakeNets5 = "make nets 5"
    MakeRope1 = "make rope 1"
    MakeRope2 = "make rope 2"
    MakeRope3 = "make rope 3"
    MakeRope4 = "make rope 4"
    MakeTallowCandles1 = "make tallow candles 1"
    MakeWindows1 = "make windows 1"
    MakeWindows2 = "make windows 2"
    MakeWindows3 = "make windows 3"
    MakeWine1 = "make wine 1"
    MakeWine2 = "make wine 2"
    MakeWine3 = "make wine 3"
    Malting1 = "malting 1"
    Malting2 = "malting 2"
    Malting3 = "malting 3"
    Malting4 = "malting 4"
    Milling1 = "milling 1"
    Milling2 = "milling 2"
    Milling3 = "milling 3"
    Milling4 = "milling 4"
    MineCopper1 = "mine copper 1"
    MineCopper2 = "mine copper 2"
    MineCopper3 = "mine copper 3"
    MineCopper4 = "mine copper 4"
    MineCopper5 = "mine copper 5"
    MineGold1 = "mine gold 1"
    MineGold2 = "mine gold 2"
    MineGold3 = "mine gold 3"
    MineGold4 = "mine gold 4"
    MineIron1 = "mine iron 1"
    MineIron2 = "mine iron 2"
    MineIron3 = "mine iron 3"
    MineIron4 = "mine iron 4"
    MineIron5 = "mine iron 5"
    MineLead1 = "mine lead 1"
    MineLead2 = "mine lead 2"
    MineLead3 = "mine lead 3"
    MineLead4 = "mine lead 4"
    MineSalt1 = "mine salt 1"
    MineSalt2 = "mine salt 2"
    MineSalt3 = "mine salt 3"
    MintCopperCoins1 = "mint copper coins 1"
    MintCopperCoins2 = "mint copper coins 2"
    MintCopperCoins3 = "mint copper coins 3"
    MintGoldCoins1 = "mint gold coins 1"
    MintGoldCoins2 = "mint gold coins 2"
    MintGoldCoins3 = "mint gold coins 3"
    MintSilverCoins1 = "mint silver coins 1"
    MintSilverCoins2 = "mint silver coins 2"
    MintSilverCoins3 = "mint silver coins 3"
    NailDuty1 = "nail duty 1"
    NetDuty1 = "net duty 1"
    Patrol1 = "patrol 1"
    Patrol2 = "patrol 2"
    Patrol2Armor = "patrol 2 (armor)"
    Patrol3 = "patrol 3"
    RefineSteel1a = "refine steel 1a"
    RefineSteel1b = "refine steel 1b"
    RefineSteel2a = "refine steel 2a"
    RefineSteel2b = "refine steel 2b"
    RefineSteel3 = "refine steel 3"
    Retting1 = "retting 1"
    Retting2 = "retting 2"
    Retting3 = "retting 3"
    SaltFish1 = "salt fish 1"
    SaltFish2 = "salt fish 2"
    SaltMeat1 = "salt meat 1"
    SaltMeat2 = "salt meat 2"
    Sawing1 = "sawing 1"
    Sawing2 = "sawing 2"
    Sawing3 = "sawing 3"
    Sawing4 = "sawing 4"
    Sawing5 = "sawing 5"
    Sculpting1 = "sculpting 1"
    Sculpting2 = "sculpting 2"
    Service1 = "service 1"
    Service2 = "service 2"
    Service3 = "service 3"
    Service4 = "service 4"
    SewCoats1a = "sew coats 1a"
    SewCoats1b = "sew coats 1b"
    SewCoats2a = "sew coats 2a"
    SewCoats2b = "sew coats 2b"
    SewCoats3 = "sew coats 3"
    SewGambeson1 = "sew gambeson 1"
    SewGarments1 = "sew garments 1"
    SewGarments2a = "sew garments 2a"
    SewGarments2b = "sew garments 2b"
    SewGarments3a = "sew garments 3a"
    SewGarments3b = "sew garments 3b"
    SewGarments4a = "sew garments 4a"
    SewGarments4b = "sew garments 4b"
    SewGarments5 = "sew garments 5"
    SewSails1 = "sew sails 1"
    SewSails2 = "sew sails 2"
    SewSails3 = "sew sails 3"
    ShearSheep1 = "shear sheep 1"
    ShearSheep2 = "shear sheep 2"
    ShearSheep3 = "shear sheep 3"
    SmeltCopper1 = "smelt copper 1"
    SmeltCopper2 = "smelt copper 2"
    SmeltGold1 = "smelt gold 1"
    SmeltGold2 = "smelt gold 2"
    SmeltGold3 = "smelt gold 3"
    SmeltGold4 = "smelt gold 4"
    SmeltIron1 = "smelt iron 1"
    SmeltIron2 = "smelt iron 2"
    SmeltIron3 = "smelt iron 3"
    SmeltIron4 = "smelt iron 4"
    SmeltLead1 = "smelt lead 1"
    SmeltLead2 = "smelt lead 2"
    SmeltLead2Silver = "smelt lead 2 (silver)"
    SmeltLead3Silver = "smelt lead 3 (silver)"
    SmokeFish1 = "smoke fish 1"
    SmokeFish2 = "smoke fish 2"
    SmokeFish3 = "smoke fish 3"
    SmokeFish4 = "smoke fish 4"
    SmokeHam1 = "smoke ham 1"
    SmokeHam2 = "smoke ham 2"
    SmokeHam3 = "smoke ham 3"
    SmokeMeat1 = "smoke meat 1"
    SmokeMeat2 = "smoke meat 2"
    SmokeMeat3 = "smoke meat 3"
    SmokeMeat4 = "smoke meat 4"
    SpinThread1 = "spin thread 1"
    SpinThread2 = "spin thread 2"
    SpinThread3 = "spin thread 3"
    SpinThread4 = "spin thread 4"
    SpinYarn1 = "spin yarn 1"
    SpinYarn2 = "spin yarn 2"
    SpinYarn3 = "spin yarn 3"
    SpinYarn4 = "spin yarn 4"
    SpinningDuty1Thread = "spinning duty 1 (thread)"
    SpinningDuty1Yarn = "spinning duty 1 (yarn)"
    SplitTimber1 = "split timber 1"
    SplitTimber2 = "split timber 2"
    SplitTimber3 = "split timber 3"
    TanHides1 = "tan hides 1"
    TanHides2 = "tan hides 2"
    TanHides3 = "tan hides 3"
    TrapFish1 = "trap fish 1"
    TrapFish2 = "trap fish 2"
    TrapFish3 = "trap fish 3"
    Trapping1 = "trapping 1"
    Trapping2 = "trapping 2"
    WeaveCloth1 = "weave cloth 1"
    WeaveCloth2 = "weave cloth 2"
    WeaveCloth2Wool = "weave cloth 2 (wool)"
    WeaveCloth3 = "weave cloth 3"
    WeaveCloth3Wool = "weave cloth 3 (wool)"
    WeaveCloth4 = "weave cloth 4"
    WeaveCloth4Wool = "weave cloth 4 (wool)"
    WeaveCloth5 = "weave cloth 5"
    WeaveCloth5Wool = "weave cloth 5 (wool)"
    YokeOx1 = "yoke ox 1"
    YokeOx2 = "yoke ox 2"
    YokeOx2Manure = "yoke ox 2 (manure)"
    YokeOx3 = "yoke ox 3"
    YokeOx3Manure = "yoke ox 3 (manure)"


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
    Hulk = "hulk"
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
    managers: Optional[dict[Item, InventoryManager]] = None
    previous_flows: Optional[dict[Item, InventoryFlow]] = {}
    reserved: Optional[int] = None

    @property
    def items(self) -> dict[Item, InventoryAccountAsset]:
        """The items in the inventory."""
        return self.account.assets


class InventoryAccount(BaseModel):
    """Represents an inventory account."""

    assets: dict[Item, InventoryAccountAsset]
    id: str
    master_id: Optional[str] = None
    name: Optional[str] = None
    owner_id: int
    sponsor_id: Optional[str] = None


class InventoryAccountAsset(BaseModel):
    """Represents an asset in an inventory account."""

    balance: float
    capacity: Optional[float] = None
    purchase: Optional[float] = None
    purchase_price: Optional[float] = None
    reserved: float
    reserved_capacity: Optional[float] = None
    sale: Optional[float] = None
    sale_price: Optional[float] = None
    unit_cost: Optional[float] = None

    @property
    def purchased(self) -> bool:
        """Whether the asset was purchased."""
        return self.purchase is not None

    @property
    def sold(self) -> bool:
        """Whether the asset was sold."""
        return self.sale is not None

    @property
    def total_purchase(self) -> float:
        """The total purchase cost of the asset."""
        return self.purchase * self.purchase_price

    @property
    def total_sale(self) -> float:
        """The total sale cost of the asset."""
        return self.sale * self.sale_price

    @property
    def total_value(self) -> float:
        """The total value of the asset."""
        return self.balance * self.unit_cost


class InventoryManager(BaseModel):
    """Represents an inventory manager."""

    buy_price: Optional[float] = None
    buy_volume: Optional[int] = None
    capacity: Optional[int] = None
    max_holding: Optional[int] = None
    sell_price: Optional[float] = None
    sell_volume: Optional[int] = None

    @property
    def buying(self) -> bool:
        """Whether the manager is buying."""
        return self.buy_price is not None and self.buy_volume is not None

    @property
    def max_buy_price(self) -> float:
        """The maximum buy price of the manager."""
        return self.buy_price * self.buy_volume

    @property
    def max_sell_price(self) -> float:
        """The maximum sell price of the manager."""
        return self.sell_price * self.sell_volume

    @property
    def selling(self) -> bool:
        """Whether the manager is selling."""
        return self.sell_price is not None and self.sell_volume is not None


class InventoryFlow(BaseModel):
    """Represents an inventory flow."""

    consumption: Optional[float] = 0.0
    expiration: Optional[float] = 0.0
    export: Optional[int] = None
    imported: Optional[int] = Field(None, alias="import")
    production: Optional[float] = 0.0
    production_cost: Optional[float] = 0.0
    purchase: Optional[int] = None
    purchase_cost: Optional[float] = 0.0
    resident: Optional[float] = None
    sale: Optional[int] = None
    sale_value: Optional[float] = 0.0
    shortfall: Optional[float] = 0.0


class DeliveryCost(BaseModel):
    """Represents the delivery cost of a building."""

    land_distance: float
    ferry_fee: Optional[float] = None


class Operation(BaseModel):
    """Represents an operation."""

    target: float = None
    production: Optional[float] = None
    provision: Optional[float] = None
    reference: Optional[str] = None
    recipe: Optional[Recipe] = None
    volume: Optional[float] = None
    tax_rate: Optional[float] = None
    tax: Optional[float] = None
    delivery_cost: Optional[DeliveryCost] = None
    flows: Optional[dict[Item, InventoryFlow]] = None

    @property
    def surplus(self) -> float:
        """The surplus of the operation."""
        return self.production - self.target

    @property
    def shortfall(self) -> float:
        """The shortfall of the operation."""
        return self.target - self.production


class Path(BaseModel):
    """Represents part of a path."""

    x: int
    y: int
    c: float


class Producer(BaseModel):
    """Represents a producer."""

    inventory: Inventory
    limited: bool
    manager: str
    previous_operation: Operation
    provider_id: Optional[int] = None
    recipe: Recipe
    reference: str
    target: Optional[float] = None


class ItemTrade(BaseModel):
    """Data for buying/selling an item."""

    direction: str
    expected_balance: float
    operation: str
    price: float
    volume: int


class ItemTradeResult(BaseModel):
    """Result of buying/selling an item."""

    settlements: Optional[list[ItemTradeSettlement]] = None
    order_id: Optional[int] = None
    embedded: Optional[dict] = Field(alias="_embedded", default_factory=dict)

    model_config = ConfigDict(arbitrary_types_allowed=True)


class ItemTradeSettlement(BaseModel):
    """Settlement of an item trade."""

    volume: int
    price: float
