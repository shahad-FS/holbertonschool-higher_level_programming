#!/usr/bin/python3
"""Module for multiple inheritance."""


class Fish:
    """Class Fish."""

    def swim(self):
        print("The fis is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Class Bird."""

    def fly(self):
        print("The bitd is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class FlyingFish that inherits from Fish and Bird."""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and sky!")
