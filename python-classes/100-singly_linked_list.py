#!/usr/bin/python3
"""Module for singly linked list class"""


class Node:
    """class Node"""
    def __init__(self, data, next_node=None):
        """Initialize a new Node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define a SinglyLinkedList"""
    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new Node into the List in correct sorted order."""
        new_node = Node(value)

        """Insert at the beginning OR empty list."""
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        """Insert in the middle or end."""
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
