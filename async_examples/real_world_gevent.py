import gevent
from gevent import monkey
monkey.patch_all()

import queue
import requests
import time


def task(name, work_queue):
    while not work_queue.empty():
        url = work_queue.get()
        print("Task {} getting URL: {}".format(name,url))
        requests.get(url)
        print("Task {} got URL: {}".format(name,url))

def main():
    """
    This is the main entry point for the program
    """
    # create the queue of 'work'
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

    # run the tasks
    tasks = [
        gevent.spawn(task, 'One', work_queue),
        gevent.spawn(task, 'Two', work_queue)
    ]
    gevent.joinall(tasks)
    print()
    end = time.time()
    print("Total elapsed time: {}".format(end-start))


if __name__ == '__main__':
    main()