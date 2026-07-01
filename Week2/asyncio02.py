# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.

import inspect

async def f():
    return 123

# Calling the function returns a coroutine object but does not run its body
coro = f()
print(f"coro: {coro}")
print(f"type(coro): {type(coro)}")
print(f"inspect.iscoroutine(coro): {inspect.iscoroutine(coro)}")

# Initiate/step the coroutine by sending None.
# Since it returns 123 immediately, it raises StopIteration containing the return value.
try:
    coro.send(None)
except StopIteration as e:
    print(f"The answer was: {e.value}")
