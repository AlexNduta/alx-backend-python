#!/usr/bin/env python3
from typing import List
"""
- Takes a list of instegers as input the returns the sum
"""


def sum_list(intput_list: List[float]) -> float:
    sum: float = 0
    for item in intput_list:
        sum += item
    return sum
