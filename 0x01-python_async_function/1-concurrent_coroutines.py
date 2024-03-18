#!/usr/bin/env python3
import asyncio
import typing

waiter = __import__('0-basic_async_syntax').wait_random
""" module documentation"""


async def wait_n(n: int, max_delay: int) -> list[float]:
    """ spawn wait_random n times with specified max_delay"""
    arr = []
    for _ in range(n):
        task = asyncio.create_task(waiter(max_delay))
        final = arr.append(task)
    return sorted(await asyncio.gather(*arr))

    return final
