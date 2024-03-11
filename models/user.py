#!/usr/bin/python3
"""
Module for the User class.
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    class User that handles users' information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
