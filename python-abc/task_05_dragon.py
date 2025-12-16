#!/usr/bin/python3
"""Module for mixin classes."""


class SwimMixin:
    """Mixin class for swimming behavior."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin class for flying behavior."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class Dragon that inherits from SwimMixin and FlyMixin."""

    def roar(self):
        print("The dragon roars!")
