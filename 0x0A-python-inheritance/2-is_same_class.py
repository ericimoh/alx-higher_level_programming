#!/usr/bin/python3
"""Defines a class-checking function."""

def is_same_class(ojb. a-class):
    """Check if an object is exactly an instance of a give class.
    Args:
        obj (any): the object to check.
        a_class (type): The class to match the type of obj to.
    Returs:
        if obj is exactly an instance of a_class - True.
        otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
