#!/usr/bin/python3
"""
Module for the Review class.
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Represent a review with the attributes
    """
    place_id = ""
    user_id = ""
    text = ""
