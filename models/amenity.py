#!/usr/bin/python3
"""Defins."""
from sqlalchemy import Column, String
from models.place import place_amenity
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Thmenity
    Attributes:
        name: inpe
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
