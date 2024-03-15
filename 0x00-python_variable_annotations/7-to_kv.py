#!/usr/bin/env python3
from typing import Tuple, Optional
""" takes a string, and int or float and returns a tupple"""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """ takes a string and either int r float
        - returns a tupple
    """
    square: float = v * v
    tpl = (k, square)
    return tpl
