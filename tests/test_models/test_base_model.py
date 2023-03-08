#!/usr/bin/python3

"""Define unittest classes"""
import os
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest cases instance"""

    def test_unique_id(self):
        self.assertNotEqual(BaseModel(self).id, BaseModel(12).id)

if __name__ == '__main__':
    unittest.main()
