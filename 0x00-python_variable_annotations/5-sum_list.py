#!/usr/bin/env python3
"""
- Takes a list of instegers as input the returns the sum
"""


def sum_list(intput_list: list[float]) -> float:
    sum: float = 0
    for item in intput_list:
        sum += item
    return sum

#print(sum_list([3.14, 1.11, 2.22]))
