# Program 10: Extracting Return Values from Tasks
# Concept: Accessing returned results from completed Task objects using .result() or direct assignment.

import asyncio
from time import ctime

async def fetch_data(i):
    print(f"{ctime()} | task {i}: Fetching data...")
    await asyncio.sleep(1)
    print(f"{ctime()} | task {i}: Data fetched!")
    return f"Data Packet {i}"

async def main():
    print(f"{ctime()} | main: Starting task 1")
    task1 = asyncio.create_task(fetch_data(1))
    
    # 1. Accessing return value via direct assignment (awaiting the task)
    print(f"{ctime()} | main: Awaiting task 1 directly...")
    result_direct = await task1
    print(f"{ctime()} | main: Got result via direct assignment: {result_direct}")
    
    # 2. Accessing return value via .result() method (only works after the task is completed)
    print(f"{ctime()} | main: Retrieving result via task1.result()...")
    result_method = task1.result()
    print(f"{ctime()} | main: Got result via .result() method: {result_method}")

if __name__ == "__main__":
    asyncio.run(main())
