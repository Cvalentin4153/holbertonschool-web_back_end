#!/usr/bin/env python3
"""
Module for converting key-value pairs to a specific tuple format.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert a string key and a numeric value to a tuple.

    Args:
        k (str): The string key.
        v (Union[int, float]): The numeric value, either an integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the string key and the square
        of the numeric value.
    """
    return (k, v ** 2)
