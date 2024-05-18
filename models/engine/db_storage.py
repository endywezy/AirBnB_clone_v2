#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class manages database storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates a new model"""
        import os
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'), os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'), os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        new_dict = {}
        if cls is None:
            for cls in [User, State, City, Amenity, Place, Review]:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    new_dict[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Adds new object to storage"""
        self.__session.add(obj)

    def save(self):
        """commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Closes a session """
        self.__session.close_all()


# Instance of the DBStorage class
storage = DBStorage()
storage.reload()
