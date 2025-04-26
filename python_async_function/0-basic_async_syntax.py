#!/usr/bin/env python3
"""
Asynchronous module that provides a function to wait for a random delay.
This module demonstrates basic async syntax in Python.
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns it
    Args:
        max_delay: maximum delay in seconds (default: 10)
    Returns:
        Random float between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
