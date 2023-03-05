import time
import concurrent.futures


def my_fun(name):
    print(f'started {name}')
    time.sleep(5)
    print(f'ended {name}')
    return True


if __name__ == '__main__':
    print('main start')
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(my_fun, ['foo', 'bar', 'baz'])

    print(f'main end')
