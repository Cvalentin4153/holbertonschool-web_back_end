#!/usr/bin/env python3

from basic_async_syntax import wait_random
import asyncio

async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)
    
    return delays
    