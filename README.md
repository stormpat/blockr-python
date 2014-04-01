#BlockrPy

[![Build Status](https://travis-ci.org/stormpat/blockr-python.svg?branch=master)](https://travis-ci.org/stormpat/blockr-python)

###Hightlights

- Support for Litecoin, Bitcoin, Digitalcoin, Quarkcoin, Peercoin, Megacoin
- Simple and easy API, based on ```requests```
- New currencies can be added easily. (when available on the blockr. API)

###Requirements

- Python 2.7 only for now.

###About

@todo

###Installation

```pip install blockr-python```

(not submitted to pip yet, clone repo for now)

###Documentation

#### Get started

First create a new instance of the ```Api``` class, then you can start to call
methods on the new object. As an argument you must pass in the cryptocurrency
you want to operate on. See above for available currencies.

As default the return data will be set to ```json``` you can choose ```text```
as an alternative. Text is formatted the was the api returns data.

```python
# New instance with Bitcoin as base currency.
coin = Api('Bitcoin')

# Set the return format to text.
coin = Api('Bitcoin', 'text')
```

#### Keeping it fast

Almost all API calls can handle multiple parameters. For instance, if you request information about a couple of blocks, you can send one API call for all of them. Parameter delimiter is a comma.

So this method reduces HTTP calls, keeping your application fast.

*TODO - ALLOW CHAINS ALL ALL METHODS*



#### Coin API

Get up-to-date information about the current currency you are working with.

- ```coin``` Basic coin information with coin name, abbreviation, logo and homepage URL.
- ```volume``` Volume information: how many coins are in supply and how many coins will there ever be.
- ```last_block``` Information about the last block in the longest chain.
- ```next_difficulty``` When will next difficulty be retargeted and how big it will probably be.
- ```market``` Current price value on markets.y be retargeted and how big it will probably be.
- ```market``` Current price value on markets.

```python
# Get current info about the coin.
info = coin.coin_info()
```

#### Exchange rates API

Get the current exchange rate. All exchange rates are based on the USD.

```python
# Get exchange rate
exchange = coin.exchange_rate()
```

*TODO - BUILD FORMATTER METHODS IN CORE API*

#### Block API

You can fetch information about a specific block, or multiple blocks at the
same time.

The variable passed in to the block pai function can be of:

- A block number (eg: ```223212```)
- A block hash (eg: ```0000000000000000210b10d620600dc1cc2380bb58eb2408f9767eb792ed31fa```)
- A word ```"last"``` - this will always return the latest block

```python
# Get info about a specific
block_id = coin.block_info(block)

# Get info about the blocks transactions
block_tx = coin.block_transaction(block)

# Get info about the blocks transactions (in bitcoind format)
block_tx_raw = coin.block_transaction_raw(block)
```


#### Transaction API


```python

tx = transaction(transaction)

```


#### Address API

```python
api.address('1L8meqhMTRpxasdGt8DHSJfscxgHHzvPgk')
api.address(['1L8meqhMTRpxasdGt8DHSJfscxgHHzvPgk', 10)
api.address(['1L8meqhMTRpxasdGt8DHSJfscxgHHzvPgk', '198aMn6ZYAczwrE5NvNTUMyJ5qkfy4g3Hi'], 10)
```

###Read

Remeber to also check out the [Blockr docs](http://blockr.io/documentation/api)