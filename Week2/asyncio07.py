# Program 7: Dual Tasks Concurrency
# Concept: Scheduling two distinct tasks concurrently and awaiting them individually without gather.

import asyncio
from time import ctime, time

async def task_coro(i, delay):
    print(f"{ctime()} | Task {i}: Started with delay {delay}s")
    await asyncio.sleep(delay)
    print(f"{ctime()} | Task {i}: Done")
    return f"Result {i}"

async def main():
    start_time = time()
    print(f"{ctime()} | main: Scheduling tasks concurrently...")
    
    # Create two tasks concurrently
    task1 = asyncio.create_task(task_coro(1, 2))
    task2 = asyncio.create_task(task_coro(2, 3))
    
    # Await them individually (without gather)
    res1 = await task1
    res2 = await task2
    
    print(f"{ctime()} | main: Received '{res1}' and '{res2}'")
    duration = time() - start_time
    print(f"{ctime()} | Total duration: {duration:0.2f} seconds (shows they ran concurrently!)")

if __name__ == "__main__":
    asyncio.run(main())
