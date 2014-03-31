import unittest
from blockr.api import Api
from blockr.service import ApiService

class TestApi(unittest.TestCase):
    """ Tests for the main Api class """

    def setUp(self):
        """
        Setting up a few diffrent currencies. Basically they all follow the
        same "path" so they are not all in need for tests. Will add three
        for now.
        """
        self.ltc = ApiService('Litecoin')
        self.btc = ApiService('Bitcoin')
        self.dgc = ApiService('Digitalcoin')

        # One instance of the "real" APi class the user instantiates.
        # Because all methods are identical only need for one test instance.
        self.api = Api('Bitcoin')

    def test_bitcoin_base_url_builder(self):
        """ Testing bitcoin root URI """
        self.assertEqual(self.btc.build_url(), 'http://blockr.io/api/v1/')

    def test_litecoin_base_url_builder(self):
        """ Testing litecoin root URI """
        self.assertEqual(self.ltc.build_url(), 'http://ltc.blockr.io/api/v1/')

    def test_digitalcoin_base_url_builder(self):
        """ Testing digitalcoin root URI """
        self.assertEqual(self.dgc.build_url(), 'http://dgc.blockr.io/api/v1/')

    def test_coin_info(self):
        """ Testing the coin info HTTP call """




if __name__ == '__main__':
    unittest.main()
