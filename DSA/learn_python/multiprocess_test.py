from multiprocessing import Queue, Process

NUMBER_OF_PROCESSES = 3
queue = Queue()
processes = []
import time

import signal
import threading


class ShutdownHandler:
    _Singleton = None
    """
    Class to handle signals and sends a Event if a Shutdown Signal is received

    The class handles SIGINT(CTRL+C), SIGTSTP(CTRL+Z), SIGTERM(kill) events
    """

    def __init__(self):
        if self._Singleton is None:
            self._Singleton = object()
        else:
            raise Exception('Shutdown Handler already initialize')
        self.signal_event = threading.Event()
        signal.signal(signal.SIGINT, self._handle_signal)
        signal.signal(signal.SIGTSTP, self._handle_signal)
        signal.signal(signal.SIGTERM, self._handle_signal)

    def _handle_signal(self, signalnum, frame):
        self.signal_event.set()


a = 'rohan'
print(a, id(a))


def worker(queue, i):
    shutdown_handler = ShutdownHandler()
    a = i
    print(a, id(a))
    while not shutdown_handler.signal_event.is_set():

        try:
            msg = queue.get(True, 1)
        except:
            msg = None

        if msg:
            print(msg)


for i in range(NUMBER_OF_PROCESSES):
    worker_process = Process(target=worker, args=(queue, i), name='worker_process_{}'.format(i))
    worker_process.start()  # Launch worker as a separate python process
    processes.append(worker_process)

shutdown_handler = ShutdownHandler()
import random

while not shutdown_handler.signal_event.is_set():
    queue.put(random.randrange(1, 100, 1))
    time.sleep(3)
