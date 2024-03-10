#!/usr/bin/python3
"""
Module for the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that handles users' information
    Public Attributes that will use FileStorage in engine
    folder to manage serialization and deserialization of User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
