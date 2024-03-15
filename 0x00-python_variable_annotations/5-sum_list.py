#!/usr/bin/env python3
from typing import List
""" sum items"""


def sum_list(intput_list: List[float]) -> float:
    """does a sumation """
    sum: float = 0
    for item in intput_list:
        sum += item
    return sum
