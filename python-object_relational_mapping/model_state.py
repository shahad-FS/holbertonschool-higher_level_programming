#!/usr/bin/python3
"""
State module that defines the State class linked to the states table
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for all models
Base = declarative_base()

class State(Base):
    """
    State class
    Links to the MySQL table 'states'
    """
    __tablename__ = 'states'

    # Define column
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
