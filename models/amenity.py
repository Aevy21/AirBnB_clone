#!/usr/bin/python3
"""
This modele contains a class that inherits from the BaseModel class
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class that inherits from the BaseModel class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
            self.name = kwargs.get('name', "")
        else:
            self.name = ''
