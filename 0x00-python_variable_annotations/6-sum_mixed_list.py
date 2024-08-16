#!/usr/bin/env python3
"""
Module for summing a mixed list of integers and floats with type annotations.
"""


from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing both integers and floats.
    """
    return sum(mxd_lst)
