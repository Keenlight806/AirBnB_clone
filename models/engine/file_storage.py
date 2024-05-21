#!/usr/bin/python3
'''
Json file
'''
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    '''
    FileStorage class
    '''
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        return FileStorage.__objects

    def save(self):
        old_dict = FileStorage.__objects
        new_dict = {}

        for obj in old_dict.keys():
            new_dict[obj] = old_dict[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                json.dump(new_dict, file)
    
    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    new_dict = json.load(file)
                    for key, value in new_dict.items():
                        self.__class__.__name__, obj_id = key.split(',')

                        cls = eval(class_name)
                        instance = cls(**values)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
