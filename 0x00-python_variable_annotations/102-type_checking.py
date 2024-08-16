#!/usr/bin/env python3
"""
Module for zooming in on a list with type annotations.
"""


from typing import List, Tuple


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Creates a zoomed-in version of the input list.
    """
    zoomed_in: List[int] = [
            item for item in lst
            for i in range(factor)
            ]
    return zoomed_in
