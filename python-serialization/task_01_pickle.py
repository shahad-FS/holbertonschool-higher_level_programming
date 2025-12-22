#!/usr/bin/python
"""Module for serializing and deserializing using pickle"""
import pickle


class CustomObject:
    """A custom object to demonstrate serialization and deserialization"""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes"""
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file"""
        try:
            with open(filename, 'wb') as file:
                pickle.dumb(self, file)
        except Exception as e:
            print("Error occurred:", e)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            print("Error occurred:", e)
            return None
