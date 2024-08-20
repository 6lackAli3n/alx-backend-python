#!/usr/bin/env python3
'''
Module that contains a coroutine to
measure the runtime of four parallel async
comprehensions.
'''


import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Executes async_comprehension four times in
    parallel and measures the total runtime.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
