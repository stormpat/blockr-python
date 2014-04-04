#BlockrPy

[![Build Status](https://travis-ci.org/stormpat/blockr-python.svg?branch=master)](https://travis-ci.org/stormpat/blockr-python)

###Hightlights

- Support for Litecoin, Bitcoin, Digitalcoin, Quarkcoin, Peercoin, Megacoin
- Simple and easy API, based on [requests](https://github.com/kennethreitz/requests).
- New currencies can be added easily. (when available on the blockr. API)

###Requirements

- Python 2.7 only for now.
- [Requests](https://github.com/kennethreitz/requests)

###About

Easily get data from the diffrent blockchains. Support for Blocks, addresses and transactions etc.
Exchange rate API is currently BETA, but will provide usefull helper methods.

###Installation

Clone the repository. (This will be a pip package one day in the future).

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

# Set the return format to UTF-8 (Human readable).
coin = Api('Bitcoin', 'text')
```

#### Keeping it fast

Almost all API calls can handle multiple parameters. For instance, if you request
information about a couple of blocks, you can send one API call for all of them. Parameter delimiter is a comma.

This method reduces HTTP calls, minimizing your application response time.

#### Chaining

Right now you can chain requests together for the following API methods:

- ```block_info()```
- ```block_transaction()```
- ```block_transaction_raw()```
- ```transaction()```
- ```transaction_unconfirmed()```
- ```address()```
- ```address_balance()```

Example (these all will work)

```python
# Get info about a single block (int)
block_info(153)

# Get info about a single block (string)
block_info('153')

# Get info about a multiple blocks (list int)
block_info([153,253,353])

# Get info about a multiple blocks (list string)
block_info(['153','253','353'])

# For the insane (list mixed)
block_info([153,'253','353', 453])
```

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

#### Block API

You can fetch information about a specific block, or multiple blocks at the
same time.

The variable passed in to the block API function can be of:

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

Get information about transactions.

```python

# Confirmed transaction data
tx = transaction(transaction)

# Unconfirmed transactions are not a part of the blockchain and should not be trusted!
tx = transaction_unconfirmed(transaction)

```

#### Address API

Returns basic address data, date, block and transaction, when this address first appeared and last transaction data.

```python
# Get basic info about a specific address
address = api.address('1L8meqhMTRpxasdGt8DHSJfscxgHHzvPgk')

# Get the address current balance
addr_balance = api.address_balance('1L8meqhMTRpxasdGt8DHSJfscxgHHzvPgk')

# Get the address transactions (Only 200 most recent transactions)
addr_tx = api.address_transactions('1L8meqhMTRpxasdGt8DHSJfscxgHHzvPgk')

# Get the address unspent transactions.
addr_tx_unspant = api.address_transactions_unspent('1L8meqhMTRpxasdGt8DHSJfscxgHHzvPgk')

# Get the address unconfirmed transactions.
addr_tx_unconf = api.address_transactions_unconfirmed('1L8meqhMTRpxasdGt8DHSJfscxgHHzvPgk')

```

###RTFM

Remeber to also check out the [Blockr.io API docs](http://blockr.io/documentation/api)