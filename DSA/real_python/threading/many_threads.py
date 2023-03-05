import time
import threading


def my_fun(name):
    print(f'started {name}')
    time.sleep(5)
    print(f'ended {name}')
    return True


def my_fun2(name):
    print(f'started2 {name}')
    time.sleep(5)
    print(f'ended2 {name}')
    return True


def my_fun3(name):
    print(f'started3 {name}')
    time.sleep(5)
    print(f'ended3 {name}')
    return True


if __name__ == '__main__':
    print('main start')
    t1 = threading.Thread(target=my_fun, args=['pythonista'])
    t1.start()

    t2 = threading.Thread(target=my_fun2, args=['pythonista'])
    t2.start()

    t3 = threading.Thread(target=my_fun3, args=['pythonista'])
    t3.start()

    t1.join()
    t2.join()
    t3.join()

print(f'main end')
