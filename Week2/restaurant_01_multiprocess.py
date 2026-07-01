# restaurant_01_multiprocess.py
# Concept: Multi-processed Restaurant Operation.
# Diners are greeted sequentially, then processes are created to process their orders concurrently.

import multiprocessing
from time import sleep, ctime, time

def greet_customer(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

def serve_customer(customer):
    print(f"{ctime()} [Task-{customer}] Taking Order ...")
    sleep(1)
    print(f"{ctime()} [Task-{customer}] Taking Order ...Done!")
    
    print(f"{ctime()} [Task-{customer}] Cooking Spaghetti ...")
    sleep(1)
    print(f"{ctime()} [Task-{customer}] Cooking Spaghetti ...Done!")
    
    print(f"{ctime()} [Task-{customer}] Manage Bar for Drink ...")
    sleep(1)
    print(f"{ctime()} [Task-{customer}] Manage Bar for Drink ...Done!")
    
    print(f"{ctime()} [Task-{customer}] All served!")

def main():
    queue = ['A', 'B', 'C']
    start_time = time()
    
    # 1. Greet all customers sequentially
    for customer in queue:
        greet_customer(customer)
        
    print(f"\n{ctime()} ---- All customers greeted. Scheduling independent Processes! ----\n")
    
    # 2. Serve customers concurrently using multi-processing
    processes = []
    for customer in queue:
        p = multiprocessing.Process(target=serve_customer, args=(customer,))
        processes.append(p)
        p.start()
        
    # Wait for all processes to finish
    for p in processes:
        p.join()
        
    duration = time() - start_time
    print(f"\n{ctime()} Finished Entire Restaurant Operation in {duration:0.2f} seconds.")

if __name__ == "__main__":
    main()
