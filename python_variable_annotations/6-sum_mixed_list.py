#!/usr/bin/env python3
from typing import List, Union
"""
This module provides a function to calculate the sum of a
list of mixed integers and floats.

It demonstrates the use of type annotations with lists containing
multiple types and return values.
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of mixed integers and floats.

    Args:
        mxd_lst (List[int, float]): A list containing
        integers and floats.

    Returns:
        float: The sum of all numbers in the input list.
    """
    return sum(mxd_lst)
