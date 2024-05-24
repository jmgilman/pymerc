# Pymerc

> A Python library for interacting with the [Mercatorio] browser based game

## Usage

You must first [generate API credentials](https://play.mercatorio.io/settings/api).
Once generated, you can instantiate a `Client` instance using the credentials.

```python
from pymerc.client import Client

# Create a new client
client = Client(os.environ["API_USER"], os.environ["API_TOKEN"])
```

### Game Objects

The `pymerc` package provides both low-level API calls as well as high-level objects that wrap those calls.
In almost all cases, you should plan to use the higher-level objects.
If something is missing in one of these objects, please submit an issue or PR.

Most logic is contained within the `Player` object:

```python
player = await client.player()
```

Creating the player object can take a few seconds as it results in several requests being sent to the API.
It's recommended you re-use the player object instead of recreating it multiple times.
The data for the player object can be updated with:

```python
await player.load()
```

#### Storehouse

Check our balance of beer and then buy some from the local market:

```python
>>> from pymerc.api.models.common import Item
>>> player.storehouse.items[Item.Beer].balance
41.5
>>> player.storehouse.items[Item.Beer].market_data
TownMarketItem(price=2.894, last_price=2.894, average_price=2.894, moving_average=2.868, highest_bid=2.894, lowest_ask=3.0, volume=95, volume_prev_12=1085, bid_volume_10=2, ask_volume_10=20)
>>> await player.storehouse.items[Item.Beer].fetch_market_details()
TownMarketItemDetails(id=47424441199, product=<Item.Beer: 'beer'>, asset=<Item.Beer: 'beer'>, currency='money', bids=[ItemOrder(volume=2, price=2.894)], asks=[ItemOrder(volume=20, price=3.0), ItemOrder(volume=1, price=3.425), ItemOrder(volume=3, price=3.475), ItemOrder(volume=1, price=3.526)], data=TownMarketItem(price=2.894, last_price=2.894, average_price=2.894, moving_average=2.868, highest_bid=2.894, lowest_ask=3.0, volume=95, volume_prev_12=1085, bid_volume_10=0, ask_volume_10=0))
>>> result = await player.storehouse.items[Item.Beer].buy(1, 3.0)
```

Adjust the price and volume of beer we are selling:

```python
>>> result.settlements[0].volume
1
>>> player.storehouse.items[Item.Beer].manager
InventoryManager(buy_price=5.45, buy_volume=0, capacity=100, max_holding=None, sell_price=2.8, sell_volume=25)
>>> await player.storehouse.items[Item.Beer].patch_manager(sell_price=2.7, sell_volume=26)
>>> player.storehouse.items[Item.Beer].manager
InventoryManager(buy_price=5.45, buy_volume=0, capacity=100, max_holding=None, sell_price=2.7, sell_volume=26)
```

#### Transports

Load the transport that is currently docked in Aderhampton:

```python
>>> tr = player.transports.by_town_name('Aderhampton')[0]
>>> tr.docked
True
```

List the items we are exporting here:

```
>>> list(tr.exports.keys())
[<Item.Cloth: 'cloth'>,
 <Item.DyedCloth: 'dyed cloth'>,
 <Item.Garments: 'garments'>]
```

Check how much cloth we exported last turn:

```python
>>> tr.exports[Item.Cloth].manager
InventoryManager(buy_price=None, buy_volume=0, capacity=None, max_holding=None, sell_price=5.0, sell_volume=37)
>>> tr.exports[Item.Cloth].volume_flowed
37
```

Bump our export volume and then buy some more cloth off the Aderhampton market:

```python
>>> await tr.exports[Item.Cloth].patch_manager(sell_volume=38)
>>> await tr.exports[Item.Cloth].fetch_market_details()
TownMarketItemDetails(id=146229288343, product=<Item.Cloth: 'cloth'>, asset=<Item.Cloth: 'cloth'>, currency='money', bids=[ItemOrder(volume=1, price=7.736), ItemOrder(volume=1, price=7.341), ItemOrder(volume=1, price=6.601)], asks=[ItemOrder(volume=1, price=9.072), ItemOrder(volume=1, price=9.205), ItemOrder(volume=1, price=9.339), ItemOrder(volume=1, price=13.677), ItemOrder(volume=1, price=14.152), ItemOrder(volume=3, price=14.628), ItemOrder(volume=1, price=14.699), ItemOrder(volume=3, price=14.919), ItemOrder(volume=6, price=15.138), ItemOrder(volume=3, price=15.358), ItemOrder(volume=1, price=15.578)], data=TownMarketItem(price=7.736, last_price=7.736, average_price=7.736, moving_average=8.918, highest_bid=7.736, lowest_ask=9.072, volume=100, volume_prev_12=1048, bid_volume_10=0, ask_volume_10=0))
>>> player.storehouse.items[Item.Cloth].balance
1477.096
>>> await tr.exports[Item.Cloth].sell(1, 7.736)
>>> player.storehouse.items[Item.Cloth].balance
1476.096
```

#### Data Analysis

Compare our total and actual imports:

```python
>>> player.imports.volume
426
>>> player.imports.volume_flowed
281  # Importing a little over half of our target volume
>>> player.imports.cost
3669.11
>>> player.imports.cost_flowed
1715.167  # Importing at half of our target cost (yay!)
```

See how our cloth production is doing:

```python
>>> cloth = player.storehouse.items[Item.Cloth]
>>> cloth.produced
400.0
>>> cloth.production_cost
2383.614
>>> excess = cloth.produced - cloth.consumed
>>> excess_value = excess * cloth.average_cost
>>> value_flowed = cloth.sale_value + player.exports[Item.Cloth].value_flowed
>>> value_flowed > excess_value
False  # Looks like we're not making money on our excess cloth!
```

## Testing

Since this library parses live API endpoints, mocking values makes little sense.
Instead, you must provide a `.env` file with your API credentials:

```text
API_USER="<USER>"
API_TOKEN="<TOKEN>"
```

The tests will utilize this to validate that all endpoints are parsing correctly:

```shell
pytest .
```

Additionally, you can create an instance of the client/player to test with using `ipython`:

```shell
> ipython
In [1]: from shell import main; await main(); from shell import client;
In [2]: player = await client.player()
```

[Mercatorio]: https://mercatorio.io