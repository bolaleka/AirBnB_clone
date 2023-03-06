#!/usr/bin/python3
"""DOC
"""
from model.base_model import BaseModel
import json


class FileStorage(BaseModel):
    """DOC2
    """
    __file_path = file.json
    __objects = {}

    def __init__(self, *args, **kwargs):
        """Init method
        """
        super().__init__(*args, **kwargs)

    def all(self):
        """Doc all
        """
        return self.__objects

    def new(self, obj):
        """
        """
        obj = self.__objects[super().__class__.__name__.id]

    def save(self):
        """
        """
        self.__object = super().to_dict
        with open(self.__file_path, "w", encoding="UTF-8") as myfile:
            json.dump(self.__object, myfile)

    def load(self):
        """
        """
        try:
            with open("file.json", "r", encoding="UTF-8") as myfile:
                new_dict = json.load(myfile)
            for k, v in new_dict.items():
                obj = self.class_dict[v['__class__']](**v)
                self.__objects[k] = obj
        except FileNotFoundError:
            pass
