import asyncio

async def print_lines():
    await asyncio.sleep(5)
    print("Welcome to [Insert Game Name]")

async def loading_screen():
    await asyncio.sleep(3)
    print("Loading ...")
    await asyncio.sleep(1)
    print('Finished Loading')

async def loop(max: int):
    for x in range(0,max):
        print(x)
        await asyncio.sleep(0.1)
    

async def main():
    await asyncio.gather(
        loop(70),
        print_lines(),
        loading_screen()
    )
    print("Main Ended..")
 

asyncio.run(main())