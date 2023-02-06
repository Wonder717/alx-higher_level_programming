#!/usr/bin/python3
"""Defines function to check class or inherited class."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
        If obj is an inherited instance of a_class returns True.
        Otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
