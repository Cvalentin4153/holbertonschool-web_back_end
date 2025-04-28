#!/usr/bin/env python3
"""
Concurrent Coroutines Module

This module demonstrates the use of asyncio to run multiple
coroutines concurrently and collect their results.
It implements a function that spawns multiple instances of
the wait_random coroutine and returns their delays in ascending order.
"""

from basic_async_syntax import wait_random
import asyncio


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: list[float] = []

    for finished in asyncio.as_completed(tasks):
        delay = await finished
        delays.append(delay)

    return delays
