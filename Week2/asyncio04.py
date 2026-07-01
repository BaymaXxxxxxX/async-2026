# Program 4: The await Keyword
# Concept: Pausing a coroutine to let another operation finish using await.

import asyncio
from time import ctime

async def custom_coro():
    print(f"{ctime()} | custom_coro: Started")
    # Pause custom_coro to let other tasks/operations run for 1 second
    await asyncio.sleep(1)
    print(f"{ctime()} | custom_coro: Done")
    return "custom_coro result"

async def main():
    print(f"{ctime()} | main: Calling and awaiting custom_coro...")
    # main pauses here until custom_coro completes
    result = await custom_coro()
    print(f"{ctime()} | main: Received result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
