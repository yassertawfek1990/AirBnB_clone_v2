#!/usr/bin/python3
"""hilass"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.review import Review
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from models.place import Place


class User(BaseModel, Base):
    """hiser
    Attributes:
        email: maadds
        password: pswrdgin
        first_name: rsame
        last_name: lname
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
