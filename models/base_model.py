#!/usr/bin/python3
"""Base model module that defines attributes and methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    """Class that holds all the common attributes/methods for classes
    """
    def __init__(self, name=None, my_number=0):
        """Initializes the instance attributes
        Args:
        name(str): model name
        my_name (int): model number
        id (int): id of object
        created_at (datetime): time of model creation
        updated_at (datetime): time of model update
        """
        self.name = name
        self.my_number = my_number
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    """@property
    def name(self):
        Get and set the name and handle errors
        return self.name

    @name.setter
    def name(self, val):
        if type(val) != str:
            self.name = str(val)
        else:
            self.name = val

    @property
    def my_number(self):
        Get and set the right type for my_number
        
        return self.my_number

    @my_number.setter
    def my_number(self, val):
        if type(val) != int:
            raise TypeError("please input an integer")
        self.my_number = val
    """
    def __str__(self):
        """Prints object details"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary representation of all the attributes
        in key: value format
        """
        ice = ["my_number", "name", "__class__", "updated_at", "id", "created_at"]
        cream = [self.my_number, self.name, self.__class__.__name__, self.updated_at.isoformat(), self.id, self.created_at.isoformat()]
        try:
            icecream = dict(zip(ice, cream))
        except IndexError:
            pass
        return icecream
