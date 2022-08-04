#!/usr/bin/python3
"""Unittest for basemodel
"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for base model
    """

    def test_base_id(self):
        """Test the id
        """
        mod = BaseModel()
        mod2 = BaseModel()
        self.assertNotEqual(mod.id, mod2.id)

    def test_base_id_type9(self):
        """Test id type
        """
        mod = BaseModel()
        self.assertEqual(type(mod.id), "str")

    def test_str(self):
        """test str returns
        """
        mod = BaseModel()
        mod.name = "chicken"
        mod.my_number = 50
        self.assertEqual(print(mod), print(mod.__str__()))

    def test_to_dict(self):
        """test the dict method
        """
        mod = BaseModel
        mod.name = "chicken"
        mod.my_number = 50
        gwen = mod.to_dict()
        self.assertEqual(gwen, self.__dict__)

if __name__ == '__main__':
    unittest.main()
