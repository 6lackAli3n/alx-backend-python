#!/usr/bin/env python3
"""
Module that contains a coroutine for async comprehensions.
"""


from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generator.
    Returns:
    A list of 10 random floats.
    """
    return [num async for num in async_generator()]
