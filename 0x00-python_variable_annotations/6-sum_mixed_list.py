#!/usr/bin/env python3
from typing import List, Union
"""
- takes a mixed list, adds the elements and return float
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns a sumation of all items in the array"""
    sum: float = 0
    for item in mxd_lst:
        sum += item

    return sum
