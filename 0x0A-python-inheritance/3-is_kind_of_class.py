#!/usr/bin/python3
"""Defines function to check class or inherited class"""


def is_kind_of_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
        If obj is exactly an instance of a_class returns True.
        Otherwise returns False.
    """
    if isinstance(obj, a_class):
        return True
    return False
