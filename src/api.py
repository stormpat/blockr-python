"""
Hello
"""
import requests
import itertools
from service import ApiService

class Api(ApiService):

    def __init__(self, currency, data='json'):
        ApiService.__init__(self, currency)
        self.data = data

    # Coin API
    def coin_info(self):
        ''' Add docblocks todo '''
        res = requests.get(self.build_url() + self.coin)
        return self.execute(res)

    # Exchange rates API
    def exchange_rate(self):
        ''' Add docblocks todo '''
        res = requests.get(self.build_url() + self.current_rate)
        return self.execute(res)

    # Block API
    def block_info(self, block):
        ''' Add docblocks todo blocks = block id, last, hash CHAIN '''
        res = requests.get(self.build_url() + self.block + str(block))
        return self.execute(res)

    def block_transaction(self, block):
        ''' Add docblocks todo '''
        res = requests.get(self.build_url() + self.block_tx + str(block))
        return self.execute(res)

    def block_transaction_raw(self, block):
        ''' Add docblocks todo '''
        res = requests.get(self.build_url() + self.block_raw + str(block))
        return self.execute(res)

    # Transaction API
    def transaction(self, transaction):
        ''' Add docblocks todo '''
        res = requests.get(self.build_url() + self.tx_info + str(transaction))
        return self.execute(res)

    def unconfirmed_transaction(self, transaction):
        ''' Add docblocks todo '''
        res = requests.get(self.build_url() + self.tx_unconf + str(transaction))
        return self.execute(res)

    # Address API
    def address(self, address={}, confirmations=0):
        ''' Add docblocks todo '''

        confs = {'confirmations': confirmations}
        if confs['confirmations'] > 0:
            res = requests.get(self.build_url() + self.addr + str(address),
                                                              params=confs)
        else:
            res = requests.get(self.build_url() + self.addr + str(address))
        print res.url
        return self.execute(res)



    def address_balance(self, address, confirmations=0):
        ''' Add docblocks todo '''
        confs = {'confirmations': confirmations}
        if confs['confirmations'] > 0:
            res = requests.get(self.build_url() + self.balance + str(address),
                                                             params=confs)
        else:
            res = requests.get(self.build_url() + self.balance + str(address))
        return self.execute(res)


api = Api('bitcoin', 'text')
print api.address('1L8meqhMTRpxasdGt8DHSJfscxgHHzvPgk', '198aMn6ZYAczwrE5NvNTUMyJ5qkfy4g3Hi')