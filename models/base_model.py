#!/usr/bin/python3
"""Defoine basemodel class"""
import uuid
from datetime import datetime
import json


class BaseModel:
    """BaseModel that defines all common
       attributes/methods for other classes
    """

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self):
        """ The init method """
        pass

    def __str__(self):
        """String Manioulation"""
        self.__dict__.update({"updated_at": BaseModel.updated_at})

        return '[' + self.__class__.__name__ + '] ' + '(' + self.id + ') ' \
               + str(dict(sorted(self.__dict__.items())))

    def save(self):
        """Upadte with public instance attribute"""
        self.updated_at = BaseModel.updated_at

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        return {
            'my_number': self.my_number,
            'name': self.name,
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'created_at': self.created_at.isoformat()
        }
