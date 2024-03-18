#!/usr/bin/env python3
import asyncio
from typing import List

waiter = __import__('0-basic_async_syntax').wait_random
""" module documentation"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawn wait_random n times with specified max_delay"""
    arr = []
    for _ in range(n):
        arr.append(asyncio.create_task(waiter(max_delay)))
    return sorted(await asyncio.gather(*arr))
