#!/usr/bin/env python3
"""
Module for zooming in on a list with type annotations.
"""


from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Creates a zoomed-in version of the input list.
    """
    zoomed_in: List[int] = [
            item for item in lst
            for i in range(int(factor))
            ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
