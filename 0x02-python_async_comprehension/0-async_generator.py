#!/usr/bin/env python3
import asyncio
import random
""" module doc"""


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        rand_num = random.uniform(0, 10)
        yield rand_num
