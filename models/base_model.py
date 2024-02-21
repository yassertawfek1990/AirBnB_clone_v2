#!/usr/bin/python3
"""hiAirBnB"""
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class BaseModel:
    """Thilasses """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """tantiaass
        Args:
            args: itsed
            kwargs: argumectaseModel
        Attributes:
            id: unierated
            created_at: create
            updated_at: udate
        """
        if kwargs:
            for a, s in kwargs.items():
                if a == "created_at" or a == "updated_at":
                    s = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f")
                if a != "__class__":
                    setattr(self, a, s)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """retstring
        Return:
            returdictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updat"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creareturns
        Return:
            returnict__
        """
        x = dict(self.__dict__)
        x["__class__"] = str(type(self).__name__)
        x["created_at"] = self.created_at.isoformat()
        x["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in x.keys():
            del x['_sa_instance_state']
        return x

    def __repr__(self):
        """returnenta"""
        return self.__str__()
