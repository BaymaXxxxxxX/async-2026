# Program 1: The First Coroutine Function
# Concept: Understanding async def and how it differs from a normal function.

import inspect

# A normal function
def normal_func():
    return 123

# A coroutine function
async def async_func():
    return 123

# Check the type of the functions
print(f"type(normal_func): {type(normal_func)}")
print(f"type(async_func): {type(async_func)}")

# Verify using inspect module
print(f"inspect.iscoroutinefunction(normal_func): {inspect.iscoroutinefunction(normal_func)}")
print(f"inspect.iscoroutinefunction(async_func): {inspect.iscoroutinefunction(async_func)}")
