#!/usr/bin/env python3
"""Module for creating multiplier functions.

This module provides a function to create a multiplier function
that multiplies a given number by a specified multiplier.

The module demonstrates the use of type annotations with Callable
to specify function types and proper return type specification.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the result of multiplying it by the specified multiplier.
    """
    def multiply(x: float) -> float:
        """Multiply a number by the multiplier.

        Args:
            x (float): The number to multiply.

        Returns:
            float: The result of multiplying x by the multiplier.
        """
        return multiplier * x
    return multiply
