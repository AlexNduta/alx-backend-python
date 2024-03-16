#!/usr/bin/env python3
from typing import Sequence, List, Tuple, Iterable
"""
make little refavtoring to code that takes a list as parameter
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ accept a sequence and return a sequence"""
    return [(i, len(i)) for i in lst]
