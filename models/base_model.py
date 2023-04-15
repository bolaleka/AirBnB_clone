#!/usr/bin/python3
"""Defoine basemodel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel that defines all common
       attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ The init method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.upadated_at = datetime.now()

        if kwargs is not None:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            id = str(uuid.uuid4())
            created_at = datetime.now()

    def __str__(self):
        """String Manioulation"""

        return ('[{}] ({}) {}'.format(self.__class__.__name__,
                                        self.id, self.__dict__))

    def save(self):
        """Upadte with public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
