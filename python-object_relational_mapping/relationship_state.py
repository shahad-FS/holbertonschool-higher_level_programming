#!/usr/bin/python3
"""
State class with realtionship to City
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from realtionship_city import City
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """State class representing 'states' table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Relationship with City
    cities = realtionship(
            "City",
            back_populates="state",
            cascade="all, delete, delete-orphan"
            )
