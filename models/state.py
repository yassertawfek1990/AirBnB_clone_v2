#!/usr/bin/python3
"""Tiss"""

from models.city import City
import shlex
from sqlalchemy import Column, Integer, String
import models
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """gffgnh
    Attributes:
        name: ipae
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        s = models.storage.all()
        k = []
        x = []
        for a in s:
            f = a.replace('.', ' ')
            f = shlex.split(f)
            if (f[0] == 'City'):
                k.append(s[a])
        for m in k:
            if (m.state_id == self.id):
                x.append(m)
        return (x)
