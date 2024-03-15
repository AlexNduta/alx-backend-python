#!/usr/bin/env python3
from typing import Callable
"""
Takes a float value then returns a function that
multiplies the float value by another float value
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return a funtion multiplying float value"""
    def mtlpt(num: float):
        flt: float = num
        return flt * multiplier
    return mtlpt
