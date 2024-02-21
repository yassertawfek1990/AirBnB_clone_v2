#!/usr/bin/python3
"""hrBnB"""

import shlex
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User
from models.base_model import BaseModel
import json


class FileStorage:
    """ Thcla
    Attributes:
        __file_path: pafile
        __objects: ostoed
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ection
        Return:
            etu
        """
        z = {}
        if cls:
            za = self.__objects
            for v in za:
                k = v.replace('.', ' ')
                k = shlex.split(k)
                if (k[0] == cls.__name__):
                    z[v] = self.__objects[v]
            return (z)
        else:
            return self.__objects

    def new(self, obj):
        """setobj
        Args:
            obj: gt
        """
        if obj:
            v = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[v] = obj

    def save(self):
        """sria"""
        x = {}
        for a, s in self.__objects.items():
            x[a] = s.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as b:
            json.dump(x, b)

    def reload(self):
        """aliz"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as b:
                for a, s in (json.load(b)).items():
                    s = eval(s["__class__"])(**s)
                    self.__objects[a] = s
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ eexi"""
        if obj:
            a = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[a]

    def close(self):
        """ lls"""
        self.reload()
