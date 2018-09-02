import time
import queue
import requests



def task(name, work_queue):
    while not work_queue.empty():
        url = work_queue.get()
        print("Task {} getting URL: {}".format(name, url))
        requests.get(url)
        print("Task {} GOT URL: {}".format(name, url))
        yield


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

    tasks = [
        task('One', work_queue),
        task('Two', work_queue)
    ]
    # run the scheduler to run the tasks
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True

    print()
    end = time.time()
    print("Total elapsed time: {}".format(end - start))


if __name__ == '__main__':
    main()