import unittest
from blockr.utils import *

class TestUtil(unittest.TestCase):
    """ Tests for module utility methods """

    def setUp(self):
        self.address = '198aMn6ZYAczwrE5NvNTUMyJ5qkfy4g3Hi'
        self.address_list = [
            '198aMn6ZYAczwrE5NvNTUMyJ5qkfy4g3Hi',
            '198aMn6ZYAczrE5gNvNTUMyJ5qkfy4w3Hi',
            '138aMn6ZYAczwrE5NvNTUMyJ5qkfy4g3Hi'
        ]

    def test_request_type_single_item(self):
        """ Test that request method handles single addresss correctly."""
        self.assertIs(True, isinstance(request_type(self.address), str))

    def test_request_type_list_of_items(self):
        """ Test that request method handles list of addresses correctlyt."""
        self.assertIs(True, isinstance(request_type(self.address_list), str))
