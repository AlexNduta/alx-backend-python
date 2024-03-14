#!/usr/bin/env python3
"""
- Takes a list of instegers as input the returns the sum
"""


def sum_list(intput_list: list) -> int:
    sum: int = 0
    for item in intput_list:
        sum += item
    return int(sum)
