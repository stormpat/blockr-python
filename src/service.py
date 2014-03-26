"""This module contains the fundamental parts of the API wrapper. The class job is to bootstrap
the app with the correct URIs for the Blockr API."""

class ApiService(object):
    """ The API service class, provies the backbone for the Api. """
    currency = None
    data = None
    base = None
    url = 'blockr.io/'
    version = 'api/v1/'
    coin = 'coin/info/'
    block = 'block/info/'
    block_tx = 'block/txs/'
    block_raw = 'block/raw/'
    tx_info = 'tx/info/'
    tx_unconf = 'zerotx/info/'
    tx_info_raw = 'tx/raw/'
    current_rate = 'exchangerate/current/'
    addr = 'address/info/'
    balance = 'address/balance/'
    address_tx = 'address/txs/'
    address_unspent = 'address/unspent/'
    currencies = ['litecoin', 'bitcoin', 'digitalcoin',
                  'quarkcoin', 'peercoin', 'megacoin']

    def __init__(self, currency):
        """ Set the user currency, and check if its allowed."""
        self.currency = currency = currency.lower()
        if currency in self.currencies:
            self.build_url()
        else: raise Exception(
                """Only {1} are supported.
                   The currency: "{0}" not allowed""".format(self.currency, self.currencies))

    def build_url(self):
        """ Build the url according the users currency, and API version."""
        if self.currency == 'bitcoin':
            self.base = ''

        if self.currency == 'litecoin':
            self.base = 'ltc.'

        if self.currency == 'digitalcoin':
            self.base = 'dgc.'

        if self.currency == 'quarkcoin':
            self.base = 'qrk.'

        if self.currency == 'peercoin':
            self.base = 'ppc.'

        if self.currency == 'megacoin':
            self.base = 'mec.'

        return 'http://{0}{1}{2}'.format(self.base, self.url, self.version)

    def execute(self, req):
        ''' The main caller method. All HTTP requests are passed via this method. '''
        if self.data == 'json':
            return req.json()
        if self.data == 'text':
            return req.text

