#!/usr/bin/python3
from abc import ABC, abstractmethod
"""Module for abstract base class"""


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Concrete class for Dog that inherits from Animal."""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Concrete class for Cat that inherits from Animal."""
    def sound(self):
        return "Meow"
