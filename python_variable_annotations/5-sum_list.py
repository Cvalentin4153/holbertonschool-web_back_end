#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of a list of floats.

It demonstrates the use of type annotations with lists and return values.
"""


def sum_list(input_list: float = []) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (list[float], optional): A list of float numbers. Defaults to [].

    Returns:
        float: The sum of all floats in the input list.
    """
    return (sum(input_list))
