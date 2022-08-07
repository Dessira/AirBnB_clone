#!/usr/bin/python3
"""Storage module for serialization and deserialization of instances
"""
import json
import os.path

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances
    Args:
    __file_path (file): storage file
    __objects (dictionary): stores the objects
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """initialization of attributes
        """
        pass

    def all(self):
        """Returns the dictionary
        """
        return self.__objects

    def new(self, obj):
        """Sets the object and id as the key
        """
        coffee = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[coffee] = obj

    def save(self):
        """Serializes __objects into a file
        """
        with open(self.__file_path, mode='w') as chips:
            #json.dump({i: v.to_dict() for i, v in self.__objects.items()}, chips)
            holder = self.__objects
            string = ""
            new = {}
            for i, v in holder.items():
                new[i] = v.to_dict()
            json.dump(new, chips)

    def reload(self):
        """Deserializes the json file to __objects
        """
        try:
            with open(self.__file_path, 'r') as lawal:
                for obj in json.load(lawal).values():
                    self.new(eval(obj["__class__"])(**obj))
                """food = json.loads(lawal.read())
                #self.__objects = food
                
                for i in food.values():
                    clss = value["__class__"]
                    self.new(eval(clss)(**value))
                    """
        except:
            pass
