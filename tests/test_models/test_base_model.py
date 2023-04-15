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

    def test_init(self):
        """Test __init__ attribute and argument"""

        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertGreater(len(model.id), 0)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

        kwargs = {
            'id': '1234',
            'created_at': '2022-04-15T12:00:00.000000',
            'updated_at': '2022-04-15T13:00:00.000000',
            'name': 'test',
            'value': 10
        }
        model_3 = BaseModel(**kwargs)
        self.assertIsInstance(model_3, BaseModel)
        self.assertEqual(model_3.id, '1234')
        self.assertEqual(model_3.created_at, datetime(2022, 4, 15, 12, 0))
        self.assertEqual(model_3.updated_at, datetime(2022, 4, 15, 13, 0))
        self.assertEqual(model_3.name, 'test')
        self.assertEqual(model_3.value, 10)


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
