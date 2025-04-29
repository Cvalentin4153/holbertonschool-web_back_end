#!/usr/bin/env python3
"""Async Generator module.

This module defines an asynchronous generator function that yields
random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronous generator function.

    This coroutine will loop 10 times, each time asynchronously
    waiting 1 second, then yielding a random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
