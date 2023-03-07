#!/usr/bin/python3
"""Defoine basemodel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel that defines all common
       attributes/methods for other classes
    """

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """ The init method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.upadated_at = self.created_at

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

        return ('[{}], ({}) {}'.format(self.__class__.__name__,
                                        self.id, self.__dict__))

    def save(self):
        """Upadte with public instance attribute"""
        self.updated_at = BaseModel.updated_at

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        new_dict = {}
        for key, values in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dict[key] = values
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
