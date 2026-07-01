# Program 9: Dynamically Tracking Tasks in a List
# Concept: Managing multiple generated tasks dynamically by appending them into a standard Python list.

import asyncio
from time import ctime, time

async def worker(i, delay):
    print(f"{ctime()} | Worker {i}: Working for {delay} seconds...")
    await asyncio.sleep(delay)
    print(f"{ctime()} | Worker {i}: Done!")
    return f"Result from worker {i}"

async def main():
    start_time = time()
    tasks = []
    
    # Generate tasks dynamically and append them to a list
    print(f"{ctime()} | main: Generating and scheduling 5 tasks dynamically")
    for i in range(1, 6):
        # We vary the delay for each task: task 1 takes 0.5s, task 2 takes 1.0s, etc.
        delay = i * 0.5
        task = asyncio.create_task(worker(i, delay))
        tasks.append(task)
        
    print(f"{ctime()} | main: Tasks list populated. Awaiting each task dynamically...")
    
    # Wait for tasks and inspect results
    for task in tasks:
        res = await task
        print(f"{ctime()} | main: Received result: {res}")
        
    duration = time() - start_time
    print(f"{ctime()} | Finished all tasks. Total time: {duration:0.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
