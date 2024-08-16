#!/usr/bin/env python3
"""
Module for safely retrieving a value from a dictionary with type annotations.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Safely retrieves the value associated with a key from a dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
