#ASYNC/ WAIT SYNTAX 
"""
    Writing asynchronous code
    -Asynchronous programming allows your application to handle multiple
    tasks concurrently without blocking the main thread.

    - async def: defines an asynchronous function - coroutine
    Doesnt execute immediately but returns a cporoutine object

    - await: pauses a function's execution till an awaited expression resolves.
"""

import asyncio

async def fetch_data(url): #async function(coroutine)
    #simulate a network request that takes one secomnd
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    tasks = [fetch_data("https://www.example.com/1"), fetch_data("https://www.example.com/2")]
    results = await asyncio.gather(*tasks) #run coroutines concurrently
    for result in results:
        print(result)

asyncio.run(main())

"""
    fetch_data - an asunc function that simulates a netwrok request
    main - creates two coroutines for fetching data from two urls
    asyncio.gatrher(*tasks) - runs both coroutines concurrently using the event loop
    await asyncio.gather - pauses the execution of main until both coroutines finish
"""


#EXECUTING AN ASYNC FUCNTION
"""
    1. Using asyncio.run()
    Creating an event loop: manages tasks, schedules their execution and handles I/O efficiently

    Running the main coroutine: You specify the top level coroutine (main) that serves
    as an entry point
    Cleaning up the event loop: 
"""

async def main():
    #async code goes here
    pass

if __name__ == "__main__":
    asyncio.run(main())



#HOW TO RUN CONCURRENT COROUTINES
"""
    1. Using asyncio.gather()
    - Allows to launch multiple coroutines simultaneously and await their completion
"""
async def coroutine1(data):
    await asyncio.sleep(1)
    return f"Results from coroutine1: {data}"

async def coroutine2(data):
    await asyncio.sleep(2)
    return f"Results from task2: {data}"

async def main():
    tasks = [coroutine1("data1"), coroutine2("data2")]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())

"""
    2. Using a loop
    Iterating through the list of coroutines and launching them one by one
"""

async def coroutine(data):
    await asyncio.sleep(1)
    print(f"Result: {data}")

async def main():
    tasks = [coroutine("data1"), coroutine("data2"), coroutine("data3")]
    for task in tasks:
        await task
    
asyncio.run(main())


#CREATING ASYNCIO TASKS
"""
    1. Define your coroutine
    - using async def syntax
        async def my_coroutine(data):
            #simulate some work
            await asyncio.sleep(1)
            return f"Result: {data}"


    2. Create a task object
        task = asyncio.create_task(my_coroutine("data"))


    4. Using the task object
        - You can await the task object to get the result
        result = await task

        asaync def main():
            task = asyncio.create_task(my_coroutine("data"))
            result = await task
            print(result)

        asyncio.run(main()
"""


#HOW TO USE THE RANDOM MODULE
"""
    1. Generating random floats
    random.random() - Generates a random floating point number between 0 and 1
"""

import random
random_float = random.randon()
print(random_float)


"""
    2. Generating random integers
    random.randrange(start, stop, step) - 
"""

random_int = random.randrange(1, 6)
print(random_int)


"""
    3. Selecting a random element from a sequence
    random.choice(sequence)
"""
colors = ["red", "green", "blue"]
random_color = random.choice(colors)
print(random_color)


"""
    4. Shuffling a  list
    random.shuffle(list)
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)
print(numbers)


"""
    5. Seeding a random number generator
    random.seed(seed)
"""