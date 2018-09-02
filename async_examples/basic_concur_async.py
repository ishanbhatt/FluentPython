import asyncio
import queue
import time


async def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0

        for x in range(count):
            print("Task {} running and counting {}".format(name,x))
            await asyncio.sleep(0.5)
            total += 1
        print("Task {} total {}".format(name, total))


async def main():
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)
    t1 = loop.create_task(task("TASK1", work_queue))
    t2 = loop.create_task(task("TASK2", work_queue))
    await asyncio.wait([t1, t2])
    return t1,t2


if __name__ == "__main__":
    try:
        start = time.time()
        loop = asyncio.get_event_loop()
        t1, t2 = loop.run_until_complete(main())
        print()
        end = time.time()
        print('Total elapsed time: {}'.format(end - start))
    except Exception as e:
        print("La la la")
    finally:
        loop.close()