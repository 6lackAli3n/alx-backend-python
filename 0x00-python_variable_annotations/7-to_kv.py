#!/usr/bin/env python3
"""
Module for creating a tuple from a string and
the square of an int or float with type annotations.
"""


from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of a number.
    """
    return (k, float(v ** 2))
