import gevent
from gevent import monkey
monkey.patch_all()

import time
import queue


def task(name, work_queue):
    while not work_queue.empty():
        count = work_queue.get()
        total = 0
        for x in range(count):
            print("Task {} running and counting {}".format(name,x))
            time.sleep(0.5)  # We don't need to yield as sleep itself is a yielding function
            total += 1
        print("Task {} total {}".format(name, total))


def main():

    start = time.time()
    work_queue = queue.Queue()
    for work in [15,10,5,2]:
        work_queue.put(work)

    tasks = [
        gevent.spawn(task, "One", work_queue), #These are greenlets
        gevent.spawn(task, "Two", work_queue)  #They won't run until expleicitly told to run
    ]

    gevent.joinall(tasks)
    print()
    end = time.time()
    print("Time taken {}".format(end-start))


if __name__ == '__main__':
    main()