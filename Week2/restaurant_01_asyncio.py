# restaurant_01_asyncio.py
# Concept: Asyncio-based Restaurant Operation.
# Diners are greeted sequentially, then async tasks are scheduled to run concurrently in the event loop.

import asyncio
from time import ctime, time

async def greet_customer(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    await asyncio.sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

async def serve_customer(customer):
    print(f"{ctime()} [Task-{customer}] Taking Order ...")
    await asyncio.sleep(1)
    print(f"{ctime()} [Task-{customer}] Taking Order ...Done!")
    
    print(f"{ctime()} [Task-{customer}] Cooking Spaghetti ...")
    await asyncio.sleep(1)
    print(f"{ctime()} [Task-{customer}] Cooking Spaghetti ...Done!")
    
    print(f"{ctime()} [Task-{customer}] Manage Bar for Drink ...")
    await asyncio.sleep(1)
    print(f"{ctime()} [Task-{customer}] Manage Bar for Drink ...Done!")
    
    print(f"{ctime()} [Task-{customer}] All served!")

async def main():
    queue = ['A', 'B', 'C']
    start_time = time()
    
    # 1. Greet all customers sequentially
    for customer in queue:
        await greet_customer(customer)
        
    print(f"\n{ctime()} ---- All customers greeted. Scheduling independent Async Tasks! ----\n")
    
    # 2. Serve customers concurrently using asyncio tasks
    tasks = []
    for customer in queue:
        task = asyncio.create_task(serve_customer(customer))
        tasks.append(task)
        
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    
    duration = time() - start_time
    print(f"\n{ctime()} Finished Entire Restaurant Operation in {duration:0.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())
