# Oscar Yu
# June 11th, 2021

import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizzLock = threading.Lock()
        self.fizzLock.acquire()
        self.buzzLock = threading.Lock()
        self.buzzLock.acquire()
        self.fizzbuzzLock = threading.Lock()
        self.fizzbuzzLock.acquire()
        self.numberLock = threading.Lock()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(self.n // 3 - self.n // 15):
            self.fizzLock.acquire()
            printFizz()
            self.numberLock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n // 5 - self.n // 15):
            self.buzzLock.acquire()
            printBuzz()
            self.numberLock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n//15):
            self.fizzbuzzLock.acquire()
            printFizzBuzz()
            self.numberLock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.numberLock.acquire()
            if i % 15 == 0:
                self.fizzbuzzLock.release()
            elif not i % 5:
                self.buzzLock.release()
            elif not i % 3:
                self.fizzLock.release()
            else:
                printNumber(i)
                self.numberLock.release()