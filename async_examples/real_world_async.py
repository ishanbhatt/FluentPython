import asyncio
import queue
import time

import requests
"""
Basically, you put await in front of every blocking call.
To make, http requests await , you need to have aiohttp.
"""


def task(name, work_queue):
    while not work_queue.empty():
        url = work_queue.get()
        print("Task {} getting URL: {}".format(name, url))
        requests.get(url)
        print("Task {} got URL: {}".format(name, url))


async def main():
    start = time.time()
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for url in [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://shutterfly.com",
        "http://mypublisher.com",
        "http://facebook.com"
    ]:
        work_queue.put(url)

    futures = [loop.run_in_executor(None, task, *(i, work_queue)) for i in range(2)]
    await asyncio.gather(*futures)


if __name__ == "__main__":
    try:
        start = time.time()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        end = time.time()
        print("Total elapsed time: {}".format(end - start))
    except Exception as e:
        print("la la la ",str(e))
    finally:
        loop.close()
