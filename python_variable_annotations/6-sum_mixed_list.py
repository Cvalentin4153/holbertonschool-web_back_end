#!/usr/bin/env python3
"""Module for calculating sums of mixed-type lists.

This module provides a function to calculate
the sum of a list containing
both integers and floating-point numbers.

The module demonstrates the use of type annotations with Union types
to handle mixed-type lists and proper return type specification.
"""
from typing import List, Union


def sum_mixed_list(
        mxd_lst: List[Union[int, float]]
) -> float:
    """Calculate the sum of a list containing integers and
    floating-point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing
        integers and/or floating-point numbers.

    Returns:
        float: The sum of all numbers in the input list,
        returned as a float.
    """
    return sum(mxd_lst)
