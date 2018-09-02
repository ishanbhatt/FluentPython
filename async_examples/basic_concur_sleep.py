import time
import queue


def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        for x in range(count):
            print("Task {} running And Counting {}".format(name,x))
            time.sleep(0.5)
            total += 1
            yield  # Here yield is used to switch the control
                   # tasks[0] yields so control goes back then tasks[1] yields so control goes back so on and so forth
        print("Task {} total: {}".format(name, total))


def main():
    """
    This is the main entry point for the program
    """
    # create the queue of 'work'
    start = time.time()
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)


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
    end = time.time()
    print()
    print('Total elapsed time: {}'.format(end-start))


if __name__ == '__main__':
    main()