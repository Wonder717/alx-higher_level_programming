#!/usr/bin/python3
"""Defines function to check class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
        If obj is exactly an instance of a_class returns True.
        Otherwise returns False.
    """
    if type(obj) == a_class:
        return True
    return False
