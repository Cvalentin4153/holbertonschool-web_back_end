#!/usr/bin/env python3

"""Async Comprehension module.

This module defines an asynchronous comprehension function that returns
a list of random numbers.
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronous comprehension function.

    This coroutine will asynchronously generate a list of random numbers
    using the async_generator coroutine.
    """
    return [i async for i in async_generator()]
