"""
from threading import Thread, Lock
from queue import Queue
import time

if __name__ == "__main__":

    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)

    # 3 2 1
    first = q.get()
    print(first)

    q.task_done()
    q.join()

    print('end main')
"""
"""
from threading import Thread, Lock
from queue import Queue
import time


def worker(q, lock):
    while True:
        value = q.get()
        # processing
        with lock:
            print(f' in {current_thread().name} got {value}')
        q.task_done()


if __name__ == "__main__":

    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = False
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print('end main')"""

"""
from threading import Thread, Lock, current_thread
from queue import Queue


def worker(q, lock):
    while True:
        value = q.get()  # blocks until the item is available

        # do stuff...
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} got {value}")
        # ...

        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i + 1}", target=worker, args=(q, lock))
        t.daemon = True  # dies when the main thread dies
        t.start()

    # fill the queue with items
    for x in range(20):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main done')
    
"""
