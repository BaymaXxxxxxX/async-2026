# Program 6: Creating a Concurrent Task
# Concept: Wrapping a coroutine inside asyncio.create_task() to schedule it to run in the background.

import asyncio
from time import ctime, time

async def background_task():
    print(f"{ctime()} | task: Started background execution")
    await asyncio.sleep(2)
    print(f"{ctime()} | task: Completed background execution")
    return "Task completed successfully"

async def main():
    start_time = time()
    print(f"{ctime()} | main: Scheduling background_task")
    
    # Wrap in create_task to schedule it immediately in the event loop
    task = asyncio.create_task(background_task())
    
    print(f"{ctime()} | main: Task created, main doing some synchronous/non-blocking work (sleeping 1s)...")
    await asyncio.sleep(1) # During this sleep, the event loop runs the task!
    
    print(f"{ctime()} | main: Main woke up. Now awaiting the task to finish...")
    result = await task
    print(f"{ctime()} | main: Received result: {result}")
    
    duration = time() - start_time
    print(f"{ctime()} | Total operation duration: {duration:0.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
