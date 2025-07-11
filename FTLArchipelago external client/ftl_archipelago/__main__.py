import asyncio
import pymem
from .client import FTLArchipelagoClient # type: ignore

async def main():
    client = FTLArchipelagoClient()
    await client.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt: 
        pass # add logic for closing (disconnect from server, close game, etc..)
