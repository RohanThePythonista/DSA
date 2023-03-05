import time
import threading


def my_fun(name):
    print(f'started {name}')
    time.sleep(5)
    print(f'ended {name}')
    return True


if __name__ == '__main__':
    print('main start')
    t = threading.Thread(target=my_fun, args=['pythonista'])
    t.start()
    t.join()
    print(f'main end')
