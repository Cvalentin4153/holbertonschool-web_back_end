#!/usr/bin/env python3
from typing import Tuple, Union
"""Module for converting key-value pairs to a specific tuple format.

This module provides a function to convert a string key and a numeric value
(either integer or float) into a tuple containing the key and the square
of the value.

The module demonstrates the use of type annotations with Union types
and Tuple return type specification.
"""


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
