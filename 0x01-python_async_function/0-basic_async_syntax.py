#!/usr/bin/env python3
import asyncio
import random
"""
- takes an int argument max_delay
- max_delay = 10
"""


async def wait_random(max_delay: int = 10) -> float:
    """waits for specified time """
    time_towait = random.uniform(0, max_delay)
    await asyncio.sleep(time_towait)
    return time_towait
