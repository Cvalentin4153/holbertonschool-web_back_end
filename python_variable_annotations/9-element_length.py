#!/usr/bin/env python3
"""Module for calculating element lengths.

This module provides a function to calculate the length of each element
in a list and return a list of tuples containing each element and its length.

The module demonstrates the use of type annotations with List, Tuple, and Any
to handle lists of various element types and proper return type specification.
"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each element in a list.

    Args:
        lst (List[Any]): A list containing elements of any type.

    Returns:
        List[Tuple[Any, int]]: A list of tuples where each tuple contains
        an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
