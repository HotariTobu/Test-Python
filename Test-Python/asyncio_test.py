import asyncio

async def hello_world():
    print("Hello World!")

async def call_hello_world():
    await hello_world()

#loop = asyncio.get_event_loop()
loop = asyncio.new_event_loop()
#loop = asyncio.get_running_loop()
loop.run_until_complete(call_hello_world())


import asyncio

async def hello_world(n):
    await asyncio.sleep(1)
    print("{}: Hello World!".format(n))

async def call_hello_world1():
    print("call_hello_world1()")
    await hello_world(1)

async def call_hello_world2():
    print("call_hello_world2()")
    await hello_world(2)

loop = asyncio.get_event_loop()
loop.create_task(hello_world(3))
loop.create_task(call_hello_world1())
loop.run_until_complete(call_hello_world2())