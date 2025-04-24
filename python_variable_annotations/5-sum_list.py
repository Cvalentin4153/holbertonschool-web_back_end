#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of a list of floats.

It demonstrates the use of type annotations with lists and return values.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of all floats in the input list.
    """
    return sum(input_list)
