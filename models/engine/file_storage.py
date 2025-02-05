#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        cls_objects = {}
        if cls:
            for k, v in self.__class__.__objects.items():
                if type(self.__class__.__objects[k]) == cls:
                    cls_objects[k] = v
            return cls_objects
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
        """Deserialize from `__file_path` to `__objects`

        Args:
            self (object): <class '__main__.FileStorage'> instance

        Returns:
            None
        """
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
        return None

    def delete(self, obj=None):
        """Delete obj from __objects if found inside.

        Args:
        self (object): <class 'main.HBNBCommand'> type object
            obj (object): <class 'BaseModel'> type object

        Returns:
            None
        """
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            self.__class__.__objects.pop(key, None)
        return None

    def close(self):
        """Method for deserializing the JSON file to objects"""
        self.reload()
