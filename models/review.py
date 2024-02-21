#!/usr/bin/python3
"""Defines class."""
from models.base_model import Base
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from models.base_model import BaseModel


class Review(BaseModel, Base):
    """present
    Attributes:
        __tablename__ : namSQL
        text : reviion
        place_id : reviee
        user_id : revuser
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
