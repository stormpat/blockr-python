"""
Hello
"""
import requests
from src.service import ApiService

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

    # Transaction API

    # Unconfirmed transaction API

    # Address API

api = Api('bitcoin', 'text')
print api.block_transaction('last')