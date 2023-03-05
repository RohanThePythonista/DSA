import concurrent.futures
import time
import threading


class Account:
    def __init__(self, balance):
        self.balance = balance  # shared data
        self.lock = threading.Lock()

    def update(self, txn, amount):
        with self.lock:
            print(f' {txn} thread started...')
            local_copy = self.balance
            local_copy += amount
            time.sleep(1)
            self.balance = local_copy
            print(f' {txn} thread ended...')


if __name__ == '__main__':
    acc = Account(100)
    print(f'starting with initial balance {acc.balance}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as exe:
        for txn, amount in [('deposit', 150), ('withdraw', -150)]:
            exe.submit(acc.update, txn, amount)
    print(f'ending with final balance {acc.balance}')
