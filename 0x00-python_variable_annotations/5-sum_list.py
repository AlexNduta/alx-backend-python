#!/usr/bin/env python3
from typing import List
"""
- Takes a list of instegers as input the returns the sum
- The sum retuned needs to be a float type
"""


def sum_list(intput_list: List[float]) -> float:
    """does a sumation of all list elements
        - should return a float type
    """
    sum: float = 0
    for item in intput_list:
        sum += item
    return sum
