#!/usr/bin/env python3
"""
Module for creating a function that multiplies a float
by a given multiplier with type annotations.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies
    a float by the given multiplier.
    """
    return lambda k: k * multiplier
