# import time
# import os
# def clock():
#     time1 = round(time.time())

#     while True:
#         if (round(time.time())- time1) % 5 == 0:
#             print("5-seconds")
#             time.sleep(1)


# def foo():
#     for i in os.walk('D\\'):
#         print(i[0])
#         time.sleep(1)


# def main():
#     foo()
#     clock()

# main()


import asyncio
async def index1():
    print("Hello")

async def index2():
    await asyncio.sleep(5)
    print("Hello2")

async def index3():
    print("Hello3")

async def main():
    task1 = asyncio.create_task(index1())
    task2 = asyncio.create_task(index2())
    task3 = asyncio.create_task(index3())

    await asyncio.gather(task1, task2, task3)

asyncio.run(main())