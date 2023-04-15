#!/usr/bin/python3
"""DOC
"""
from models.base_model import BaseModel
import json


class FileStorage(BaseModel):
    """DOC2
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            new_dict = {}
            for key, value in FileStorage.__objects.items():
                new_dict[key] = value.to_dict()
            json
