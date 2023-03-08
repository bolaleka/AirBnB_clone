#!/usr/bin/python3

"""Define unittest classes"""
import os
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest cases instance"""

    def test_unique_id(self):
        """Test unique id"""
        self.assertNotEqual(BaseModel(self).id, BaseModel(12).id)

    def test_save(self):
        """Test if save method exist"""

        self.assertTrue(type(BaseModel()).save.__name__, "save")

if __name__ == '__main__':
    unittest.main()
