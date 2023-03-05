import threading
import time

lock = threading.Lock()
print(f'{lock}')
lock.acquire()
print(f'{lock}')
lock.release()
print(f'{lock}')


r_lock = threading.RLock()
r_lock.acquire()
r_lock.acquire()
print(f'{r_lock}')
r_lock.release()
print(f'{r_lock}')
r_lock.release()
print(f'{r_lock}')