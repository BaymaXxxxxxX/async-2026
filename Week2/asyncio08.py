# Program 8: Task Interleaving (Context Switching)
# Concept: Watching a single thread switch back and forth between two different workflows using create_task.

import asyncio
from time import ctime

async def task_a():
    print(f"{ctime()} | [Task A] Step 1: Starting...")
    await asyncio.sleep(0.5) # yielding control back to the event loop
    print(f"{ctime()} | [Task A] Step 2: Resumed & Finished!")

async def task_b():
    print(f"{ctime()} | [Task B] Step 1: Starting...")
    await asyncio.sleep(0.2) # yielding control back to the event loop (runs and resumes faster)
    print(f"{ctime()} | [Task B] Step 2: Resumed & Finished!")

async def main():
    print(f"{ctime()} | main: Scheduling Task A and Task B")
    t1 = asyncio.create_task(task_a())
    t2 = asyncio.create_task(task_b())
    
    # Wait for both tasks to finish
    await t1
    await t2
    print(f"{ctime()} | main: Completed")

if __name__ == "__main__":
    asyncio.run(main())
