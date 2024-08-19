#!/usr/bin/env python3
'''
Module 2-measure_runtime
Defines a function to measure
the runtime of executing wait_n.
'''


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measures the total execution time for
    wait_n(n, max_delay) and returns the
    average time per coroutine.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
