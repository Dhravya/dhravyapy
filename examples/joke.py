import dhravyapy
import asyncio


async def main():
    joke = await dhravyapy.Fun().joke()
    print(joke)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
