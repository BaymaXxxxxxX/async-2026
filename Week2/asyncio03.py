# Program 3: The Event Loop (asyncio.run)
# Concept: Using the Event Loop to actually execute a Coroutine Object.

import asyncio

async def f():
    await asyncio.sleep(0.5)
    return 111

# The modern way to run a coroutine under an event loop:
result = asyncio.run(f())
print(f"Result from asyncio.run: {result}")

# The low-level way using get_event_loop() (as shown in PDF Slide 20):
loop = asyncio.new_event_loop() # Use new_event_loop to avoid conflicts with run()
asyncio.set_event_loop(loop)
try:
    coro = f()
    result_low_level = loop.run_until_complete(coro)
    print(f"Result from loop.run_until_complete: {result_low_level}")
finally:
    loop.close()
