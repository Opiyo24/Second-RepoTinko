#!/usr/bin/env python3
"""
- Provide a mechanism for efficiently handling asynchronous tasks that produce sequence of values.
"""

import asyncio

async def generate_numbers1(start, end):
    for i in range(start, end + 1):
        await asyncio.sleep(1)
        yield i

async def print_numbers():
    async for number in generate_numbers1(1, 10):
        print(number)

asyncio.run(print_numbers())


"""
- async_result = [expression async for item in async_iterable]
- async_result = {key: expression async for item in async_iterable}
- async_result = {item async for item in async_iterable}
"""

async def fetch_data(url):
    await asyncio.sleep(1)
    return f"Data from {url}"


async def main():
    urls = ["https://example.com/1", "https://example.com/2", "https://example.com/3"]
    results = [await fetch_data(url) for url in urls]
    for result in results:
        print(result)

asyncio.run(main())


from typing import Generator

def generate_numbers(start: int, end: int) -> Generator[int, None, None]:
    for i in range(start, end 
    + 1):
        yield 1



def modify_data(data: str) -> Generator[str, int, str]:
    for chunk in data.splitlines():
        value = yield int(chunk)
        yield f"Modified: {value * 2}"


        
