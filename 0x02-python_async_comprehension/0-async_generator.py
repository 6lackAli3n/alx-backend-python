#!/usr/bin/env python3
'''
Module that contains an asynchronous generator.
'''


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Asynchronous generator that yields
    a random float between 0 and 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
