# restaurant_01_simple.py
# Concept: Synchronous Restaurant Operation (sequential execution of all tasks per customer).

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
    
    # Synchronous: Process each customer fully (including greeting) one by one
    for customer in queue:
        greet_customer(customer)
        serve_customer(customer)
        
    duration = time() - start_time
    print(f"\n{ctime()} Finished Entire Restaurant Operation in {duration:0.2f} seconds.")

if __name__ == "__main__":
    main()
