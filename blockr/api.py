""" The main API class. This class contains all the API HTTP call methods.
This class uses the util class as helper, and gets its bootstrap from the
ApiService class."""

import requests
import utils
from service import ApiService

# Aliases
r = requests

class Api(ApiService):
    """ The main API class. Calls the Block API with GET requests. """
    def __init__(self, currency, data='json'):
        ApiService.__init__(self, currency)
        self.data = data

    # Coin API
    def coin_info(self):
        """ Get the current coin information. """
        res = r.get(self.build_url() + self.coin)
        return self.execute(res)

    # Exchange rates API
    def exchange_rate(self):
        """ Get the current exchange rate. Has many FIAT money currencies. """
        res = r.get(self.build_url() + self.current_rate)
        return self.execute(res)

    # Block API
    def block_info(self, block):
        """ Get info about a block. Multiple call options. """
        res = r.get(self.build_url() + self.block + str(block))
        return self.execute(res)

    def block_transaction(self, block):
        """ Add docblocks todo """
        res = r.get(self.build_url() + self.block_tx + str(block))
        return self.execute(res)

    def block_transaction_raw(self, block):
        """ Add docblocks todo """
        res = r.get(self.build_url() + self.block_raw + str(block))
        return self.execute(res)

    # Transaction API
    def transaction(self, transaction):
        """ Add docblocks todo """
        res = r.get(self.build_url() + self.tx_info + str(transaction))
        return self.execute(res)

    def transaction_unconfirmed(self, transaction):
        """ Add docblocks todo """
        res = r.get(self.build_url() + self.tx_unconf + str(transaction))
        return self.execute(res)

    # Address API
    def address(self, address, confirmations=0):
        """ Add docblocks todo """
        address = utils.request_type(address)

        confs = {'confirmations': confirmations}
        if confs['confirmations'] > 0:
            res = r.get(self.build_url() + self.addr + str(address), params=confs)
        else:
            res = r.get(self.build_url() + self.addr + str(address))
        return self.execute(res)

    def address_balance(self, address, confirmations=0):
        """ Get a address balance. Optinally add confirmation count """
        address = utils.request_type(address)

        confs = {'confirmations': confirmations}
        if confs['confirmations'] > 0:
            res = r.get(self.build_url() + self.balance + str(address), params=confs)
        else:
            res = r.get(self.build_url() + self.balance + str(address))
        return self.execute(res)

    def address_transactions(self, address):
        """ Show the addess transactions. 200 most recent are available. """
        res = r.get(self.build_url() + self.address_tx + str(address))
        return self.execute(res)

    def address_transactions_unspent(self, address):
        """ Show the addess transactions that are unspent. """
        res = r.get(self.build_url() + self.address_unspent + str(address))
        return self.execute(res)

    def address_transactions_unconfirmed(self, address):
        """ Show the addess unconfirmed transactions. """
        res = r.get(self.build_url() + self.address_unconfirmed + str(address))
        return self.execute(res)
