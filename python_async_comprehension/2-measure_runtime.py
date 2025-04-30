#!/usr/bin/env python3
"""Measure Runtime module.

This module defines a coroutine that measures the runtime of executing
async_comprehension four times in parallel.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of executing async_comprehension 4 times.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time
