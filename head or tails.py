import random
import asyncio
from asyncio import wait_for
async def main():
    print("Guess head or tails")
    await asyncio.sleep(5)
    head_to_tails=random.randint(0,1)
    if head_to_tails==0:
        print("Heads")
    else:
        print("Tails")
asyncio.run(main())