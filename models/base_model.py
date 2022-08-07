#!/usr/bin/python3
"""Base model module that defines attributes and methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    """Class that holds all the common attributes/methods for classes
    """
    def __init__(self, *args, **kwargs):
        """Initializes the instance attributes
        Args:
        name(str): model name
        my_name (int): model number
        id (int): id of object
        created_at (datetime): time of model creation
        updated_at (datetime): time of model update
        """
        from models import storage
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Prints object details"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates updated_at with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dictionary representation of all the attributes
        in key: value format
        """
        """ice = ["id", "created_at", "__class__", "my_number", "updated_at", "name"]
        cream = [self.id, self.created_at.isoformat(), self.__class__.__name__, self.my_number, self.updated_at.isoformat(), self.name]
        try:
            icecream = dict(zip(ice, cream))
        except IndexError:
            pass
        return icecream
        """
        ice = self.__dict__.copy()
        ice["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                ice[k] = v
        return ice
        
