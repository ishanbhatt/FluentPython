import queue


def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        for x in range(count):
            print("Task {} running for count {} iter {}".format(name,count,x))
            total += 1
            yield
        print("Task {} total: {}".format(name, total))


def main():
    """
    This is the main entry point for the program
    """
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # create some tasks
    tasks = [
        task('One', work_queue),  # They aren't called here. Remember they are generators which yields
        task('Two', work_queue)   # And generators aren't called until someone calls next() on them
                                  # These two are generator objects,They don't RUN the function until told
                                  # You can call them separately using next(tasks[0])
    ]

    # run the tasks
    done = False
    while not done:
        for t in tasks:  # This loop is going to get called everytime. And it will pick up the first task again from tasks.
                         # As it is controlled by while not done.
            try:
                next(t)  # This is doing next on task, not on tasks - STUPID
                print("CONTROL CAME BACK")
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True


if __name__ == '__main__':
    main()