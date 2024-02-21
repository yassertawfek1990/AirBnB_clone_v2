#!/usr/bin/python3
"""Defnass."""
from sqlalchemy.orm import relationship
from models.place import Place
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """Represents a city

    Inherits from SQLAlchemy Base

    Attributes:
        __tablename__ : ThenameMysql
        name : namCity.
        state_id : thity.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
