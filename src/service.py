"""
A Python Docstring. Todo
"""

class ApiService(object):
    '''
    Docstring. Documentation todo
    '''
    currency = None
    data = None
    base = None
    url = 'blockr.io/'
    version = 'api/v1/'
    confirmations = '?confirmations='
    coin = 'coin/info/'
    block = 'block/info/'
    block_tx = 'block/txs/'
    block_raw = 'block/raw/'
    tx_info = 'tx/info/'
    tx_info_raw = 'tx/raw/'
    current_rate = 'exchangerate/current/'
    address = 'address/info/'
    balance = 'address/balance/'
    address_tx = 'address/txs/'
    address_unspent = 'address/unspent/'
    currencies = ['litecoin', 'bitcoin', 'digitalcoin',
                  'quarkcoin', 'peercoin', 'megacoin']

    def __init__(self, currency):
        self.currency = currency = currency.lower()
        if currency in self.currencies:
            self.build_url()
        else: raise Exception(
                '''
                Only Bitcoin, Litecoin and Digitalcoin are supported.
                The currency: "{0}" not allowed
                '''
                .format(self.currency))

    def build_url(self):
        '''
        Docstring. Documentation todo
        '''
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
        ''' Add docblocks todo '''
        if self.data == 'json':
            return req.json()
        if self.data == 'text':
            return req.text

