#!/usr/bin/python3
"""
Module for the Amenity class.
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Represent a name (str)
    The name of the amenity.
    """
    name = ""
