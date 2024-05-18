#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}


    def __init__(self):
        """Initialize the FileStorage class and create necessary directories and files"""
        self.setup_directories_and_files()


    def setup_directories_and_files(self):
        """Create templates directory and 5-number.html file if they don't exist"""
        templates_dir = os.path.join(os.path.dirname(__file__), '..', 'web_flask', 'templates')
        file_path = os.path.join(templates_dir, '5-number.html')

        try:
            os.makedirs(templates_dir, exist_ok=True)
            with open(file_path, 'a'):
                os.utime(file_path, None)
        except Exception as e:
            print(f"An error occurred while setting up directories and files: {e}")


    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            return {k: v for k, v in FileStorage.__objects.items()
                    if isinstance(v, cls)}
        return FileStorage.__objects


    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})


    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)


    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass


    def delete(self, obj=None):
        """Delete object from file storage"""
        if obj is not None:
            for k, v in self.__objects.copy().items():
                if obj == v:
                    del self.__objects[k]


    def close(self):
        """ Reload storage dictionary from file"""
        self.reload()
