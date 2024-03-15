#!/usr/bin/env python3
from typing import Tuple, Optional, Union
""" takes a string, and int or float and returns a tupple
    Args: k, v
    return Tuple
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ takes a string and either int r float
        - returns a tupple
    """
    square: float = v * v
    tpl = (k, square)
    return tpl
