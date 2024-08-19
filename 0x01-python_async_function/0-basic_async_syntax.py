#!/usr/bin/env python3
"""
Module 0-basic_async_syntax
Defines an asynchronous coroutine that waits for a random delay.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds.
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
