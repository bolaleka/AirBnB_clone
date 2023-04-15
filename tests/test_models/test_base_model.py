#!/usr/bin/python3

"""Define unittest classes"""
import os
import time
import uuid
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest cases instance"""

    def test_attributes(self):
        """Test unique id"""

        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))
	self.assertEqual(type(b.id), str)
	self.assertEqual(type(b.created_at), datetime)
	self.assertEqual(type(b.updated_at), datetime)

    def test_save(self):
        """Test if save method exist"""
        
        b = BaseModel()
        old_updated_at = b.updated_at
        b.save()
        self.assertNotEqual(old_updated_at, b.updated_at)

    def test_to_dict(self):
        """Test Dictionary output"""

        b = BaseModel()
        b_dict = b.to_dict()
        self.assertEqual(type(b_dict), dict)
        self.assertTrue("id" in b_dict)
        self.assertTrue("created_at" in b_dict)
        self.assertTrue("updated_at" in b_dict)
        self.assertTrue("__class__" in b_dict)
        self.assertEqual(b_dict["__class__"], "BaseModel")
        self.assertEqual(type(b_dict["created_at"]), str)
        self.assertEqual(type(b_dict["updated_at"]), str)

    def test_str(self):
        """Test for __str__ representation"""

        b = BaseModel()
        string = "[{}] ({}) {}".format(type(b).__name__, b.id, b.__dict__)
        self.assertEqual(str(b), string)
        

if __name__ == '__main__':
    unittest.main()
