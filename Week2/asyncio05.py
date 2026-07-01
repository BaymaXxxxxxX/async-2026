# Program 5: Sequential Execution (The Wrong Way)
# Concept: Showing that simply awaiting one after another is still sequential (Synchronous behavior).

import asyncio
from time import ctime, time

async def task_coro(i, delay):
    print(f"{ctime()} | Task {i}: Started with delay {delay}s")
    await asyncio.sleep(delay)
    print(f"{ctime()} | Task {i}: Done")

async def main():
    start_time = time()
    print(f"{ctime()} | main starting...")
    
    # Awaiting sequentially (this is synchronous in behavior!)
    await task_coro(1, 1)
    await task_coro(2, 2)
    
    duration = time() - start_time
    print(f"{ctime()} | Total duration: {duration:0.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
