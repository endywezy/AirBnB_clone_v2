#!/usr/bin/python3
"""
Module for the City class.
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Represent a city with state ID and name
    """
    state_id = ""
    name = ""
